'''

Fonte: https://www.dcc.ufrj.br/~fabiom/mab225/tutorialtkinter.pdf

'''

import tkinter as tk
from tkinter import messagebox
import query
import os

CURR_PATH = os.path.dirname(os.path.abspath(__file__))

class Window_Add:
    
    def __init__(self, master):
        
        # Frame do Topo (pesquisa de compostos)
        
        self.add_frame = tk.Frame(master=master, highlightbackground='black', highlightcolor='black',
                                    highlightthickness=1)
        
        self.add_frame.place(x=0, y=0, relwidth=1, relheight=1)
        #self.add_frame.pack(side='top', anchor='nw', padx=5, pady=5, fill='x')
        
        # Adicionar nome
        
        self.add_frame_title = tk.Label(master=self.add_frame, text='Nome: ')
        self.add_frame_title.place(x=5,y=5)
        
        self.compound_var_add = tk.StringVar()
        self.compound_entry = tk.Entry(master=self.add_frame, textvariable=self.compound_var_add, fg='grey')
        self.compound_entry.place(x=7,y=27, relwidth=0.1, height=28) 
        
        # Adicionar fórmula
        
        self.formula_add_frame_title = tk.Label(master=self.add_frame, text='Fórmula: ')
        self.formula_add_frame_title.place(x=305,y=5)
        
        self.formula_var_add = tk.StringVar()
        self.formula_entry = tk.Entry(master=self.add_frame, textvariable=self.formula_var_add, fg='grey')
        self.formula_entry.place(x=307,y=27, relwidth=0.1, height=28)
        
        # Adicionar aroma
        
        self.odour_add_frame_title = tk.Label(master=self.add_frame, text='Aroma: ')
        self.odour_add_frame_title.place(x=605,y=5)
        
        self.odour_var_add = tk.StringVar()
        self.odour_entry = tk.Entry(master=self.add_frame, textvariable=self.odour_var_add, fg='grey')
        self.odour_entry.place(x=607,y=27, relwidth=0.1, height=28)

        # Adicionar SMILES
        
        self.smiles_add_frame_title = tk.Label(master=self.add_frame, text='SMILES: ')
        self.smiles_add_frame_title.place(x=5,y=85)
        
        self.smiles_var_add = tk.StringVar()
        self.smiles_entry = tk.Entry(master=self.add_frame, textvariable=self.smiles_var_add, fg='grey')
        self.smiles_entry.place(x=7,y=107, relwidth=0.1, height=28)

        # Adicionar Ponto de Ebulição
        
        self.BP_add_frame_title = tk.Label(master=self.add_frame, text='Ponto de Ebulição: ')
        self.BP_add_frame_title.place(x=305,y=85)
        
        self.BP_var_add = tk.StringVar()
        self.BP_entry = tk.Entry(master=self.add_frame, textvariable=self.BP_var_add, fg='grey')
        self.BP_entry.place(x=307,y=107, relwidth=0.1, height=28)

        # Adicionar Ponto de Fusão
        
        self.MP_add_frame_title = tk.Label(master=self.add_frame, text='Ponto de Fusão: ')
        self.MP_add_frame_title.place(x=605,y=85)
        
        self.MP_var_add = tk.StringVar()
        self.MP_entry = tk.Entry(master=self.add_frame, textvariable=self.MP_var_add, fg='grey')
        self.MP_entry.place(x=607,y=107, relwidth=0.1, height=28)

        # Adicionar Ponto de Flash
        
        self.FP_add_frame_title = tk.Label(master=self.add_frame, text='Ponto de Flash: ')
        self.FP_add_frame_title.place(x=5,y=165)
        
        self.FP_var_add = tk.StringVar()
        self.FP_entry = tk.Entry(master=self.add_frame, textvariable=self.FP_var_add, fg='grey')
        self.FP_entry.place(x=7,y=187, relwidth=0.1, height=28)

        # Adicionar Solubilidade
        
        self.solubility_add_frame_title = tk.Label(master=self.add_frame, text='Solubilidade: ')
        self.solubility_add_frame_title.place(x=305,y=165)
        
        self.solubility_var_add = tk.StringVar()
        self.solubility_entry = tk.Entry(master=self.add_frame, textvariable=self.solubility_var_add, fg='grey')
        self.solubility_entry.place(x=307,y=187, relwidth=0.1, height=28)

        # Adicionar Pressão de Vapor
        
        self.VP_add_frame_title = tk.Label(master=self.add_frame, text='Pressão de Vapor: ')
        self.VP_add_frame_title.place(x=605,y=165)
        
        self.VP_var_add = tk.StringVar()
        self.VP_entry = tk.Entry(master=self.add_frame, textvariable=self.VP_var_add, fg='grey')
        self.VP_entry.place(x=607,y=187, relwidth=0.1, height=28)

        # Adicionar Densidade
        
        self.density_add_frame_title = tk.Label(master=self.add_frame, text='Densidade: ')
        self.density_add_frame_title.place(x=5,y=245)
        
        self.density_var_add = tk.StringVar()
        self.density_entry = tk.Entry(master=self.add_frame, textvariable=self.density_var_add, fg='grey')
        self.density_entry.place(x=7,y=267, relwidth=0.1, height=28)

        # Adicionar Densidade de Vapor
        
        self.vapor_density_add_frame_title = tk.Label(master=self.add_frame, text='Densidade de Vapor: ')
        self.vapor_density_add_frame_title.place(x=305,y=245)
        
        self.vapor_density_var_add = tk.StringVar()
        self.vapor_density_entry = tk.Entry(master=self.add_frame, textvariable=self.vapor_density_var_add, fg='grey')
        self.vapor_density_entry.place(x=307,y=267, relwidth=0.1, height=28)

        # Adicionar pKa
        
        self.pka_add_frame_title = tk.Label(master=self.add_frame, text='pKa: ')
        self.pka_add_frame_title.place(x=605,y=245)
        
        self.pka_var_add = tk.StringVar()
        self.pka_entry = tk.Entry(master=self.add_frame, textvariable=self.pka_var_add, fg='grey')
        self.pka_entry.place(x=607,y=267, relwidth=0.1, height=28)

        self.search_btn = tk.Button(master=self.add_frame, text='Adicionar composto ao banco de dados',
                                            command=lambda: self.add_compound())
        self.search_btn.place(x=300, y=350, height=28)
        
    def add_compound(self):
        
        # lista dos parâmetros (em tuple) dados pelo usuário
        # o erro acontece aqui, deveria preencher tudo mas fica tudo como string vazia
        # rodando esse arquivo sozinho, preenche ok
        add_parameters = [(self.smiles_var_add.get(), self.odour_var_add.get(), 
                        self.compound_var_add.get(), self.formula_var_add.get(), 
                        self.BP_var_add.get(), self.MP_var_add.get(), self.FP_var_add.get(), 
                        self.solubility_var_add.get(), self.VP_var_add.get(), 
                        self.density_var_add.get(), self.vapor_density_var_add.get(),
                        self.pka_var_add.get())]

        print(add_parameters)

        # 'aperta' o botão
        self.search_btn.configure(relief='sunken')

        # checa se o usuário colocou nome e fórmula
        if add_parameters[0][0] == '':    

            messagebox.showinfo('Erro','O composto deve ter um nome, uma fórmula e pelo menos uma propriedade. Por favor, verifique.')
            
        else:

            param_found = False

            # checa se o usuário colocou pelo menos um parâmetro
            for i in range(len(add_parameters[0])):

                if i != 0 and add_parameters[0][i] != '':
                    param_found = True
                    break

            if not param_found:    

                messagebox.showinfo('Erro','O composto deve ter um nome, uma fórmula e pelo menos uma propriedade. Por favor, verifique.')
            
            else:
            
                # adiciona os dados ao banco de dados
                added = query.update_db(add_parameters)

                # limpa os campos de entrada

                self.smiles_entry.delete(0,'end')
                self.odour_entry.delete(0,'end')
                self.compound_entry.delete(0,'end')
                self.formula_entry.delete(0,'end') 
                self.BP_entry.delete(0,'end')
                self.MP_entry.delete(0,'end')
                self.FP_entry.delete(0,'end') 
                self.solubility_entry.delete(0,'end')
                self.VP_entry.delete(0,'end'), 
                self.density_entry.delete(0,'end')
                self.vapor_density_entry.delete(0,'end')
                self.pka_entry.delete(0,'end')

                messagebox.showinfo('Atualização de dados','Composto adicionado com sucesso.')

        # solta o botão
        self.search_btn.configure(relief='raised')
        return 'break'

