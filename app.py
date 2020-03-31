import tkinter as tk
import query
from PIL import Image, ImageTk
import os
from tkinter import messagebox


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

ODOURS = query.get_odours()


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.results_buttons = []

        self.create_search_frame(self.parent)

        self.create_results_frame(self.parent)

        self.create_image_frame(self.parent)

        self.create_popup_menu(self.parent)

    def search(self):
        self.submit()
        self.update_results_frame()

    def add_compound(self):
        result = tk.messagebox.askokcancel(
            message="Do you want to add the compound's information?"
        )
        if result:
            add_compound_info = [
                (
                    self.smiles_search_bar.get(),
                    self.odour_dropbox_value.get(),
                    self.compound_name_search_bar.get(),
                    self.formula_search_bar.get(),
                    self.boiling_point_search_bar.get(),
                    self.melting_point_search_bar.get(),
                    self.flash_point_search_bar.get(),
                    self.solubility_search_bar.get(),
                    self.vapor_pressure_search_bar.get(),
                    self.density_search_bar.get(),
                    self.vapor_density_search_bar.get(),
                    self.pka_search_bar.get(),
                )
            ]
            # button goes down
            self.add_button.configure(relief="sunken")

            # checa se o usuário colocou nome e alguma outra propriedade
            if add_compound_info[0][2] == "" or True not in [
                x != ""
                for x in add_compound_info[0]
                if add_compound_info[0].index(x) != 2
            ]:
                messagebox.showerror(
                    message="O composto deve ter um nome e pelo menos outra propriedade. Por favor, verifique."
                )
            else:
                query.update_db(add_compound_info)

                # clears the entry search bars
                self.compound_name_search_bar.delete(0, "end")
                self.smiles_search_bar.delete(0, "end")
                self.formula_search_bar.delete(0, "end")
                self.boiling_point_search_bar.delete(0, "end")
                self.melting_point_search_bar.delete(0, "end")
                self.flash_point_search_bar.delete(0, "end")
                self.solubility_search_bar.delete(0, "end")
                self.vapor_pressure_search_bar.delete(0, "end")
                self.density_search_bar.delete(0, "end")
                self.vapor_density_search_bar.delete(0, "end")
                self.pka_search_bar.delete(0, "end")
                self.odour_dropbox_value.set(ODOURS[0])

                messagebox.showinfo(
                    "Atualização de dados", "Composto adicionado com sucesso."
                )

            # button comes up again
            self.add_button.configure(relief="raised")
            return "break"

    def create_search_frame(self, parent):
        self.search_frame = tk.Frame(parent)

        self.compound_name_search_bar = self._create_search_bar(
            self.search_frame, x=0.00625, y=0, label="Nome: "
        )
        self.formula_search_bar = self._create_search_bar(
            self.search_frame, x=0.38125, y=0, label="Formula: "
        )
        tk.Label(self.search_frame, text="Aroma: ").place(relx=0.75875, rely=0)
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
        self.submit_button.place(relx=0.48375, rely=0.85, height=28, relwidth=0.275)

        self.add_button = tk.Button(
            master=self.search_frame, text="Adicionar", command=self.add_compound
        )
        self.add_button.place(relx=0.100875, rely=0.85, height=28, relwidth=0.275)

        self.search_frame.place(x=0, y=0, relwidth=1, relheight=0.5)

        parent.bind(
            "<Return>", self.submit
        )  # hitting the enter button has the same function as clicking the 'Pesquisar' button

    def _create_search_bar(self, parent, x, y, label, relwidth=0.1, height=28):
        label = tk.Label(parent, text=label)
        label.place(relx=x, rely=y)

        search_bar = tk.Entry(parent, fg="black")
        search_bar.place(
            relx=x + 0.002, rely=y + 0.07, relwidth=relwidth, height=height
        )

        return search_bar

    def create_dropbox(self, parent, options):
        value = tk.StringVar(parent)
        value.set(options[0])

        return tk.OptionMenu(parent, value, *options), value

    def create_results_frame(self, parent):
        self.results_frame = ScrollFrame(parent)
        self.results_frame.bind("<Enter>", self._frame_entered)
        self.results_frame.bind("<Leave>", self._frame_left)
        self.submit()
        self.update_results_frame()

        self.results_frame.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.425)

    def create_image_frame(self, parent):
        self.image_frame = ScrollFrame(parent)
        self.image_frame.bind("<Enter>", self._frame_entered)
        self.image_frame.bind("<Leave>", self._frame_left)
        self.image_panel = tk.Label(master=self.image_frame.viewPort)
        self.image_panel.pack()

        tk.Label(self.image_frame.viewPort, text="Name: ").pack()
        self.result_name = tk.Label(self.image_frame.viewPort, text="")
        self.result_name.pack()

        tk.Label(self.image_frame.viewPort, text="SMILES: ").pack()
        self.result_smiles = tk.Label(self.image_frame.viewPort, text="")
        self.result_smiles.pack()

        tk.Label(self.image_frame.viewPort, text="Formula: ").pack()
        self.result_formula = tk.Label(self.image_frame.viewPort, text="")
        self.result_formula.pack()

        tk.Label(self.image_frame.viewPort, text="Odour: ").pack()
        self.result_odour = tk.Label(self.image_frame.viewPort, text="")
        self.result_odour.pack()

        tk.Label(self.image_frame.viewPort, text="Boiling Point: ").pack()
        self.result_boiling_point = tk.Label(self.image_frame.viewPort, text="")
        self.result_boiling_point.pack()

        tk.Label(self.image_frame.viewPort, text="Melting Point: ").pack()
        self.result_melting_point = tk.Label(self.image_frame.viewPort, text="")
        self.result_melting_point.pack()

        tk.Label(self.image_frame.viewPort, text="Flash Point: ").pack()
        self.result_flash_point = tk.Label(self.image_frame.viewPort, text="")
        self.result_flash_point.pack()

        tk.Label(self.image_frame.viewPort, text="Solubility: ").pack()
        self.result_solubility = tk.Label(self.image_frame.viewPort, text="")
        self.result_solubility.pack()

        tk.Label(self.image_frame.viewPort, text="Vapor Pressure: ").pack()
        self.result_vapor_pressure = tk.Label(self.image_frame.viewPort, text="")
        self.result_vapor_pressure.pack()

        tk.Label(self.image_frame.viewPort, text="Density: ").pack()
        self.result_density = tk.Label(self.image_frame.viewPort, text="")
        self.result_density.pack()

        tk.Label(self.image_frame.viewPort, text="Vapor Density: ").pack()
        self.result_vapor_density = tk.Label(self.image_frame.viewPort, text="")
        self.result_vapor_density.pack()

        tk.Label(self.image_frame.viewPort, text="pKa: ").pack()
        self.result_pka = tk.Label(self.image_frame.viewPort, text="")
        self.result_pka.pack()

        self.update_image_frame(
            self.displayed_values[0]
        )  # when first creating the image frame, show the image of the first compound on the list

        self.image_frame.place(relx=0.43, rely=0.5, relheight=0.5, relwidth=0.57)

    def create_popup_menu(self, parent):
        self.popup_menu = tk.Menu(parent, tearoff=0)
        self.popup_menu.add_command(
            label="Delete", command=self.delete_compound
        )  # adds the delete option to the menu which calls delete_compound by clicking it

    def update_image_frame(self, compound_info):

        if os.path.isfile(os.path.join(CURR_PATH, "images", compound_info[0]) + ".png"):

            img = tk.PhotoImage(
                file=f'{os.path.join(CURR_PATH, "images", compound_info[0])}.png'
            )

        else:

            img = tk.PhotoImage(
                file=f'{os.path.join(CURR_PATH, "images", "notfound")}.png'
            )

        self.image_panel.configure(image=img)
        self.image_panel.image = img
        self.result_smiles.configure(text=compound_info[0])
        self.result_odour.configure(text=compound_info[1])
        self.result_name.configure(text=compound_info[2])
        self.result_formula.configure(text=compound_info[3])
        self.result_boiling_point.configure(text=compound_info[4])
        self.result_melting_point.configure(text=compound_info[5])
        self.result_flash_point.configure(text=compound_info[6])
        self.result_solubility.configure(text=compound_info[7])
        self.result_vapor_pressure.configure(text=compound_info[8])
        self.result_density.configure(text=compound_info[9])
        self.result_vapor_density.configure(text=compound_info[10])
        self.result_pka.configure(text=compound_info[11])

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

    def delete_compound(self):
        if self.deleted_compound:
            deleted = query.delete_compound(
                self.deleted_compound[2]
            )  # deletes compound from the database, returns True if deleted successfully
            if deleted:
                tk.messagebox.showinfo(
                    "Deletion!", f"Deleted {self.deleted_compound[2]} SUCCESSFULLY"
                )
                self.submit()
                self.update_results_frame()  # submit and update_results_frame are called to reset the results display
            else:
                tk.messagebox.showerror(
                    "Deletion!",
                    f"Something went wrong when trying to delete {self.deleted_compound[2]}. Deletion FAILED",
                )
        else:
            tk.messagebox.showerror(
                "Deletion!",
                "Could not locate the compound on the database, try refreshing the compound list by clicking 'Pesquisar' again.",
            )  # in a case where deleted_compound was not set, the compound problably doesnt exist anymore

    def _handle_result_button_click(self, event):
        self.update_image_frame(event.widget.info)

    def update_results_frame(self):
        for compound_buttons in self.results_buttons:
            compound_buttons.grid_forget()  # removes the buttons before adding new ones
        self.results_buttons = (
            []
        )  # clears the list of buttons since the buttons have been deleted
        for row in self.displayed_values:
            result = tk.Label(
                self.results_frame.viewPort,
                text=f"{row[3]}\n{row[2]}",
                cursor="hand2",
                height=5,
                width=45,
            )  # creates a button for each result of the query

            result.info = row
            result.grid(row=self.displayed_values.index(row), sticky="nsew")
            self.results_frame.viewPort.grid_columnconfigure(
                0, weight=1
            )  # makes the labels fill the scrollable frame if the main window is resized
            result.bind(
                "<Button-1>", lambda x: self._handle_result_button_click(x),
            )
            result.bind(
                "<Button-3>", lambda x: self._handle_result_button_right_click(x)
            )  # binds the right button to the _handle_result_button_right_click
            self.results_buttons.append(
                result
            )  # adds them to the list so we know to clean them up later

    # once the mouse is inside the frame bound to this command, binds the canvas portion of the frame to a handle scroll function using the mouse wheel
    def _frame_entered(self, event):
        event.widget.canvas.bind_all(
            "<MouseWheel>", lambda x: self._handle_scroll(x, event.widget.canvas)
        )  # passes the canvas to the _handle_scroll function because the scroll event can happen over any widget inside the frame entered, but only the canvas can actually yview_scroll

    # once the mouse leaves the frame bound to this command, using the mouse whell wont do anything
    def _frame_left(self, event):
        event.widget.canvas.unbind_all("<MouseWheel>")

    # scrolls a canvas yview
    def _handle_scroll(self, event, canvas):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _handle_result_button_right_click(self, event):
        self.deleted_compound = event.widget.info
        self.popup_menu.post(
            event.x_root, event.y_root
        )  # opens the popup menu with the delete option where the mouse clicked with the right button


