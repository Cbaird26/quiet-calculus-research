#!/usr/bin/env python3
"""Compile a portable pdfLaTeX project and fail on unresolved or layout diagnostics."""
import hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
exe=shutil.which('pdflatex')
if exe is None and Path('/Library/TeX/texbin/pdflatex').exists():exe='/Library/TeX/texbin/pdflatex'
if exe is None:raise SystemExit('pdfLaTeX is required. Install a TeX distribution or compile main.tex on Overleaf.')
verify=ROOT/'verification';verify.mkdir(exist_ok=True)
version=subprocess.check_output([exe,'--version'],text=True).splitlines()[0]
for i in range(1,4):
    p=subprocess.run([exe,'-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','main.tex'],cwd=ROOT,capture_output=True,text=True)
    (verify/f'pdflatex-pass-{i}.txt').write_text(p.stdout+p.stderr)
    if p.returncode:
        print((p.stdout+p.stderr)[-6000:]);raise SystemExit(p.returncode)
log=(ROOT/'main.log').read_text(errors='replace')
issues=[x for x in log.splitlines() if re.search(r'(^!|Warning|Overfull|Underfull|undefined|Missing character)',x)]
report={'compiler':version,'passes':3,'success':not issues,'diagnostics':issues,'pdf_bytes':(ROOT/'main.pdf').stat().st_size,'pdf_sha256':hashlib.sha256((ROOT/'main.pdf').read_bytes()).hexdigest(),'scope':'Artifact compilation, not empirical validation'}
(verify/'build_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if issues:sys.exit(2)
