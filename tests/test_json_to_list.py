import json


def test_ids():
    list=[]
    with open('lozon_id.json', 'r', encoding='utf-8') as f:
        polygons = json.load(f)
    for p in polygons:
        list.append(str(p['lozon_id']))
    print(list)



