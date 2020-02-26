# -*- coding: utf-8 -*-
"""
Autores:
    
    Arthur Adabo de Camargo, nº USP: 9834128
    Pedro Alvares Eggers, nº USP: 9833440

Fonte: https://www.sqlitetutorial.net/sqlite-python/create-tables/

"""

import sqlite3
from sqlite3 import Error
import csv
import os

CURR_PATH = os.path.dirname(os.path.abspath(__file__))


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
        
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_db():

    """
    Fonte: https://www.sqlitetutorial.net/sqlite-python/create-tables/
    
    """

    database = os.path.join(CURR_PATH, "camd_db.db")

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS molecule_table (
                                        smiles text NOT NULL,
                                        odour text NOT NULL,
                                        compound_name text PRIMARY KEY,
                                        formula text NOT NULL,
                                        boiling_point text NOT NULL,
                                        melting_point text NOT NULL,
                                        flash_point text NOT NULL,
                                        solubility text NOT NULL,
                                        vapor_pressure text NOT NULL,
                                        density text NOT NULL,
                                        vapor_density text NOT NULL,
                                        pka text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")


def read_molecule_csv():

    """
    Transforma um arquivo .csv em lista
    """

    with open(os.path.join(CURR_PATH, "to_database.csv"), "r") as f:
        reader = csv.reader(f, delimiter=";")
        table_list = list(map(tuple, reader))

    return table_list


def update_db(values_list):

    database = os.path.join(CURR_PATH, "camd_db.db")
    conn = create_connection(database)
    print(values_list)

    try:
        c = conn.cursor()

        c.executemany(
            """
        INSERT OR REPLACE INTO molecule_table (smiles, odour, compound_name, formula, boiling_point, melting_point, 
        flash_point, solubility, vapor_pressure, density, vapor_density, pka)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?) 
        """,
            values_list,
        )

        conn.commit()

        print("Dados inseridos com sucesso.")

        conn.close()

    except Error as e:
        print(e)


def new_get_data(
    smiles="",
    compound_name="",
    formula="",
    boiling_point="",
    melting_point="",
    flash_point="",
    solubility="",
    vapor_pressure="",
    density="",
    vapor_density="",
    pka="",
    odour="",
):
    query = f"SELECT * FROM molecule_table WHERE smiles LIKE '%{smiles}%' AND compound_name LIKE '%{compound_name}%' AND formula LIKE '%{formula}%' AND boiling_point LIKE '%{boiling_point}%' AND melting_point LIKE '%{melting_point}%' AND flash_point LIKE '%{flash_point}%' AND solubility LIKE '%{solubility}%' AND vapor_pressure LIKE '%{vapor_pressure}%' AND density LIKE '%{density}%' AND vapor_density LIKE '%{vapor_density}%' AND pka LIKE '%{pka}%' AND odour LIKE '%{odour}%'"
    database = os.path.join(CURR_PATH, "camd_db.db")
    conn = create_connection(database)
    c = conn.cursor()
    aux = c.execute(query).fetchall()
    conn.close()

    return list(aux)


def get_data(search_parameters):

    compound = search_parameters[0]
    formula = search_parameters[1]
    odour = search_parameters[2]

    # Modifica a query baseado em quais parâmetros foram dados
    query = "SELECT * FROM molecule_table"

    if compound != "":

        query += """ WHERE compound_name LIKE '%""" + compound + """%'"""

        if formula != "":

            query += """ AND formula LIKE '%""" + formula + """%'"""

        if odour != "":

            query += """ AND odour LIKE '%""" + odour + """%'"""

    elif formula != "":

        query += """ WHERE formula LIKE '%""" + formula + """%'"""
        if odour != "":

            query += """ AND odour LIKE '%""" + odour + """%'"""

    elif odour != "":

        query += """ WHERE odour LIKE '%""" + odour + """%'"""

    database = os.path.join(CURR_PATH, "camd_db.db")
    conn = create_connection(database)
    result_list = []
    try:

        c = conn.cursor()
        # match parcial no banco de dados
        c.execute(query)

        for row in c.fetchall():
            result_list.append(row)

        conn.close()
        return result_list

    except Error as e:
        print(e)


# create_db()
# update_db(read_molecule_csv())

