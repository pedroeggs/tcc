'''

Fonte: https://www.dcc.ufrj.br/~fabiom/mab225/tutorialtkinter.pdf

'''

import tkinter as tk
from tkinter import messagebox
import time

class Window:
    
    def __init__(self, master):
        
        # Frame do Topo (pesquisa de compostos)
        
        self.search_frame = tk.Frame(master=master, highlightbackground='black', highlightcolor='black',
                                     highlightthickness=1)
        
        self.search_frame.place(x=0, y=0, relwidth=1, relheight=0.2)
        #self.search_frame.pack(side='top', anchor='nw', padx=5, pady=5, fill='x')
        
        
        self.search_frame_title = tk.Label(master=self.search_frame, text='Pesquisa de compostos: ')
        self.search_frame_title.place(x=5,y=5)
        
        self.compound_var_entry = tk.StringVar()
        self.compound_var_entry.set('Oi')
        self.compound_entry = tk.Entry(master=self.search_frame, textvariable=self.compound_var_entry, fg='grey')
        self.compound_entry.place(x=7,y=27, relwidth=0.1, height=28)

        self.search_compound_btn = tk.Button(master=self.search_frame, text='Pesquisar')
        self.search_compound_btn.bind('<Button-1>', self.search_compounds)
        self.search_compound_btn.place(x=90, y=27, height=28)        
    
        # Frames inferiores (de output)
        
        self.output_frame_one = tk.Frame(highlightbackground='black', highlightcolor='black',
                                     highlightthickness=1, bg='white')
        
        
        self.output_frame_one.place(relx=0,rely=0.2,relheight=0.8,relwidth=0.33)
        
        self.output_frame_two = tk.Frame(highlightbackground='black', highlightcolor='black',
                                     highlightthickness=1, bg='cyan')
        
        
        self.output_frame_two.place(relx=0.335,rely=0.2,relheight=0.8,relwidth=0.33)
        
        self.output_frame_three = tk.Frame(highlightbackground='black', highlightcolor='black',
                                     highlightthickness=1, bg='green')
        
        
        self.output_frame_three.place(relx=0.67,rely=0.2,relheight=0.8,relwidth=0.33)
        
        
    def search_compounds(self, event):
        
        self.search_compound_btn.configure(relief='sunken')
        
        compound = self.compound_var_entry.get()
        messagebox.showinfo('Composto selecionado','Voce selecionou o composto ' + compound)
        self.search_compound_btn.configure(relief='raised')
        
        return 'break'
    
root = tk.Tk()
root.geometry('800x600+100+100')
root.title('TCC v0.0')
Window(root)
root.mainloop()
