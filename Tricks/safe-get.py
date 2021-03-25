# if u not sure about if what u want to get is really exist or not u can use safe get to avoid the error that come up to u in case of the jey not exist at all

dic.get('key','what u want to print in case of deosn\'t exist mostly using None or N/A ')


event ={0: 'a', 1: 'b', 2: 'c', 3: 'd',"queryStringParameters": {"postcode": 12345}}

postcode = event.get('queryStringParameters',"not found").get("postcode","N/A")
print(postcode)
