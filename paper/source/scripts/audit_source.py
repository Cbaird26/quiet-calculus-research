#!/usr/bin/env python3
"""Read-only audit of the original source. Requires pypdf; source is never copied or modified."""
import argparse, hashlib, json
from pathlib import Path
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('source',type=Path);args=p.parse_args()
source=args.source.resolve();raw=source.read_bytes();digest=hashlib.sha256(raw).hexdigest()
expected='23ab20b0f9a31dfc2e92d3e66100076a4e8db4b90a93f943fc55ca8d9c8f09ba'
assert digest==expected,'This is not the exact PDF analyzed in version 1.0.'
r=PdfReader(source)
rows=[]
for i,page in enumerate(r.pages):
    t=page.extract_text() or ''
    rows.append({'pdf_page':i+1,'printed_folio':i if i else None,'text_characters':len(t),'whitespace_word_count':len(t.split()),'text_sha256':hashlib.sha256(t.encode()).hexdigest()})
report={'source_file':str(source),'bytes':len(raw),'sha256':digest,'pdf_pages':len(r.pages),'page_convention':'Physical PDF page; printed folio = PDF page - 1 after cover','word_count':sum(x['whitespace_word_count'] for x in rows),'metadata':{str(k):str(v) for k,v in r.metadata.items()},'illustrative_pages_visually_reviewed':[1,20,59,63],'pages':rows,'source_modified':False}
(ROOT/'data/source_provenance.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('pages','metadata')},indent=2))
