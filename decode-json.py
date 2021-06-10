import json

json_str = '{"cat":[{"name":"mustafa","Address":"Iraq","class":"Royal"},\
{"name":"Mena","Address":"USA","class":"Royal"},\
{"name":"Yousif","Address":"England","class":"Royal"}]}'

json_hash = json.loads(json_str)

#print(json_hash)
#print("json_hash:", json_hash["Address"])

addresses = []


for obj in json_hash["cat"]:
    print("obj: ", obj)
    addresses.append(obj["Address"])

print("addresses: ", addresses)
