'''

Fonte: https://www.dcc.ufrj.br/~fabiom/mab225/tutorialtkinter.pdf

'''

import tkinter as tk
import query 
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from tkinter import scrolledtext

CURR_PATH = os.path.dirname(os.path.abspath(__file__))

class Window:
    
    def __init__(self, master):

        # Frame do Topo (pesquisa de compostos)
        
        self.search_frame = tk.Frame(master=master, highlightbackground='black', highlightcolor='black',
                                     highlightthickness=1)
        
        self.search_frame.place(x=0, y=0, relwidth=1, relheight=0.5)
        #self.search_frame.pack(side='top', anchor='nw', padx=5, pady=5, fill='x')
        
        # Adicionar nome
        
        self.search_frame_title = tk.Label(master=self.search_frame, text='Nome: ')
        self.search_frame_title.place(relx=0.00625,y=0.00625)
        
        self.compound_var = tk.StringVar()
        self.compound_entry = tk.Entry(master=self.search_frame, textvariable=self.compound_var, fg='black')
        self.compound_entry.place(relx=0.00875,rely=0.07, relwidth=0.1, height=28) 
        
        # Adicionar fórmula
        
        self.formula_search_frame_title = tk.Label(master=self.search_frame, text='Fórmula: ')
        self.formula_search_frame_title.place(relx=0.38125,rely=0.00625)
        
        self.formula_var = tk.StringVar()
        self.formula_entry = tk.Entry(master=self.search_frame, textvariable=self.formula_var, fg='black')
        self.formula_entry.place(relx=0.38375,rely=0.07, relwidth=0.1, height=28)
        
        # Adicionar aroma
        
        self.odour_search_frame_title = tk.Label(master=self.search_frame, text='Aroma: ')
        self.odour_search_frame_title.place(relx=0.75625,rely=0.00625)
        
        self.odour_var = tk.StringVar()
        self.odour_entry = tk.Entry(master=self.search_frame, textvariable=self.odour_var, fg='black')
        self.odour_entry.place(relx=0.75875,rely=0.07, relwidth=0.1, height=28)

        # Adicionar SMILES
        
        self.smiles_search_frame_title = tk.Label(master=self.search_frame, text='SMILES: ')
        self.smiles_search_frame_title.place(relx=0.00625,rely=0.2)
        
        self.smiles_var = tk.StringVar()
        self.smiles_entry = tk.Entry(master=self.search_frame, textvariable=self.smiles_var, fg='black')
        self.smiles_entry.place(relx=0.00875,rely=0.27, relwidth=0.1, height=28)

        # Adicionar Ponto de Ebulição
        
        self.BP_search_frame_title = tk.Label(master=self.search_frame, text='Ponto de Ebulição: ')
        self.BP_search_frame_title.place(relx=0.38125,rely=0.2)
        
        self.BP_var = tk.StringVar()
        self.BP_entry = tk.Entry(master=self.search_frame, textvariable=self.BP_var, fg='black')
        self.BP_entry.place(relx=0.38375,rely=0.27, relwidth=0.1, height=28)

        # Adicionar Ponto de Fusão
        
        self.MP_search_frame_title = tk.Label(master=self.search_frame, text='Ponto de Fusão: ')
        self.MP_search_frame_title.place(relx=0.75625,rely=0.2)
        
        self.MP_var = tk.StringVar()
        self.MP_entry = tk.Entry(master=self.search_frame, textvariable=self.MP_var, fg='black')
        self.MP_entry.place(relx=0.75875,rely=0.27, relwidth=0.1, height=28)

        # Adicionar Ponto de Flash
        
        self.FP_search_frame_title = tk.Label(master=self.search_frame, text='Ponto de Flash: ')
        self.FP_search_frame_title.place(relx=0.00625,rely=0.4)
        
        self.FP_var = tk.StringVar()
        self.FP_entry = tk.Entry(master=self.search_frame, textvariable=self.FP_var, fg='black')
        self.FP_entry.place(relx=0.00875,rely=0.47, relwidth=0.1, height=28)

        # Adicionar Solubilidade
        
        self.solubility_search_frame_title = tk.Label(master=self.search_frame, text='Solubilidade: ')
        self.solubility_search_frame_title.place(relx=0.38125,rely=0.4)
        
        self.solubility_var = tk.StringVar()
        self.solubility_entry = tk.Entry(master=self.search_frame, textvariable=self.solubility_var, fg='black')
        self.solubility_entry.place(relx=0.38375,rely=0.47, relwidth=0.1, height=28)

        # Adicionar Pressão de Vapor
        
        self.VP_search_frame_title = tk.Label(master=self.search_frame, text='Pressão de Vapor: ')
        self.VP_search_frame_title.place(relx=0.75625,rely=0.4)
        
        self.VP_var = tk.StringVar()
        self.VP_entry = tk.Entry(master=self.search_frame, textvariable=self.VP_var, fg='black')
        self.VP_entry.place(relx=0.75875,rely=0.47, relwidth=0.1, height=28)

        # Adicionar Densidade
        
        self.density_search_frame_title = tk.Label(master=self.search_frame, text='Densidade: ')
        self.density_search_frame_title.place(relx=0.00625,rely=0.6)
        
        self.density_var = tk.StringVar()
        self.density_entry = tk.Entry(master=self.search_frame, textvariable=self.density_var, fg='black')
        self.density_entry.place(relx=0.00875,rely=0.67, relwidth=0.1, height=28)

        # Adicionar Densidade de Vapor
        
        self.vapor_density_search_frame_title = tk.Label(master=self.search_frame, text='Densidade de Vapor: ')
        self.vapor_density_search_frame_title.place(relx=0.38125,rely=0.6)
        
        self.vapor_density_var = tk.StringVar()
        self.vapor_density_entry = tk.Entry(master=self.search_frame, textvariable=self.vapor_density_var, fg='black')
        self.vapor_density_entry.place(relx=0.38375,rely=0.67, relwidth=0.1, height=28)

        # Adicionar pKa
        
        self.pka_search_frame_title = tk.Label(master=self.search_frame, text='pKa: ')
        self.pka_search_frame_title.place(relx=0.75625,rely=0.6)
        
        self.pka_var = tk.StringVar()
        self.pka_entry = tk.Entry(master=self.search_frame, textvariable=self.pka_var, fg='black')
        self.pka_entry.place(relx=0.75875,rely=0.67, relwidth=0.1, height=28)

        # Botão de Adição

        self.add_btn = tk.Button(master=self.search_frame, text='Adicionar composto ao banco de dados',
                                            command=lambda: self.add_compound())
        self.add_btn.place(relx=0.100875, rely=0.85, height=28, relwidth = 0.275)

        # Botão de pesquisa 

        self.search_btn = tk.Button(master=self.search_frame, text='Pesquisar compostos no banco de dados',
                                              command=lambda: self.search_compounds())
        self.search_btn.place(relx=0.48375, rely=0.85, height=28, relwidth = 0.275)
    
        # Frames inferiores (de output)
        # Esquerda
        
        self.output_frame_left_var_entry = tk.StringVar()
        
        self.output_frame_left = tk.Frame(highlightbackground='black', highlightcolor='black',
                                          highlightthickness=1, bg='white')
        
        
        self.output_frame_left.place(relx=0,rely=0.5,relheight=0.81,relwidth=0.5)
        
        self.output_frame_left_text = tk.scrolledtext.ScrolledText(master=self.output_frame_left, bg='white', wrap=tk.WORD)
        self.output_frame_left_text.place(relx=0,rely=0,relheight=0.62,relwidth=1)

        # Meio
        self.output_frame_mid = tk.Frame(highlightbackground='black', highlightcolor='black',
                                     highlightthickness=1, bg='white')
        
        
        self.output_frame_mid.place(relx=0.505,rely=0.5,relheight=0.81,relwidth=0.5)
        
        self.output_frame_mid_text = tk.Label(master=self.output_frame_mid, text='', bg='white', image='')
        self.output_frame_mid_text.place(relx=0,rely=0,relheight=1,relwidth=1)

    def search_compounds(self):
        
        self.output_frame_left_text.delete('1.0', tk.END)


        # 'aperta' o botão
        self.search_btn.configure(relief='sunken')
    
        results = query.new_get_data(smiles=self.smiles_var.get(),
                                    compound_name=self.compound_var.get(),
                                    formula=self.formula_var.get(),
                                    boiling_point=self.BP_var.get(),
                                    melting_point=self.MP_var.get(),
                                    flash_point=self.FP_var.get(),
                                    solubility=self.solubility_var.get(),
                                    vapor_pressure=self.VP_var.get(),
                                    density=self.density_var.get(),
                                    vapor_density=self.vapor_density_var.get(),
                                    pka=self.pka_var.get(),
                                    odour=self.odour_var.get())

        self.search_btn.configure(relief='raised')

        str_out = ''

        if len(results) == 0:

            str_out += 'Nenhum composto com os parâmetros pesquisado encontrado.'
            self.output_frame_left_text.insert(tk.END, str_out)

        else:

            for r in results:
                
                str_out += 'SMILES: '+ r[0] + '\n\nAroma: ' + r[1] + '\n\nNome do composto: ' + r[2]
                str_out += '\n\nFórmula: ' + r[3] + '\n\nPonto de Ebulição: ' + r[4]
                str_out += '\n\nPonto de Fusão: ' + r[5] + '\n\nPonto de Flash: ' + r[6]
                str_out += '\n\nSolubilidade: ' + r[7] + '\n\nPressão de Vapor' + r[8] + '\n\nDensidade: ' + r[9]
                str_out += '\n\nDensidade de Vapor: ' + r[10] + '\n\npKa: ' + r[11] + '\n--------------------\n\n'

                image_path = os.path.join(CURR_PATH, 'images', r[0] + '.png')
                
                if os.path.exists(image_path): 
                    image = Image.open(image_path)
                    photo = ImageTk.PhotoImage(image)

                    # mais de uma foto
                    # self.output_frame_mid_text.image_create(tk.END, image = photo)
                    # self.output_frame_mid_text.insert(tk.END, '\n')
                    
                    # uma foto
                    self.output_frame_mid_text['image'] = photo
                    self.output_frame_mid_text.image = photo
                
                self.output_frame_left_text.insert(tk.END, str_out)                
        
        return 'break'

    def add_compound(self):
        
        # lista dos parâmetros (em tuple) dados pelo usuário
        # o erro acontece aqui, deveria preencher tudo mas fica tudo como string vazia
        # rodando esse arquivo sozinho, preenche ok
        add_parameters = [(self.smiles_var.get(), self.odour_var.get(), 
                        self.compound_var.get(), self.formula_var.get(), 
                        self.BP_var.get(), self.MP_var.get(), self.FP_var.get(), 
                        self.solubility_var.get(), self.VP_var.get(), 
                        self.density_var.get(), self.vapor_density_var.get(),
                        self.pka_var.get())]

        # 'aperta' o botão
        self.search_btn.configure(relief='sunken')

        # checa se o usuário colocou nome e fórmula
        if add_parameters[0][2] == '':    

            messagebox.showinfo('Erro','O composto deve ter um nome. Por favor, verifique.')
            
        else:

            param_found = False

            # checa se o usuário colocou pelo menos um parâmetro
            for i in range(len(add_parameters[0])):

                if i != 0 and add_parameters[0][i] != '':
                    param_found = True
                    break

            if not param_found:    

                messagebox.showinfo('Erro','O composto deve ter um nome e pelo menos uma propriedade. Por favor, verifique.')
            
            else:
            
                # adiciona os dados ao banco de dados
                query.update_db(add_parameters)

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

