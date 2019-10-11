'''

Fonte: https://www.dcc.ufrj.br/~fabiom/mab225/tutorialtkinter.pdf

'''

import tkinter as tk

class Window:
    
    def __init__(self, master):
        
        # Frame do Topo (pesquisa de compostos)
        
        self.search_frame = tk.Frame(highlightbackground='black', highlightcolor='black',
                                     highlightthickness=1)
        
        self.search_frame.pack(side='left', anchor='nw', padx=5, pady=5, fill='x')
        
        
        self.search_frame_title = tk.Label(master=self.search_frame, text='Pesquisa de compostos: ')
        self.search_frame_title.pack(side='top', anchor='nw', padx=5)
        
        self.compound_var = tk.StringVar()
        self.compound_var.set('Oi')
        self.compound_entry = tk.Entry(master=self.search_frame, textvariable=self.compound_var, fg='grey')
        self.compound_entry.pack(side='left', padx=5)
        
        self.search_compound_btn = tk.Button(master=self.search_frame, text='Pesquisar Composto')
        self.search_compound_btn.bind('<Button-1>', self.search_compounds)
        self.search_compound_btn.pack(side='left')
        
        
        
    def search_compounds(self, event):
            
        compound = self.compound_var.get()
        print(compound)
        

root = tk.Tk()
root.geometry('800x600+100+100')
root.title('TCC v0.0')
Window(root)
root.mainloop()
