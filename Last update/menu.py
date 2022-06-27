from tkinter import Tk, ttk, filedialog
import tkinter as tk
from tab_b1 import Example as TabA
from tab_a import Example as TabB
from tkinter import *
import pandas as pd

from tab_c import Example as TabC


class MainInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Транзакций")
        self.window.geometry("700x700")
        self.create_widgets()
        self.window.resizable(width=False, height=False)
        self.m = Menu(self.window)
        self.window.config(menu=self.m)
        self.file_menu = Menu(self.m, tearoff=False)
        self.m.add_cascade(label="Меню", menu=self.file_menu)
        self.label = Label(self.window, text='')
        # self.label.pack(pady=20)
        self.file_menu.add_command(label="Open File", command=self.open_file)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.frame = Frame(self.window)
        # self.frame.pack(pady=20)
        self.tree = ttk.Treeview(self.frame)
        self.clear_treeview()





    def create_widgets(self):
        self.window['padx'] = 10
        self.window['pady'] = 10

        self.notebook = ttk.Notebook(self.window, width=700, height=650)

        a_tab = TabA(self.notebook)
        b_tab = TabB(self.notebook)

        self.notebook.add(b_tab, text="Транзакций")
        self.notebook.add(a_tab, text="Аналитика")
        self.notebook.grid(row=1, column=1)

    # def create_menu(self):
    #     self.m = m = Menu(self.window)
    #     self.window.config(menu=m)
    #
    #     file_menu = Menu(m, tearoff=False)
    #     m.add_cascade(label="Menu", menu=file_menu)
    #     file_menu.add_command(label="Open File", command=self.open_file)
    #
    # def open_file(self):
    #     self.filename = filedialog.askopenfilename(title="Open a File", filetype=(("xlxs files", ".*xlsx"),
    #                                                                              ("All Files", "*.")))







    def open_file(self):
        self.filename = filedialog.askopenfilename(title="Open a File", filetype=(("xlxs files", ".*xlsx"),
                                                                             ("All Files", "*.")))

        if self.filename:
            try:
                self.filename = r"{}".format(self.filename)
                self.df = pd.read_excel(self.filename)
            except ValueError:
                self.label.config(text="File could not be opened")
            except FileNotFoundError:
                self.label.config(text="File Not Found")

        self.tree["column"] = list(self.df.columns)
        self.tree["show"] = "headings"
        for col in self.tree["column"]:
            self.tree.heading(col, text=col)

        # Put Data in Rows
        self.df_rows = self.df.to_numpy().tolist()
        for row in self.df_rows:
            self.tree.insert("", "end", values=row)

        self.tree.pack()


    def clear_treeview(self):
        self.tree.delete(*self.tree.get_children())

    # Create a Treeview widget




if __name__ == '__main__':
    program = MainInterface()
    program.window.mainloop()