def search_help():

    messagebox.showinfo('Ajuda de Pesquisa','''O programa realiza pesquisas com qualquer forma de preenchimento das entradas. Como exemplos:\n
a) Para pesquisar compostos com 8 carbonos que têm aroma Doce, digite "C8" no campo "Fórmula" e "Doce" no campo "Aroma".\n
b) Para pesquisar todos os compostos, simplesmente pressione o botão de pesquisa sem preencher qualquer campo.''')

def add_help():

    messagebox.showinfo('Ajuda de Atualização','Para adicionar um novo composto ao banco de dados, é necessário preencher o campo "Nome" e pelo menos um outro campo disponível.')

def about():

    messagebox.showinfo('Sobre','''TKAroma v1.0 (07/03/2020)\n\nO programa TKAroma foi criado por Arthur Adabo de Camargo e Pedro Alvares Eggers como projeto de conclusão do curso de Engenharia Química da Escola Politécnica da Universidade de São Paulo.\n
O programa TKAroma foi escrito em Python, sendo utilizada a biblioteca TKinter para a interface gráfica, e em SQLite3 para o banco de dados. Sua finalidade é fornecer facilmente propriedades sobre compostos cujos aromas possam ser interessantes para a indústria de cosméticos, bem como permitir a pesquisa de tais aromas.''')


root = tk.Tk()
menubar = tk.Menu(root)

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ajuda", menu=help_menu)
help_menu.add_command(label="Pesquisa", command = search_help)
help_menu.add_command(label="Atualização de Banco de Dados", command = add_help)
help_menu.add_command(label="Sobre", command = about)

root.geometry('800x600+100+100')
root.title('TKAroma')
root.config(menu=menubar)
root.minsize(800, 600)
Window(root)
root.mainloop()             
