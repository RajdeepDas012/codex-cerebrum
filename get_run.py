import json
try:
    with open('data/knowledge_base.json') as f:
        d = json.load(f)
    print(d.get('meta', {}).get('total_runs', '?'))
except Exception:
    print('?')
