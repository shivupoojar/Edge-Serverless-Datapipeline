import json
def handle(req):
    data = { "result":"Not found","text":req}
    words = req.split()
    for word in words:
      if word=="shiva":
        data = {"result":"Success","text":req} 


    return json.dumps(data)

