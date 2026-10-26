#!/usr/bin/env python3
"""Vector figure from saved held-out contrasts; does not rerun any experiment."""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,Color
ROOT=Path(__file__).resolve().parents[1]
r=json.loads((ROOT/'data/revision_memory_summary.json').read_text());s=r['combined']
names=list(s['scenarios']);names.insert(11,'known_average')
w,h=720,590;c=canvas.Canvas(str(ROOT/'figures/revision_memory_results.pdf'),pagesize=(w,h),invariant=1)
left,right,top,bottom=170,690,496,70
xmin,xmax=-7.,2.
X=lambda value:left+(value-xmin)/(xmax-xmin)*(right-left)
c.setFont('Helvetica-Bold',14);c.setFillColor(HexColor('#183244'));c.drawString(28,561,'Revised memory on new held-out paths')
c.setFont('Helvetica',10);c.drawString(28,543,'Both policies compared with the same validation-selected fixed baseline; lower loss is better')
colors={'adaptive-minus-fixed':HexColor('#7e8790'),'revised-minus-fixed':HexColor('#006c87')}
for j,(key,label) in enumerate([('adaptive-minus-fixed','Original adaptive policy, fresh paths'),('revised-minus-fixed','Revised causal gate, fresh paths')]):
 x=35+j*332;c.setStrokeColor(colors[key]);c.setLineWidth(2);c.line(x,521,x+18,521);c.setFillColor(colors[key]);c.circle(x+9,521,2,fill=1,stroke=0);c.setFillColor(HexColor('#183244'));c.setFont('Helvetica',9);c.drawString(x+23,517,label)
for tick in range(-7,3):
 c.setStrokeColor(HexColor('#d9e1e7'));c.setLineWidth(.5);c.line(X(tick),bottom+18,X(tick),top+2)
 c.setFont('Helvetica',9);c.setFillColor(HexColor('#425466'));c.drawCentredString(X(tick),bottom+3,str(tick))
c.setStrokeColor(HexColor('#596876'));c.setLineWidth(.8);c.line(X(0),bottom+18,X(0),top+2)
c.setStrokeColor(HexColor('#c75342'));c.setDash(3,3);c.line(X(1),bottom+18,X(1),top+2);c.setDash()
for i,name in enumerate(names):
 y=top-i*28
 if name=='known_average':
  c.setStrokeColor(HexColor('#80909d'));c.line(28,y+16,690,y+16);c.line(28,y-16,690,y-16)
  values=s['known_scenario_average'];label='Known-family average'
 else:
  values=s['scenarios'][name]['contrasts'];label=name.replace('_',' ')
  if i>11:label+=' *'
 c.setFillColor(HexColor('#183244'));c.setFont('Helvetica-Bold' if name=='known_average' else 'Helvetica',10);c.drawRightString(left-12,y-3,label)
 for key,offset in [('adaptive-minus-fixed',4),('revised-minus-fixed',-4)]:
  d=values[key]['brier'];yy=y+offset;lo,hi=[v*1000 for v in d['ci95']];mu=d['mean']*1000
  c.setStrokeColor(colors[key]);c.setFillColor(colors[key]);c.setLineWidth(1.15);c.line(X(lo),yy,X(hi),yy);c.line(X(lo),yy-2.6,X(lo),yy+2.6);c.line(X(hi),yy-2.6,X(hi),yy+2.6);c.circle(X(mu),yy,2.4,stroke=0,fill=1)
c.setFont('Helvetica',10);c.setFillColor(HexColor('#183244'));c.drawCentredString((left+right)/2,49,'Paired Brier loss minus fixed baseline (units of 0.001)')
c.setFont('Helvetica',9);c.drawString(28,28,'Bars: pointwise 95% Monte Carlo intervals. Red line: +0.001 harm margin, formally tested on known families only.')
c.drawString(28,14,'* New exploratory families: excluded from tuning and both primary gates; the fixed policy remains better on these families.')
c.save();print('Generated figures/revision_memory_results.pdf')
