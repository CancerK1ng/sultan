from tkinter import Tk, ttk, filedialog
import tkinter as tk
from tkinter import *
import numpy
import pandas as pd
from tab_b import Example as TabA
from tab_a import Example as TabB


class MainInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Транзакций")
        self.window.geometry("1280x720")
        self.create_widgets()
        self.window.resizable(width=False, height=False)


    def create_widgets(self):
        self.window['padx'] = 10
        self.window['pady'] = 10

        self.notebook = ttk.Notebook(self.window, width=1080, height=720)

        a_tab = TabA(self.notebook)
        b_tab = TabB(self.notebook)

        self.notebook.add(b_tab, text="Транзакций")
        self.notebook.add(a_tab, text="Аналитика")


        self.notebook.grid(row=1, column=1)


if __name__ == '__main__':
    program = MainInterface()
    program.window.mainloop()