'''

Fonte: https://www.dcc.ufrj.br/~fabiom/mab225/tutorialtkinter.pdf

'''

import tkinter as tk
import query 
from PIL import Image, ImageTk
import os

CURR_PATH = os.path.dirname(os.path.abspath(__file__))

class Window:
    
    def __init__(self, master):
        
        # Frame do Topo (pesquisa de compostos)
        
        self.search_frame = tk.Frame(master=master, highlightbackground='black', highlightcolor='black',
                                     highlightthickness=1)
        
        self.search_frame.place(x=0, y=0, relwidth=1, relheight=0.2)
        #self.search_frame.pack(side='top', anchor='nw', padx=5, pady=5, fill='x')
        
        # Pesquisa por nome
        
        self.search_frame_title = tk.Label(master=self.search_frame, text='Pesquisa por nome do composto: ')
        self.search_frame_title.place(x=5,y=5)
        
        self.compound_var_entry = tk.StringVar()
        self.compound_var_entry.set('Pesquisar')
        self.compound_entry = tk.Entry(master=self.search_frame, textvariable=self.compound_var_entry, fg='grey')
        self.compound_entry.place(x=7,y=27, relwidth=0.1, height=28)

        self.search_compound_btn = tk.Button(master=self.search_frame, text='Pesquisar',
                                             command=lambda: self.search_compounds('compound_name'))
        self.search_compound_btn.place(x=90, y=27, height=28) 
        
        # Pesquisa por fórmula
        
        self.formula_search_frame_title = tk.Label(master=self.search_frame, text='Pesquisa por fórmula: ')
        self.formula_search_frame_title.place(x=305,y=5)
        
        self.formula_var_entry = tk.StringVar()
        self.formula_var_entry.set('Pesquisar')
        self.formula_entry = tk.Entry(master=self.search_frame, textvariable=self.formula_var_entry, fg='grey')
        self.formula_entry.place(x=307,y=27, relwidth=0.1, height=28)

        self.search_formula_btn = tk.Button(master=self.search_frame, text='Pesquisar',
                                              command=lambda: self.search_compounds('formula'))
        self.search_formula_btn.place(x=390, y=27, height=28)
        
        # pesquisa por aroma
        
        self.odour_search_frame_title = tk.Label(master=self.search_frame, text='Pesquisa por aroma: ')
        self.odour_search_frame_title.place(x=605,y=5)
        
        self.odour_var_entry = tk.StringVar()
        self.odour_var_entry.set('Pesquisar')
        self.odour_entry = tk.Entry(master=self.search_frame, textvariable=self.odour_var_entry, fg='grey')
        self.odour_entry.place(x=607,y=27, relwidth=0.1, height=28)

        self.search_odour_btn = tk.Button(master=self.search_frame, text='Pesquisar',
                                              command=lambda: self.search_compounds('odour'))
        self.search_odour_btn.place(x=690, y=27, height=28)
    
        # Frames inferiores (de output)
        # Esquerda
        
        self.output_frame_left_var_entry = tk.StringVar()
        self.output_frame_left_var_entry.set('Pesquisar')
        
        self.output_frame_left = tk.Frame(highlightbackground='black', highlightcolor='black',
                                          highlightthickness=1, bg='white')
        
        
        self.output_frame_left.place(relx=0,rely=0.2,relheight=0.81,relwidth=0.5)
        
        self.output_frame_left_text = tk.Text(master=self.output_frame_left, bg='white')
        self.output_frame_left_text.place(relx=0,rely=0,relheight=1,relwidth=1)
        
        # Scroll da esquerda
        
        self.scrollbar_left = tk.Scrollbar(master=self.output_frame_left_text)
        self.scrollbar_left.pack(side='right', fill='y')
        self.scrollbar_left.config(command=self.output_frame_left_text.yview)
        
        # Meio
        self.output_frame_mid = tk.Frame(highlightbackground='black', highlightcolor='black',
                                     highlightthickness=1, bg='white')
        
        
        self.output_frame_mid.place(relx=0.505,rely=0.2,relheight=0.81,relwidth=0.5)
        
        self.output_frame_mid_text = tk.Label(master=self.output_frame_mid, text='', bg='white', image='')
        self.output_frame_mid_text.place(relx=0,rely=0,relheight=1,relwidth=1)
        
        
        
    def search_compounds(self, column_filter):
        
        self.output_frame_left_text.delete('1.0', tk.END)
        # 'aperta' o botão
        if column_filter == 'compound_name':

            self.search_compound_btn.configure(relief='sunken')
            
            search_parameter = self.compound_var_entry.get()
            results = query.get_data(column_filter, search_parameter)
            # 'solta' o botao
            self.search_compound_btn.configure(relief='raised')
            
        elif column_filter == 'formula':
            
            self.search_formula_btn.configure(relief='sunken')
            
            search_parameter = self.formula_var_entry.get()
            results = query.get_data(column_filter, search_parameter)
            # 'solta' o botao
            self.search_formula_btn.configure(relief='raised')
            
        elif column_filter == 'odour':
            
            self.search_odour_btn.configure(relief='sunken')
            
            search_parameter = self.odour_var_entry.get()
            results = query.get_data(column_filter, search_parameter)
            # 'solta' o botao
            self.search_odour_btn.configure(relief='raised')
        
        str_out = ''
        for r in results:
            
            str_out += 'SMILES: '+ r[0] + '\nAroma: ' + r[1] + '\nNome do composto: ' + r[2]
            str_out += '\n\nFórmula: ' + r[3] + '\n\nPonto de Ebulição: ' + r[4]
            str_out += '\n\nPonto de Fusão: ' + r[5] + '\n\nPonto de Flash: ' + r[6]
            str_out += '\n\nSolubilidade: ' + r[7] + '\n\nPressão de Vapor' + r[8] + '\n\nDensidade: ' + r[9]
            str_out += '\n\nDensidade de Vapor: ' + r[10] + '\n\npKa: ' + r[11] + '\n--------------------\n\n'
            image = Image.open(os.path.join(CURR_PATH, 'images', r[0] + '.png'))
            photo = ImageTk.PhotoImage(image)
            
            # descomentar para ter fotos no frame da esquerda. Tá bugado pra mais de uma foto
            # self.output_frame_left_text.image_create(tk.END, image = photo)
            # self.output_frame_left_text.insert(tk.END, '\n')
            self.output_frame_left_text.insert(tk.END, str_out)
            
            self.output_frame_mid_text['image'] = photo
            self.output_frame_mid_text.image = photo

    
        if str_out == '':
            str_out = 'Nenhum composto foi encontrado!'
        
        
        return 'break'
    
root = tk.Tk()
root.geometry('800x600+100+100')
root.title('TCC v0.0')
Window(root)
root.mainloop()             
