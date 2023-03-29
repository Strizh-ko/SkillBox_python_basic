import json


def findkey(key, dct: dict):
    if key in dct:
        return dct[key]
    for k, val in dct.items():
        if type(val) == dict:
            return findkey(key, val)


diff_list = ['status', "services", "staff", "datetime"]
result = dict()

with open('json_old.json', 'r') as old_file:
    with open('json_new.json', 'r') as new_file:
        old, new = json.loads(old_file.read()), json.loads(new_file.read())

for key in diff_list:
    vo = findkey(key, old)
    vn = findkey(key, new)
    if vo != vn:
        result[key] = vn
print(result)

with open('result.json', 'w') as file:
    json.dump(result, file, indent=4)


