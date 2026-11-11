import csv, statistics, collections
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data'/'return_to_work_synthetic.csv'
with p.open(newline='',encoding='utf-8') as f:rows=list(csv.DictReader(f))
print('Fictional cases:',len(rows));print('Average days to plan:',round(statistics.mean(int(r['days_to_plan']) for r in rows),1))
print('Fictional closure status counts:',dict(collections.Counter(r['illustrative_outcome'] for r in rows)))
print('NOT APM/ACC data; not evidence of historical return-to-work outcomes.')
