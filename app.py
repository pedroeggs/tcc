import tkinter as tk
import query
from PIL import Image, ImageTk
import os
from sql import SQLite


# TODO: ver como pegar a info do text do botao que eu cliquei especificamente e mudar o posicionamento do botao de pesquisar pra ficar no mesmo frame das search bars
# TODO: ver pq nao ta carregando os botao e travando o app

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
        self.results_buttons = []

        self.create_search_frame(self.parent)

        self.create_results_frame(self.parent)
        # self.output_frame = tk.Frame(self.parent)
        # self.output_frame.pack(side="left", anchor="n", fill="both", expand=True)
        # self.create_compound_info_frame(self.output_frame)
        self.create_image_frame(self.parent)

    def __del__(self):
        if self.parent:
            self.parent.destroy()

    def search(self):
        self.submit()
        self.update_results_frame()

    def add_compound(self):
        print('mudar essa funcao')

    def create_search_frame(self, parent):
        self.search_frame = tk.Frame(parent)

        self.compound_name_search_bar = self._create_search_bar(
            self.search_frame, x=0.00625, y=0, label="Nome: "
        )
        self.formula_search_bar = self._create_search_bar(
            self.search_frame, x=0.38125, y=0, label="Formula: "
        )
        tk.Label(self.search_frame, text='Aroma: ').place(relx=0.75875, rely=0)
        self.odour_dropbox, self.odour_dropbox_value = self.create_dropbox(
            self.search_frame, ODOURS
        )
        self.odour_dropbox.place(relx=0.75875, rely=0.07)

        self.smiles_search_bar = self._create_search_bar(
            self.search_frame, x=0.00625, y=0.2, label="SMILES: "
        )
        self.boiling_point_search_bar = self._create_search_bar(
            self.search_frame, x=0.38125, y=0.2, label="Ponto de Ebulição: "
        )
        self.melting_point_search_bar = self._create_search_bar(
            self.search_frame, x=0.75625, y=0.2, label="Ponto de Fusão: "
        )
        self.flash_point_search_bar = self._create_search_bar(
            self.search_frame, x=0.00625, y=0.4, label="Ponto de Flash: "
        )
        self.solubility_search_bar = self._create_search_bar(
            self.search_frame, x=0.38125, y=0.4, label="Solubilidade: "
        )
        self.vapor_pressure_search_bar = self._create_search_bar(
            self.search_frame, x=0.75625, y=0.4, label="Pressão de Vapor: "
        )
        self.density_search_bar = self._create_search_bar(
            self.search_frame, x=0.00625, y=0.6, label="Densidade: "
        )
        self.vapor_density_search_bar = self._create_search_bar(
            self.search_frame, x=0.38125, y=0.6, label="Densidade de Vapor: "
        )
        self.pka_search_bar = self._create_search_bar(
            self.search_frame, x=0.75625, y=0.6, label="pKa: "
        )

        self.submit_button = tk.Button(
            self.search_frame, text="Pesquisar", command=self.search
        )
        self.submit_button.place(relx=0.48375, rely=0.85, height=28, relwidth = 0.275)

        self.add_button = tk.Button(master=self.search_frame, text='Adicionar',
                                 command=self.add_compound)
        self.add_button.place(relx=0.100875, rely=0.85, height=28, relwidth = 0.275)

        self.search_frame.place(x=0, y=0, relwidth=1, relheight=0.5)

        parent.bind(
            "<Return>", self.submit
        )  # hitting the enter button has the same function as clicking the 'Pesquisar' button

    # def create_search_bar(
    #     self, parent, row=0, column=0, label="Pesquisar: ", search_bar_width=60
    # ):
    #     tk.Label(parent, text=label).grid(
    #         row=row, column=column
    #     )  # nome do campo sempre no canto superior esquerdo
    #     search_bar = tk.Entry(parent, width=search_bar_width)
    #     search_bar.grid(
    #         row=row, column=column + 1
    #     )  # sempre coloca a barra de pesquisa há uma certa distância do nome baseado no tamanho do nome
    #     return search_bar

    def _create_search_bar(self, parent, x, y, label, relwidth=0.1, height=28):
        label = tk.Label(parent, text=label)
        label.place(relx=x, rely=y)

        search_bar = tk.Entry(parent, fg='black')
        search_bar.place(relx=x+0.002, rely=y+0.07, relwidth=relwidth, height=height)

        return search_bar

    def create_dropbox(self, parent, options):
        value = tk.StringVar(parent)
        value.set(options[0])

        return tk.OptionMenu(parent, value, *options), value

    #def create_compound_info_frame(self, parent):
    #    self.results_frame = ScrollFrame(parent)  # add a new scrollable frame.
    #    self.submit()  # updates the displayed values to be all the items in the database
    #    self.update_compound_info_frame()  # clears the current buttons and draws new ones based on the query result
#
    #    # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
    #    self.results_frame.pack(side="left", anchor="n")

    def create_results_frame(self, parent):
        self.results_frame = ScrollFrame(parent)
        self.submit()
        self.update_results_frame()

        self.results_frame.place(relx=0,rely=0.5,relheight=0.5,relwidth=0.3)

    def create_image_frame(self, parent):
        self.image_frame = tk.Frame(master=parent)
        self.image_panel = tk.Label(master=self.image_frame)
        self.image_panel.pack(anchor='n')
        self.update_image(
            os.path.join(CURR_PATH, "images", f"{self.displayed_values[0][0]}.png")
        )  # when first creating the image frame, show the image of the first compound on the list
        self.image_frame.place(relx=0.305,rely=0.5,relheight=0.5,relwidth=0.7)

    def update_image(self, image_path):
        img = tk.PhotoImage(file=image_path)
        self.image_panel.configure(image=img)
        self.image_panel.image = img

    def submit(self, event=None):
        self.displayed_values = query.get_data(
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

    def update_results_frame(self):
        for compound_buttons in self.results_buttons:
            compound_buttons.grid_forget()  # removes the buttons before adding new ones
        self.results_buttons = (
            []
        )  # clears the list of buttons since the buttons have been deleted
        for row in self.displayed_values:
            result = tk.Label(
                self.results_frame.viewPort,
                text=f'{row[3]}\n{row[1]}',
                cursor='hand2',
                height=5,
                width=20,
            )  # creates a button for each result of the query
            self.results_buttons.append(
                result
            )  # adds them to the list so we know to clean them up later
            result.grid(row=self.displayed_values.index(row))
            result.bind('<Button-1>', lambda x: self.update_image(CURR_PATH + f'/images/{row[0]}.png'))


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
    root.minsize(800, 600)
    root.mainloop()
