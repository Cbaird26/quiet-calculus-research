#!/usr/bin/env python3
"""New conditional illustrations only; no empirical or inherited-research rerun.
Requires numpy; --figures additionally requires ReportLab. No network or source files.
"""
import argparse, hashlib, json, math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def sat(a):
    z=math.exp(-a)
    return (-a*math.log1p(-z)+sum(z**k/k**2 for k in range(1,1000)))/math.pi**3

def kernel(a,b,n=16384):
    if b==0:return 0.
    # Finite upper bound at a+60; positive exponentially small tail.
    x=np.linspace(a,a+60,n+1);q=x*x-a*a;u=b*np.sqrt(q)
    # Stable 1-sinc(u)^2 near zero, through u^6.
    delta=np.empty_like(u);small=np.abs(u)<.02;u2=u[small]**2
    delta[small]=u2/3-2*u2**2/45+u2**3/315
    delta[~small]=1-np.sinc(u[~small]/np.pi)**2
    occ=np.exp(-x)/(-np.expm1(-x))**2
    y=q*occ*delta
    return float((60/n)/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())/(2*np.pi**3))

def all_results():
    a_values=[.5,1.,3.];bs=np.geomspace(.001,20,101)
    curves=[];maxerr=0.
    for a in a_values:
        vals=[kernel(a,float(b)) for b in bs]
        check_b=[.001,.01,.1,1,3,10,20]
        diffs=[abs(kernel(a,b,32768)-kernel(a,b,16384)) for b in check_b]
        maxerr=max(maxerr,max(diffs))
        assert all(-1e-14<=v<=sat(a)+1e-12 for v in vals)
        curves.append({'m_over_T':a,'b':bs.tolist(),'normalized_rate':[v/sat(a) for v in vals], 'saturation':sat(a),'max_resolution_difference':max(diffs)})
    # Independent Gauss-Legendre quadrature for a=1,b=1.
    nodes,w=np.polynomial.legendre.leggauss(256);x=31+30*nodes
    q=x*x-1;u=np.sqrt(q)
    gauss=float(30*np.dot(w,q*np.exp(-x)/(-np.expm1(-x))**2*(1-np.sinc(u/np.pi)**2))/(2*np.pi**3))
    numeric=kernel(1,1,32768);assert abs(gauss-numeric)<1e-10
    ratio=kernel(1,.002)/kernel(1,.001);assert abs(ratio-4)<.0002
    norm=numeric/sat(1);assert abs(norm-.8161552758397436)<1e-8
    assert maxerr<1e-8
    lam=.7;tau=1.2;theta=.3;v=math.exp(-lam*tau)
    fisher=tau*tau*v*v*math.cos(theta)**2/(1-v*v*math.cos(theta)**2)
    def p(l):return (1+math.exp(-l*tau)*math.cos(theta))/2
    h=1e-5;dp=(p(lam+h)-p(lam-h))/(2*h)
    fnum=dp*dp/(p(lam)*(1-p(lam)));assert abs(fnum-fisher)<1e-9
    ids=['Z1','Z2','Z3','Z4','F1','F2','F3','F4','T1','T2','T3','T4']
    return {'scope':'Version 2 conditional mathematical illustrations, also reproducible in version 3; no laboratory or human data. Fresh research executions are separately recorded in fresh_run_manifest.json.', 'algorithm':'Composite Simpson, n=16384; resolution n=32768; range [a,a+60]; independent Gauss-Legendre order256 at a=b=1.', 'tail_bound_note':'For a>=0.5, b arbitrary, 0<=1-sinc^2<=1. Tail integral bounded by exp(-L)*(L^2+2L+2)/((1-exp(-L))^2*2*pi^3), L=a+60.', 'max_tail_bound':math.exp(-60.5)*(60.5**2+2*60.5+2)/(1-math.exp(-60.5))**2/(2*math.pi**3), 'curves':curves, 'checks':{'bounds':True,'K_at_zero':kernel(1,0),'small_separation_ratio':ratio,'a1_b1_normalized':norm,'gauss_simpson_abs_difference':abs(gauss-numeric),'max_resolution_abs_difference':maxerr,'path_basis_fisher_exact':0.,'interference_fisher':fisher,'interference_finite_difference':fnum,'running_slope':-49/(36*math.pi**2),'spectral_C1_over_C0':2.0841549984043078e-4/1.3093131218139378e-4},'prediction_ids':ids}

def figure(result):
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    p=ROOT/'figures/portal_shape.pdf';c=canvas.Canvas(str(p),pagesize=(510,294),pageCompression=1)
    c.setTitle('Conditional quadratic-portal separation response');c.setAuthor('Christopher Michael Baird; Zora AI assistance')
    left,bottom,width,height=58,51,427,207
    xmin,xmax=-3,math.log10(20)
    def X(b):return left+width*(math.log10(b)-xmin)/(xmax-xmin)
    def Y(y):return bottom+height*y
    c.setFont('Helvetica',9);c.setStrokeColor(HexColor('#d8dfe7'));c.setFillColor(HexColor('#24364b'))
    for y in [0,.25,.5,.75,1]:
        c.line(left,Y(y),left+width,Y(y));c.drawRightString(left-8,Y(y)-3,f'{y:g}')
    for x,label in [(.001,'0.001'),(.01,'0.01'),(.1,'0.1'),(1,'1'),(10,'10')]:
        c.line(X(x),bottom,X(x),bottom+height);c.drawCentredString(X(x),bottom-15,label)
    c.setStrokeColor(HexColor('#24364b'));c.rect(left,bottom,width,height,fill=0,stroke=1)
    colors=['#235c9e','#c76c25','#36816a']
    for curve,color in zip(result['curves'],colors):
        c.setStrokeColor(HexColor(color));c.setLineWidth(1.8);path=c.beginPath()
        for i,(b,y) in enumerate(zip(curve['b'],curve['normalized_rate'])):
            if i==0:path.moveTo(X(b),Y(y))
            else:path.lineTo(X(b),Y(y))
        c.drawPath(path)
    c.setFillColor(HexColor('#24364b'));c.setFont('Helvetica',10)
    c.drawCentredString(left+width/2,17,'Separation b = rT (logarithmic scale)')
    c.saveState();c.translate(17,bottom+height/2);c.rotate(90);c.drawCentredString(0,0,'Rate / large-separation limit');c.restoreState()
    c.setFont('Helvetica-Bold',11);c.drawString(left,277,'Conditional response; no fitted observations')
    for i,(curve,color) in enumerate(zip(result['curves'],colors)):
        x=left+15;y=237-17*i;c.setStrokeColor(HexColor(color));c.line(x,y,x+22,y);c.setFillColor(HexColor('#24364b'));c.setFont('Helvetica',9);c.drawString(x+30,y-3,f"m/T = {curve['m_over_T']:g}")
    c.showPage();c.save()

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--figures',action='store_true');args=parser.parse_args()
    r=all_results();r['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/'data/prediction_checks.json').write_text(json.dumps(r,indent=2)+'\n')
    if args.figures:figure(r)
    print(json.dumps(r['checks'],indent=2))
