from tkinter import Tk, ttk
import tkinter as tk

from tab_b import Example as TabA
from tab_a import Example as TabB


class MainInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Транзакций")
        self.window.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        self.window['padx'] = 10
        self.window['pady'] = 10

        self.notebook = ttk.Notebook(self.window, width=500, height=500)

        a_tab = TabA(self.notebook)
        b_tab = TabB(self.notebook)

        self.notebook.add(b_tab, text="Транзакций")
        self.notebook.add(a_tab, text="Аналитика")


        self.notebook.grid(row=1, column=1)


if __name__ == '__main__':
    program = MainInterface()
    program.window.mainloop()