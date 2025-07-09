import requests
from bs4 import BeautifulSoup
import json

versions=['24r1','24r2']
documents=['clinical-operations','commercial','medical','platform','quality','regulatory']
data=[]
dict1={}
for version in versions:
    list1=[]
    for document in documents:
        url = f'https://rn.veevavault.help/en/lr/archive/{version}/{version}-data-model-changes-{document}/'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            code_components = soup.find('article').find_all('code')
            code_texts=[code_component.text for code_component in code_components]
            dict2={}
            dict2[document]=code_texts
            list1.append(dict2)
        else:
            print(f'URL Error: {url}')
    dict1[version]=list1
data.append(dict1)

with open('vaulte_release.json', 'w') as file:
    json.dump(data, file)