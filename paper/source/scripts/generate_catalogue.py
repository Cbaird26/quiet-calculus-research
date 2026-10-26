#!/usr/bin/env python3
"""Build the complete page-indexed scientific catalogue from a plain-text audit table."""
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'data/principles.psv').open(),delimiter='|'))
assert [int(r['id']) for r in rows]==list(range(1,93))
def esc(s):
    return s.replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
head=r'''\section{Complete source-grounded principle catalogue}
\label{app:catalogue}
This catalogue contains 92 distinct coded items, including methodological principles, hypotheses, ethical commitments, and fictional boundaries. It is not a list of 92 established scientific laws. Rows marked H require testing; rows marked F do not describe observed reality. M, E, and N have the meanings in Table~\ref{tab:status}. All locators are physical PDF pages. Close interpretations and critical extensions are identified in their wording.
\small
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.055\linewidth}>{\raggedright\arraybackslash}p{0.735\linewidth}>{\raggedright\arraybackslash}p{0.15\linewidth}@{}}
\toprule
ID & Principle and scientific qualification & Pages; class\\\midrule
\endfirsthead
\toprule
ID & Principle and scientific qualification (continued) & Pages; class\\\midrule
\endhead
\bottomrule
\endfoot
'''
body=''.join(f"P{int(r['id']):02d} & \\textbf{{{esc(r['principle'])}.}} {esc(r['qualification'])} & {r['pages']}; {r['status']}\\\\[0.5em]\n" for r in rows)
(ROOT/'sections/08_catalogue.tex').write_text(head+body+'\\end{longtable}\n\\normalsize\n')
(ROOT/'data/principles.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Generated 92 catalogue entries')
