#!/usr/bin/env python3
"""Structural artifact checks; requires pypdf and pdfplumber. Not scientific validation."""
import hashlib, json, re
from pathlib import Path
import pdfplumber
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
reader=PdfReader(ROOT/'main.pdf');texts=[p.extract_text() or '' for p in reader.pages];text='\n'.join(texts)
rows=json.loads((ROOT/'data/principles.json').read_text());assert len(rows)==92
missing=[f'P{i:02}' for i in range(1,93) if f'P{i:02}' not in text];assert not missing,missing
assert all(len(t.strip())>40 for t in texts),'Unexpected empty page'
assert '\ufffd' not in text,'Replacement character in output'
source=json.loads((ROOT/'data/source_provenance.json').read_text())
assert hashlib.sha256(Path(source['source_file']).read_bytes()).hexdigest()==source['sha256']
tex='\n'.join(p.read_text() for p in [ROOT/'main.tex',*sorted((ROOT/'sections').glob('*.tex'))])
keys=set(k for group in re.findall(r'\\cite\{([^}]+)\}',tex) for k in group.split(','))
refs=set(re.findall(r'\\bibitem\{([^}]+)\}',(ROOT/'references.tex').read_text()))
assert keys==refs,(keys-refs,refs-keys)
assert len(refs)==33
cards=json.loads((ROOT/'data/prediction_registry.json').read_text())['cards']
assert len(cards)==12
assert all(card['id']+':' in text for card in cards)
research=json.loads((ROOT/'data/research_sources.json').read_text())['sources']
assert len(research)==24
assert all(hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256'] for r in research)
bounds=[]
with pdfplumber.open(ROOT/'main.pdf') as pdf:
    for i,page in enumerate(pdf.pages):
        bad=[ch for ch in page.chars if ch['x0']<0 or ch['x1']>page.width+.1 or ch['top']<0 or ch['bottom']>page.height+.1]
        if bad:bounds.append({'page':i+1,'count':len(bad)})
assert not bounds,bounds
report={'pages':len(reader.pages),'catalogue_items':len(rows),'bibliography_items':len(refs),'all_catalogue_ids_present':True,'all_citation_keys_resolved':True,'out_of_page_text_bounds':bounds,'source_hash_unchanged':True,'replacement_characters':False,'empty_pages':False,'pdf_sha256':hashlib.sha256((ROOT/'main.pdf').read_bytes()).hexdigest(),'prediction_cards':len(cards),'research_sources':len(research),'all_research_hashes_unchanged':True,'scope':'Structural and source-integrity checks only'}
(ROOT/'verification/artifact_audit.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
