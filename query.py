# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import sqlite3
from sqlite3 import Error
import csv
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn
 
 
def create_table(conn, create_table_sql):
    
    
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
        
    Fonte: https://www.sqlitetutorial.net/sqlite-python/create-tables/
        
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
 
 
def create_db():
    
    '''
    Fonte: https://www.sqlitetutorial.net/sqlite-python/create-tables/
    
    '''
    
    database = r"C:/TCC/camd_db.db"
 
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS molecule_table (
                                        smiles text NOT NULL,
                                        odour text NOT NULL,
                                        compound_name text PRIMARY KEY,
                                        formula text NOT NULL
                                    ); """  # adicionar dps compound_name text NOT NULL
 
    # create a database connection
    conn = create_connection(database)
 
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")
        
        
def read_molecule_csv():
    
    '''
    Transforma um arquivo .csv em lista
    '''
    
    with open(r'C:\TCC\to_database.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        table_list = list(map(tuple, reader))
        
    return table_list

def update_db():
    
    # Lê o arquivo com os compostos
    values_list = read_molecule_csv()    

    database = r"C:/TCC/camd_db.db"   
    conn = create_connection(database)
    
    try:
        c = conn.cursor()
        # inserir a tabela dos compostos no banco de dados
        c.executemany("""
        INSERT INTO molecule_table (smiles, odour, compound_name, formula)
        VALUES (?,?,?,?)
        """, values_list)
        
        conn.commit()

        print('Dados inseridos com sucesso.')
        
        conn.close()
        
    except Error as e:
        print(e)

def get_data(column_filter, search_parameter):
    
    database = r"C:/TCC/camd_db.db"   
    conn = create_connection(database)
    result_list = []
    try:
        c = conn.cursor()
        # 
        c.execute("""
        SELECT * FROM molecule_table  WHERE """ + column_filter +  """ LIKE '%""" +
        search_parameter + """%'       
        """)
        
        for row in c.fetchall():
            result_list.append(row)
        
        conn.close()
        return result_list
        
    except Error as e:
        print(e)
        



