#!/usr/bin/env python3
"""Plot saved fresh simulation contrasts; does not rerun or relabel experiments."""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
ROOT=Path(__file__).resolve().parents[1]
r=json.loads((ROOT/'data/fresh_memory_summary.json').read_text())
rows=list(r['scenarios'].items())+[('Scenario average',r['combined'])]
c=canvas.Canvas(str(ROOT/'figures/fresh_memory_results.pdf'),pagesize=(520,350),pageCompression=1)
c.setTitle('Fresh adaptive-memory test: benefits and harms across scenarios')
left,right,top,bottom=138,496,299,61;xmin,xmax=-7.5,2.3
X=lambda x:left+(right-left)*(x-xmin)/(xmax-xmin)
c.setFont('Helvetica-Bold',11);c.setFillColor(HexColor('#24364b'));c.drawString(12,332,'Adaptive minus validation-selected fixed memory')
c.setFont('Helvetica',9);c.drawString(12,316,'Synthetic paths; lower loss is better; fixed hazard = 0.05')
c.setStrokeColor(HexColor('#e0e5eb'));c.setFont('Helvetica',8)
for x in [-7,-6,-5,-4,-3,-2,-1,0,1,2]:
 c.line(X(x),bottom,X(x),top+5);c.drawCentredString(X(x),bottom-13,str(x))
c.setStrokeColor(HexColor('#536273'));c.setLineWidth(.8);c.line(X(0),bottom,X(0),top+5)
c.setStrokeColor(HexColor('#b74431'));c.setDash(3,3);c.line(X(1),bottom,X(1),top+5);c.setDash()
for i,(name,v) in enumerate(rows):
 y=top-i*20
 if name=='Scenario average':
  c.setStrokeColor(HexColor('#a8b2be'));c.line(10,y+10,right,y+10)
 color=HexColor('#b74431' if v['mean']>0 else '#246c91')
 c.setStrokeColor(color);c.setFillColor(color);c.setLineWidth(1.3)
 lo,hi=[x*1000 for x in v['ci95']];mean=v['mean']*1000
 c.line(X(lo),y,X(hi),y);c.line(X(lo),y-3,X(lo),y+3);c.line(X(hi),y-3,X(hi),y+3);c.circle(X(mean),y,2.6,fill=1,stroke=0)
 c.setFillColor(HexColor('#24364b'));c.setFont('Helvetica-Bold' if name=='Scenario average' else 'Helvetica',8.5);c.drawRightString(left-9,y-3,name.replace('_',' '))
c.setFont('Helvetica',9);c.drawCentredString((left+right)/2,25,'Paired Brier difference (units of 0.001)')
c.setFont('Helvetica',8);c.drawString(12,7,'Robust-benefit gate: failed. Intervals are pointwise; formal harm gate uses simultaneous bounds.')
c.showPage();c.save()
print(ROOT/'figures/fresh_memory_results.pdf')
