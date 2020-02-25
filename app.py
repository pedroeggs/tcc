import tkinter as tk
import query
from PIL import Image, ImageTk
import os


ODOURS = ["Anis", "Azedo", "Balsamo", "Doce"]


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.create_search_bar_frame(self.parent)
        self.create_compound_info_frame(self.parent)

    def create_search_bar_frame(self, parent):
        self.search_bar_frame = tk.Frame(parent)
        self.create_search_bar(self.search_bar_frame)
        self.create_odour_dropbox(self.search_bar_frame)
        self.search_bar_frame.pack(anchor="nw")

    def create_search_bar(self, parent, label="Pesquisar: ", search_bar_width=60):
        tk.Label(parent, text=label).pack(
            side="left"
        )  # nome do campo sempre no canto superior esquerdo
        self.search_bar = tk.Entry(parent, width=search_bar_width)
        self.search_bar.pack(
            side="left"
        )  # sempre coloca a barra de pesquisa há uma certa distância do nome baseado no tamanho do nome

    def create_odour_dropbox(self, parent):
        self.odour_value = tk.StringVar(parent)
        self.odour_value.set(ODOURS[0])

        self.odour_dropbox = tk.OptionMenu(parent, self.odour_value, *ODOURS)
        self.odour_dropbox.pack(side="left")

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
