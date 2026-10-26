#!/usr/bin/env python3
"""Deterministic toy calculations. No empirical measurements or participant data.
Run with Python 3. Standard library suffices for all numbers and TeX tables.
Add --figures to regenerate the vector figure (requires reportlab).
"""
import argparse, itertools, json, math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
q=Fraction(7,10)
forecasts=[Fraction(1,2),q,Fraction(19,20)]
scores=[{'p':float(p),'expected_brier':float(q*(p-1)**2+(1-q)*p**2)} for p in forecasts]
for p in forecasts:
    assert q*(p-1)**2+(1-q)*p**2 == (p-q)**2+q*(1-q)
routes=[{'route':'A','nominal_cost':1.0,'margin':.12,'L':1.0}, {'route':'B','nominal_cost':1.25,'margin':.35,'L':1.0}]
epsilon=.20
for r in routes:r['certified_residual']=round(r['margin']-r['L']*epsilon,8)
assert routes[0]['certified_residual']<0<routes[1]['certified_residual']
# Here g=c-delta exactly, so failure of A at delta=.2 is an actual violation,
# not merely a failure to certify. General Lipschitz bounds need not be tight.
due={'A':4,'B':3,'C':7};weights={'A':1,'B':2,'C':1};penalties={'A':10,'B':8,'C':6}
scenarios=[{'A':a,'B':2,'C':c} for a in (1,5) for c in (2,4)]
schedule=[]
for order in itertools.permutations('ABC'):
    losses=[]; delays=[]; misses=[]
    for duration in scenarios:
        clock=0;loss=0;delay=0;miss=0
        for job in order:
            clock+=duration[job]
            tardy=max(0,clock-due[job]);m=int(clock>due[job])
            loss+=weights[job]*tardy+penalties[job]*m
            delay+=tardy;miss+=m
        losses.append(loss);delays.append(delay);misses.append(miss)
    schedule.append({'order':''.join(order),'scenario_losses':losses,'expected_loss':sum(losses)/4,'expected_unweighted_tardiness':sum(delays)/4,'expected_missed_connections':sum(misses)/4})
schedule.sort(key=lambda d:(d['expected_loss'],d['order']))
assert len(schedule)==math.factorial(3)
cohorts=[{'p':p,'all_30':p**30} for p in (.90,.95,.99)]
# An independent special-case check: for order B,A,C the completions are
# 2,2+A,2+A+C. B never misses; A misses iff A=5; C misses in (5,2),(5,4).
manual_bac=(0+0+21+23)/4
# The scenario loss expressions below make the analytic check inspectable.
manual_losses=[]
for a,c in itertools.product((1,5),(2,4)):
    manual_losses.append(max(0,2+a-4)+10*int(2+a>4)+max(0,2+a+c-7)+6*int(2+a+c>7))
