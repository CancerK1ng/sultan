import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent


        self.data = {
            'Python': 11.27,
            'C': 11.16,
            'Java': 10.46,
            'C++': 7.5,
            'C#': 5.26
        }
        self.languages = self.data.keys()
        self.popularity = self.data.values()

        # create a figure
        self.figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)

        # create the toolbar
        NavigationToolbar2Tk(self.figure_canvas, self)

        # create axes
        self.axes = self.figure.add_subplot()
        self.axes.bar(self.languages, self.popularity)
        self.axes.set_title('График Продаж')
        self.axes.set_ylabel('Popularity')

        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#        self.init_ui()






   # def init_ui(self):
        # self.pack(fill=tk.BOTH, expand=1)
        #
        # acts = ['Scarlett Johansson', 'Rachel Weiss', 'Natalie Portman', 'Jessica Alba']
        #
        # self.lb = tk.Listbox(self)
        # for i in acts:
        #     self.lb.insert(tk.END, i)
        #     self.lb.bind("<<ListboxSelect>>", self.on_select)
        #     self.lb.pack(pady=15)
        # self.button = tk.Button(self, text='Append', command=self.on_click)
        # self.var = tk.StringVar()
        # self.label = tk.Label(self, text=0, textvariable=self.var)
        # self.label.pack()
        #
        # self.pack()
    def on_click(self):
        print('Hello World!')
    def on_select(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)