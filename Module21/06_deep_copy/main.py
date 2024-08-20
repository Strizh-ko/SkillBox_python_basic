import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

def replacement(name, site):
    site['html']['head']['title'] = site['html']['head']['title'][0:13] + name + site['html']['head']['title'][20:]
    site['html']['body']['h2'] = site['html']['body']['h2'][:27] + name

def site_copy(num):
    for _ in range(num):
        site_copy = copy.deepcopy(site)
        name = input('Введите название продукта для нового сайта: ')
        replacement(name, site_copy)
        site_dct[name] = site_copy
        for name, new_site in site_dct.items():
            print(f'''\nСайт для {name}
site = {new_site}''')

num = int(input('Введите количество копий: '))
site_dct = {}
site_copy(num)

