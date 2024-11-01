import requests

def item_seq_list(name, page=1, numOfRows=10):
    servicekey = "rx55UmYNTIJ7mnCrWgtatEVsuIM2bfyX95AVSjIF/Hzt/gUIkxG8dPRzogYTFravV/w+6Vc02fNWGqgLgGfVeQ=="
    url = "http://apis.data.go.kr/1471000/DrugPrdtPrmsnInfoService06/getDrugPrdtPrmsnDtlInq05"
    params = {
        "serviceKey": servicekey,
        "pageNo": page,
        "numOfRows": numOfRows,
        "item_name": name,
        "type": "json"
    }
    res = requests.get(url, params=params)
    print(res.request.url)
    data = res.json()
    items = data['body']
    if items['totalCount'] == 0:
        return []
    
    return [item['ITEM_SEQ'] for item in items['items']]


print(item_seq_list("브이타민정"))