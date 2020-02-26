import tkinter as tk
import query
from PIL import Image, ImageTk
import os


ODOURS = ["Anis", "Azedo", "Balnilha", "Balsamo", "Canfora", "Doce", "Frutado", "Mel"]


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.create_search_bar_frame(self.parent)
        self.submit_button = tk.Button(
            self.parent, text="Pesquisar", command=self.submit
        ).pack(anchor="n")
        self.create_compound_info_frame(self.parent)

    def create_search_bar_frame(self, parent):
        self.search_bar_frame = tk.Frame(parent)

        self.smiles_search_bar = self.create_search_bar(
            self.search_bar_frame, row=0, label="Smiles: "
        )
        self.compound_name_search_bar = self.create_search_bar(
            self.search_bar_frame, row=1, label="Nome: "
        )
        self.formula_search_bar = self.create_search_bar(
            self.search_bar_frame, row=2, label="Formula: "
        )
        self.boiling_point_search_bar = self.create_search_bar(
            self.search_bar_frame, row=3, label="Ponto de Ebulicao: "
        )
        self.melting_point_search_bar = self.create_search_bar(
            self.search_bar_frame, row=4, label="Ponto de Fusao: "
        )
        self.flash_point_search_bar = self.create_search_bar(
            self.search_bar_frame, row=5, label="Ponto de Flash: "
        )
        self.solubility_search_bar = self.create_search_bar(
            self.search_bar_frame, row=6, label="Solubilidade: "
        )
        self.vapor_pressure_search_bar = self.create_search_bar(
            self.search_bar_frame, row=7, label="Pressao de Vapor: "
        )
        self.density_search_bar = self.create_search_bar(
            self.search_bar_frame, row=8, label="Densidade: "
        )
        self.vapor_density_search_bar = self.create_search_bar(
            self.search_bar_frame, row=9, label="Densidade de Vapor: "
        )
        self.pka_search_bar = self.create_search_bar(
            self.search_bar_frame, row=10, label="pka: "
        )

        self.odour_dropbox, self.odour_dropbox_value = self.create_dropbox(
            self.search_bar_frame, ODOURS
        )
        self.odour_dropbox.grid(row=4, column=2)

        self.search_bar_frame.pack(anchor="nw")

        parent.bind(
            "<Return>", self.submit
        )  # hitting the enter button has the same function as clicking the 'Pesquisar' button

    def create_search_bar(
        self, parent, row=0, column=0, label="Pesquisar: ", search_bar_width=60
    ):
        tk.Label(parent, text=label).grid(
            row=row, column=column
        )  # nome do campo sempre no canto superior esquerdo
        search_bar = tk.Entry(parent, width=search_bar_width)
        search_bar.grid(
            row=row, column=column + 1
        )  # sempre coloca a barra de pesquisa há uma certa distância do nome baseado no tamanho do nome
        return search_bar

    def create_dropbox(self, parent, options):
        value = tk.StringVar(parent)
        value.set(options[0])

        return tk.OptionMenu(parent, value, *options), value

    def create_compound_info_frame(self, parent):
        self.scrollFrame = ScrollFrame(parent)  # add a new scrollable frame.

        for row in range(15):
            a = row
            tk.Label(
                self.scrollFrame.viewPort,
                text="%s" % row,
                width=3,
                borderwidth="1",
                relief="solid",
            ).grid(row=row, column=0)
            t = "this is the second column for row %s" % row
            tk.Button(
                self.scrollFrame.viewPort,
                text=t,
                command=lambda x=a: self.printMsg("Hello " + str(x)),
            ).grid(row=row, column=1)

        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.pack(side="left", anchor="n", fill="both", expand=True)

    def printMsg(self, msg):
        print(msg)

    def submit(self, event=None):
        self.displayed_values = query.new_get_data(
            smiles=self.smiles_search_bar.get(),
            compound_name=self.compound_name_search_bar.get(),
            formula=self.formula_search_bar.get(),
            boiling_point=self.boiling_point_search_bar.get(),
            melting_point=self.melting_point_search_bar.get(),
            flash_point=self.flash_point_search_bar.get(),
            solubility=self.solubility_search_bar.get(),
            vapor_pressure=self.vapor_pressure_search_bar.get(),
            density=self.density_search_bar.get(),
            vapor_density=self.vapor_density_search_bar.get(),
            pka=self.pka_search_bar.get(),
            odour=self.odour_dropbox_value.get(),
        )
        for row in self.displayed_values:
            print(row[2])


class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # create a frame (self)

        self.canvas = tk.Canvas(
            self, borderwidth=0, background="#ffffff"
        )  # place canvas on self
        self.viewPort = tk.Frame(
            self.canvas, background="#ffffff"
        )  # place a frame on the canvas, this frame will hold the child widgets
        self.vsb = tk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
        )  # place a scrollbar on self
        self.canvas.configure(
            yscrollcommand=self.vsb.set
        )  # attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")  # pack scrollbar to right of self
        self.canvas.pack(
            side="left", fill="both", expand=True
        )  # pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window(
            (4, 4),
            window=self.viewPort,
            anchor="nw",  # add view port frame to canvas
            tags="self.viewPort",
        )

        self.viewPort.bind(
            "<Configure>", self.onFrameConfigure
        )  # bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind(
            "<Configure>", self.onCanvasConfigure
        )  # bind an event whenever the size of the viewPort frame changes.

        self.onFrameConfigure(
            None
        )  # perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

    def onFrameConfigure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )  # whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        """Reset the canvas window to encompass inner frame when required"""
        canvas_width = event.width
        self.canvas.itemconfig(
            self.canvas_window, width=canvas_width
        )  # whenever the size of the canvas changes alter the window region respectively.


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600+300+300")
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