class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # create a frame (self)

        self.canvas = tk.Canvas(
            self, borderwidth=0, background="#F0F0F0", width=150
        )  # place canvas on self
        self.viewPort = tk.Frame(
            self.canvas, background="#F0F0F0"
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


def search_help():
    tk.messagebox.showinfo(
        "Ajuda de Pesquisa",
        """O programa realiza pesquisas com qualquer forma de preenchimento das entradas. Como exemplos:\n
a) Para pesquisar compostos com 8 carbonos que têm aroma Doce, digite "C8" no campo "Fórmula" e "Doce" no campo "Aroma".\n
b) Para pesquisar todos os compostos, simplesmente pressione o botão de pesquisa sem preencher qualquer campo.""",
    )


def add_help():
    tk.messagebox.showinfo(
        "Ajuda de Atualização",
        'Para adicionar um novo composto ao banco de dados, é necessário preencher o campo "Nome" e pelo menos um outro campo disponível.',
    )


def about():
    tk.messagebox.showinfo(
        "Sobre",
        """TKAroma v1.0 (07/03/2020)\n\nO programa TKAroma foi criado por Arthur Adabo de Camargo e Pedro Alvares Eggers como projeto de conclusão do curso de Engenharia Química da Escola Politécnica da Universidade de São Paulo.\n
O programa TKAroma foi escrito em Python, sendo utilizada a biblioteca TKinter para a interface gráfica, e em SQLite3 para o banco de dados. Sua finalidade é fornecer facilmente propriedades sobre compostos cujos aromas possam ser interessantes para a indústria de cosméticos, bem como permitir a pesquisa de tais aromas.""",
    )


if __name__ == "__main__":
    root = tk.Tk()
    menubar = tk.Menu(root)

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Ajuda", menu=help_menu)
    help_menu.add_command(label="Pesquisa", command=search_help)
    help_menu.add_command(label="Atualização de Banco de Dados", command=add_help)
    help_menu.add_command(label="Sobre", command=about)
    root.config(menu=menubar)
    root.geometry("800x600+300+300")
    App(root, background="#F0F0F0").pack(side="top", fill="both", expand=True)
    root.minsize(800, 600)
    root.mainloop()
