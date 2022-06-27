import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
import pandas as pd
class Example(tk.Frame):
    def __init__(self, parent, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        self.parent = parent

        self.init_ui()




    def init_ui(self):

        # Кнопки добавить, изменить, удалить
        self.button2 = tk.Button(self, text="Добавить Транзакцию", width = 20, command=self.add, background="#555", foreground="#ccc",
             font="8").place(x=5, y=40)
        self.button3 = tk.Button(self, text="Изменить Транзакцию", width=20, command=self.edit, background="#555",foreground="#ccc",
             font="8").place(x=5, y=80)
        self.button1 = tk.Button(self, text="Удалить Транзакцию",width = 20, command=self.delete, background="#555", foreground="#ccc",
             font="8").place(x=5, y=120)

        # Кнопки принять и сбросить
        self.button4 = tk.Button(self, text="Применить", width=20, command=self.apply, background="#555",foreground="#ccc",
             font="8").place(x=5, y=560)
        self.button5 = tk.Button(self, text="Сбросить", width=20, command=self.reset, background="#555",foreground="#ccc",
             font="8").place(x=5, y=600)

        # Радио кнопки по фильтру
        self.var = IntVar()
        self.var.set(False)
        self.r1 = tk.Radiobutton(self, text='По номеру транзакций', variable=self.var, value=0).place(x=5, y=280)
        self.r2 = tk.Radiobutton(self, text='По товарам', variable=self.var, value=1).place(x=5, y=360)
        self.r2 = tk.Radiobutton(self, text='По дате', variable=self.var, value=2).place(x=5, y=440)

        self.message = StringVar()

        self.message_entry = tk.Entry(self,width=20,
                                   font="8", bd='3')
        self.message_entry.place(x=5, y=520)


    # D_A_E == Delete_Add_Edit


    # def open_file(self):
    #     self.filename = filedialog.askopenfilename(title="Open a File", filetype=(("xlxs files", ".*xlsx"),
    #                                                                          ("All Files", "*.")))
    #
    #     if self.filename:
    #         try:
    #             self.filename = r"{}".format(self.filename)
    #             self.df = pd.read_excel(self.filename)
    #         except ValueError:
    #             self.label.config(text="File could not be opened")
    #         except FileNotFoundError:
    #             self.label.config(text="File Not Found")
    #
    #     self.tree["column"] = list(self.df.columns)
    #     self.tree["show"] = "headings"
    #     for col in self.tree["column"]:
    #         self.tree.heading(col, text=col)
    #
    #     # Put Data in Rows
    #     self.df_rows = self.df.to_numpy().tolist()
    #     for row in self.df_rows:
    #         self.tree.insert("", "end", values=row)
    #
    #     self.tree.pack()


    def clear_treeview(self):
        self.tree.delete(*self.tree.get_children())



    def add(self):
        self.text.insert(tk.END, 'Add!\n')

    def edit(self):
        self.text.insert(tk.END, 'Edit!\n', )

    def delete(self):
        self.text.insert(tk.END, 'Delete!\n')

    def apply(self):
        self.text.insert(tk.END, 'Apply!\n')

    def reset(self):
        self.text.insert(tk.END, 'Reset!\n')

    def radio_b(self):
        self.var = IntVar()
        self.var.set(False)
        self.r1 = Radiobutton(text='По номеру транзакций', variable=self.var, value=0).place(x = 5, y = 280)
        self.r2 = Radiobutton(text='По товарам',variable=self.var, value=1 ).place(x = 5, y = 360)
        self.r2 = Radiobutton(text='По дате', variable=self.var, value=2).place(x=5, y=440)



    def entry_search(self):

        self.message = StringVar()

        self.message_entry = Entry(width = 20,
             font="8", bd = '3')
        self.message_entry.place(x = 5, y = 520)


