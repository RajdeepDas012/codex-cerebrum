import json
try:
    with open('data/knowledge_base.json') as f:
        d = json.load(f)
    e = d['entries'][-1]
    topic = e.get('topic', 'unknown')
    cat = e.get('category', '?')
    print(topic + ' [' + cat + ']')
except Exception:
    print('update')
