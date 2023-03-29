import requests
import json

my_req = requests.get('https://swapi.dev/api/starships/')
data = json.loads(my_req.text)


for i in data["results"]:
    if i['name'] == 'Millennium Falcon':

        dct_for_write = {
            'name': i['name'],
            'model': i['model'],
            'starship_class': i['starship_class'],
            'pilots': {}
        }

        for pilot_url in i['pilots']:
            pilot_api = requests.get(pilot_url)
            pilot_data = json.loads(pilot_api.text)

            homeworld_api = requests.get(pilot_data['homeworld'])
            homeworld_data = json.loads(homeworld_api.text)

            pilot = {
                'height': pilot_data['height'],
                'mass': pilot_data['mass'],
                'homeworld': f"{homeworld_data['name']}, {pilot_data['homeworld']}"
            }
            dct_for_write['pilots'][pilot_data['name']] = pilot

        with open('my_test.json', 'w') as file:
            json.dump(dct_for_write, file, indent=4)

        break
for key, val in dct_for_write.items():
    if key == 'pilots':
        print("pilots:")
        for key, val in dct_for_write['pilots'].items():
            print('\tname:', key)
            for key, val in val.items():
                print(f'\t{key}: {val}')
            print()
    else:
        print(f'{key}: {val}')



