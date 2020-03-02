import tkinter as tk
import query
from PIL import Image, ImageTk
import os
from sql import SQLite


# TODO: ver como pegar a info do text do botao que eu cliquei especificamente e mudar o posicionamento do botao de pesquisar pra ficar no mesmo frame das search bars

CURR_PATH = os.path.dirname(__file__)

ODOURS = [
    "Anis",
    "Azedo",
    "Balnilha",
    "Balsamo",
    "Canfora",
    "Doce",
    "Frutado",
    "Mel",
    "Rosa",
]

sqlite = SQLite(os.path.join(os.path.dirname(os.path.abspath(__file__)), "camd_db.db"))
ODOURS = [""] + sorted(
    list(
        set(
            [
                x[0].split(",")[0]
                for x in sqlite.execute(
                    "SELECT DISTINCT odour FROM molecule_table"
                ).fetchall()
            ]
        )
    )
)


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.compound_info_buttons = []

        self.create_search_bar_frame(self.parent)
        self.submit_button = tk.Button(
            self.parent, text="Pesquisar", command=self.search
        ).pack(anchor="n")
        self.output_frame = tk.Frame(self.parent)
        self.output_frame.pack(side="left", anchor="n", fill="both", expand=True)
        self.create_compound_info_frame(self.output_frame)
        self.create_image_frame(self.output_frame)

    def search(self):
        self.submit()
        self.update_compound_info_frame()

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
        self.compound_info_frame = ScrollFrame(parent)  # add a new scrollable frame.
        self.submit()  # updates the displayed values to be all the items in the database
        self.update_compound_info_frame()  # clears the current buttons and draws new ones based on the query result

        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.compound_info_frame.pack(side="left", anchor="n")

    def create_image_frame(self, parent):
        self.image_frame = tk.Frame(master=parent)
        self.image_panel = tk.Label(master=self.image_frame)
        self.image_panel.pack()
        self.update_image(
            os.path.join(CURR_PATH, "images", f"{self.displayed_values[0][0]}.png")
        )  # when first creating the image frame, show the image of the first compound on the list
        self.image_frame.pack()

    def update_image(self, image_path):
        img = tk.PhotoImage(file=image_path)
        self.image_panel.configure(image=img)
        self.image_panel.image = img

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

    def update_compound_info_frame(self):
        for compound_buttons in self.compound_info_buttons:
            compound_buttons.grid_forget()  # removes the buttons before adding new ones
        self.compound_info_buttons = (
            []
        )  # clears the list of buttons since the buttons have been deleted
        for row in self.displayed_values:
            button = tk.Button(
                self.compound_info_frame.viewPort,
                text=row[3],
                height=5,
                width=20,
                command=lambda: print(row[0]),
            )  # creates a button for each result of the query
            self.compound_info_buttons.append(
                button
            )  # adds them to the list so we know to clean them up later
            button.grid(row=self.displayed_values.index(row))


class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # create a frame (self)

        self.canvas = tk.Canvas(
            self, borderwidth=0, background="#ffffff", width=150
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
