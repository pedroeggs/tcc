# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:53:31 2019

@author: Arthur
"""

import tkinter as tk

root = tk.Tk()

topframe = tk.Frame(master=root)
topframe.pack()
bottomframe = tk.Frame(master=root)
bottomframe.pack(side='bottom')

root.mainloop()