assert next(r for r in schedule if r['order']=='BAC')['scenario_losses']==manual_losses
assert next(r for r in schedule if r['order']=='BAC')['expected_loss']==manual_bac
results={'status':'synthetic illustration only','q':float(q),'epsilon':epsilon,'brier':scores,'routes':routes,'cohort':cohorts,'scheduling':{'jobs':{'due':due,'weights':weights,'miss_penalties':penalties},'scenarios':scenarios,'scenario_probability':.25,'ranked_orders':schedule},'checks':{'brier_identity_exact_rational':True,'robust_route_counterexample':True,'six_orders_enumerated':True,'BAC_completion_formula_agrees':True}}
(ROOT/'data/toy_results.json').write_text(json.dumps(results,indent=2)+'\n')
lines=[r'\begin{table}[htbp]\centering\small',r'\begin{tabular}{lrrr}\toprule',r'Order & Expected loss & Expected tardiness & Expected misses\\\midrule']
for r in schedule:lines.append(f"{r['order']} & {r['expected_loss']:.2f} & {r['expected_unweighted_tardiness']:.2f} & {r['expected_missed_connections']:.2f}\\\\")
lines += [r'\bottomrule\end{tabular}',r'\caption{Exact enumeration for the four equally likely synthetic loading scenarios. Tardiness is summed across jobs in time units. The loss includes declared priority weights and missed-connection penalties.}\label{tab:schedules}',r'\end{table}']
(ROOT/'data/schedule_table.tex').write_text('\n'.join(lines)+'\n')
(ROOT/'data/result_macros.tex').write_text('\\newcommand{\\BestOrder}{'+schedule[0]['order']+'}\n\\newcommand{\\BestLoss}{'+f"{schedule[0]['expected_loss']:.2f}"+'}\n')
if argparse.ArgumentParser().parse_known_args()[1] == ['--figures']:
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    c=canvas.Canvas(str(ROOT/'figures/toy_results.pdf'),pagesize=(540,240),invariant=1)
    navy=HexColor('#1b4458'); rust=HexColor('#b04e29'); gray=HexColor('#60717a')
    def plot(x0,y0,w,h,xmax,ymin,ymax,title,xlabel,ylabel,curves,xticks,yticks):
        def xy(x,y):return x0+x/xmax*w,y0+(y-ymin)/(ymax-ymin)*h
        c.setFont('Helvetica-Bold',10);c.setFillColor(navy);c.drawString(x0,y0+h+27,title)
        c.setStrokeColor(gray);c.setLineWidth(.5)
        for y in yticks:
            xx,yy=xy(0,y);c.setStrokeColor(HexColor('#dbe2e5'));c.line(x0,yy,x0+w,yy)
            c.setFillColor(gray);c.setFont('Helvetica',8);c.drawRightString(x0-5,yy-3,f'{y:.2f}')
        c.setStrokeColor(gray);c.line(x0,y0,x0+w,y0);c.line(x0,y0,x0,y0+h)
        for x in xticks:
            xx,yy=xy(x,ymin);c.line(xx,yy,xx,yy-3);c.setFont('Helvetica',8);c.drawCentredString(xx,yy-13,f'{x:.1f}')
        c.setFont('Helvetica',9);c.drawCentredString(x0+w/2,y0-29,xlabel)
        c.saveState();c.translate(x0-34,y0+h/2);c.rotate(90);c.drawCentredString(0,0,ylabel);c.restoreState()
        for fn,col in curves:
            p=c.beginPath()
            for n in range(101):
                x=n*xmax/100; xx,yy=xy(x,fn(x))
                if n==0:p.moveTo(xx,yy)
                else:p.lineTo(xx,yy)
            c.setStrokeColor(col);c.setLineWidth(1.8);c.drawPath(p)
        return xy
    xy=plot(48,48,195,145,.4,-.3,.4,'A. Bounded-perturbation margin','Disturbance bound epsilon','Residual constraint margin',[(lambda x:.12-x,rust),(lambda x:.35-x,navy)],[0,.1,.2,.3,.4],[-.2,0,.2,.4])
    for y,label,col in [(.12,'Route A',rust),(.35,'Route B',navy)]:
        c.setFillColor(col);c.setFont('Helvetica',8);xx,yy=xy(.03,y-.03);c.drawString(xx+3,yy+7,label)
    xx,_=xy(.2,0);c.setDash(3,3);c.setStrokeColor(gray);c.line(xx,48,xx,193);c.setDash()
    xy2=plot(319,48,195,145,1,.18,.72,'B. Expected forecast loss','Issued probability p','Expected binary Brier score',[(lambda p:(p-.7)**2+.21,navy)],[0,.2,.4,.6,.8,1],[.2,.4,.6])
    xx,yy=xy2(.7,.21);c.setFillColor(rust);c.circle(xx,yy,3,fill=1,stroke=0);c.setFont('Helvetica',8);c.drawString(xx-37,yy+12,'Minimum at p = 0.7')
    c.save()
print(json.dumps(results,indent=2))
