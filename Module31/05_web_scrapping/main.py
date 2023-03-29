import re
import requests


my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
data = my_req.text
headers_temp = re.findall(r'\bh3.+>.+</h3\b', data)


for part in headers_temp:
    header_beg = re.search(r'>', part).start() + 1
    header_end = re.search(r'<', part).end() - 1
    print(part[header_beg:header_end])