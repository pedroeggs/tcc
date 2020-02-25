'''

Fonte: https://www.dcc.ufrj.br/~fabiom/mab225/tutorialtkinter.pdf

'''

import tkinter as tk
import query
import os

CURR_PATH = os.path.dirname(os.path.abspath(__file__))

class Window:
    
    def __init__(self, master):
        
        # Frame do Topo (pesquisa de compostos)
        
        self.add_frame = tk.Frame(master=master, highlightbackground='black', highlightcolor='black',
                                     highlightthickness=1)
        
        self.add_frame.place(x=0, y=0, relwidth=1, relheight=1)
        #self.add_frame.pack(side='top', anchor='nw', padx=5, pady=5, fill='x')
        
        # Adicionar nome
        
        self.add_frame_title = tk.Label(master=self.add_frame, text='Nome: ')
        self.add_frame_title.place(x=5,y=5)
        
        self.compound_var_entry = tk.StringVar()
        self.compound_entry = tk.Entry(master=self.add_frame, textvariable=self.compound_var_entry, fg='grey')
        self.compound_entry.place(x=7,y=27, relwidth=0.1, height=28) 
        
        # Adicionar fórmula
        
        self.formula_add_frame_title = tk.Label(master=self.add_frame, text='Fórmula: ')
        self.formula_add_frame_title.place(x=305,y=5)
        
        self.formula_var_entry = tk.StringVar()
        self.formula_entry = tk.Entry(master=self.add_frame, textvariable=self.formula_var_entry, fg='grey')
        self.formula_entry.place(x=307,y=27, relwidth=0.1, height=28)
        
        # Adicionar aroma
        
        self.odour_add_frame_title = tk.Label(master=self.add_frame, text='Aroma: ')
        self.odour_add_frame_title.place(x=605,y=5)
        
        self.odour_var_entry = tk.StringVar()
        self.odour_entry = tk.Entry(master=self.add_frame, textvariable=self.odour_var_entry, fg='grey')
        self.odour_entry.place(x=607,y=27, relwidth=0.1, height=28)

        # Adicionar SMILES
        
        self.smiles_add_frame_title = tk.Label(master=self.add_frame, text='SMILES: ')
        self.smiles_add_frame_title.place(x=5,y=85)
        
        self.smiles_var_entry = tk.StringVar()
        self.smiles_entry = tk.Entry(master=self.add_frame, textvariable=self.smiles_var_entry, fg='grey')
        self.smiles_entry.place(x=7,y=107, relwidth=0.1, height=28)

        # Adicionar Ponto de Ebulição
        
        self.BP_add_frame_title = tk.Label(master=self.add_frame, text='Ponto de Ebulição: ')
        self.BP_add_frame_title.place(x=305,y=85)
        
        self.BP_var_entry = tk.StringVar()
        self.BP_entry = tk.Entry(master=self.add_frame, textvariable=self.BP_var_entry, fg='grey')
        self.BP_entry.place(x=307,y=107, relwidth=0.1, height=28)

        # Adicionar Ponto de Fusão
        
        self.MP_add_frame_title = tk.Label(master=self.add_frame, text='Ponto de Fusão: ')
        self.MP_add_frame_title.place(x=605,y=85)
        
        self.MP_var_entry = tk.StringVar()
        self.MP_entry = tk.Entry(master=self.add_frame, textvariable=self.MP_var_entry, fg='grey')
        self.MP_entry.place(x=607,y=107, relwidth=0.1, height=28)

        # Adicionar Ponto de Flash
        
        self.FP_add_frame_title = tk.Label(master=self.add_frame, text='Ponto de Flash: ')
        self.FP_add_frame_title.place(x=5,y=165)
        
        self.FP_var_entry = tk.StringVar()
        self.FP_entry = tk.Entry(master=self.add_frame, textvariable=self.FP_var_entry, fg='grey')
        self.FP_entry.place(x=7,y=187, relwidth=0.1, height=28)

        # Adicionar Solubilidade
        
        self.solubility_add_frame_title = tk.Label(master=self.add_frame, text='Solubilidade: ')
        self.solubility_add_frame_title.place(x=305,y=165)
        
        self.solubility_var_entry = tk.StringVar()
        self.solubility_entry = tk.Entry(master=self.add_frame, textvariable=self.solubility_var_entry, fg='grey')
        self.solubility_entry.place(x=307,y=187, relwidth=0.1, height=28)

        #c.executemany("""
        #INSERT INTO molecule_table (smiles, odour, compound_name, formula, boiling_point, melting_point, 
        #flash_point, solubility, vapor_pressure, density, vapor_density, pka)
        #VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        #""", values_list)


        self.search_btn = tk.Button(master=self.add_frame, text='Pesquisar',
                                              command=lambda: self.search_compounds())
        self.search_btn.place(x=690, y=27, height=28)
           
    def search_compounds(self):
        
        self.output_frame_left_text.delete('1.0', tk.END)
        
        search_parameters = [self.compound_var_entry.get(), self.formula_var_entry.get(),
                             self.odour_var_entry.get()]

        # 'aperta' o botão
        self.search_btn.configure(relief='sunken')
    
        results = query.get_data(search_parameters)
        self.search_btn.configure(relief='raised')

        str_out = ''

        if len(results) == 0:

            str_out += 'Nenhum composto com os parâmetros pesquisado encontrado.'
            self.output_frame_left_text.insert(tk.END, str_out)

        else:

            for r in results:
                
                print(r)
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
        
        return 'break'
    
root = tk.Tk()
root.geometry('800x600+100+100')
root.title('TCC v0.0')
Window(root)
root.mainloop()  