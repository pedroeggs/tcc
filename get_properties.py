import requests
from selenium import webdriver
import time
import csv

with open('to_database.csv', 'r') as csvfile:
    componds = csv.reader(csvfile, delimiter=';')
    nome_dos_compostos = [x[2] for x in componds]
nome_das_propriedades = ['Odor', 'Boiling-Point', 'Melting-Point', 'Flash-Point', 'Solubility', 'Vapor-Pressure', 'Density', 'Vapor-Density', 'pKa']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

i = 1
deu_ruim = []
with open('/home/pedro/Desktop/Properties.csv', 'w') as f:
    for nome_do_composto in nome_dos_compostos:
        r = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{nome_do_composto}/cids/TXT')
        cid = ''
        if r.status_code != 200:
            print(f'Deu errado pra pegar o cid do composto {nome_do_composto}')
        else:
            cid = r.text.strip()
        
        if cid:
            properties_line = f'{nome_do_composto}^^^'
            for propriedade in nome_das_propriedades:
                driver = webdriver.Chrome('/home/pedro/Documents/TCC/chromedriver', options=chrome_options)
                driver.get(f'https://pubchem.ncbi.nlm.nih.gov/compound/{cid}#section={propriedade}&fullscreen=true')
                time.sleep(2)
                properties_line += str([x.text.split("\n")[0] for x in driver.find_elements_by_css_selector(f'#{propriedade} > div.section-content > div.section-content-item')]) + '^^^'
                if propriedade == 'pKa':
                    properties_line += '\n'
                print(properties_line)
                driver.quit()

            print(str(i) + '/' + str(len(nome_dos_compostos)))
            i += 1
            f.write(properties_line)
            print(properties_line)
        else:
            deu_ruim.append(nome_do_composto)

print(deu_ruim)