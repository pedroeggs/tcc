# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:50:42 2019

@author: Arthur

Lê o arquivo .csv com os SMILES, puxa seus nomes e fórmulas do pubChem e coloca em uma planilha do Excel
"""

import pubchempy as pcp
import csv
import xlsxwriter

def read_csv():
  
    # abre o arquivo
    with open(r'C:\TCC\molecules.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        # faz uma lista com ele. Por isso, é diferente da função read_molecule_csv()
        table_list = list(reader)
        
    return table_list

def import_from_pubchem():
    
    compounds = read_csv()
    # cria uma planilha no mesmo local do arquivo .py
    workbook = xlsxwriter.Workbook(filename='to_database.xlsx')
    # cria uma aba
    worksheet = workbook.add_worksheet(name='results')
    row = 1
    
    print('\nEstabelecendo conexão com o PubChem...')
    # para cada composto na tabela
    for comp in compounds:
        
        # pega dados no pubChem
        results = pcp.get_compounds(comp[0], 'smiles')
        # baixa a imagem de composto
        pcp.download('PNG', 'C:\\TCC\\images\\' + comp[0] + '.png', comp[0], 'smiles', overwrite=True)
        
        # para cada resultado, escreve na planilha nova o SMILES, o odor, o nome IUPAC e a fórmula molecular
        for c in results:
            print('\nComposto ' + c.iupac_name)
            worksheet.write(row, 0, comp[0])
            worksheet.write(row, 1, comp[1])
            worksheet.write(row, 2, c.iupac_name)
            worksheet.write(row, 3, c.molecular_formula)
            row += 1
            
    workbook.close()
    print('Pronto! Compostos Atualizados')

import_from_pubchem()