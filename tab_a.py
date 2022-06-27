import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import messagebox
from tkinter import *
class Example(tk.Frame):
    def __init__(self, parent, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()




    def init_ui(self):


        self.button2 = tk.Button(self, text="Добавить Транзакцию", width = 20, command=self.D_A_E, background="#555", foreground="#ccc",
             font="8").place(x=5, y=40)
        self.button3 = tk.Button(self, text="Изменить Транзакцию", width = 20, command=self.D_A_E, background="#555", foreground="#ccc",
             font="8").place(x=5, y=80)
        self.button1 = tk.Button(self, text="Удалить Транзакцию",width = 20, command=self.D_A_E, background="#555", foreground="#ccc",
             font="8").place(x=5, y=120)

        # Кнопки принять и сбросить, можно открыть для них отдельную функцию
        self.button4 = tk.Button(self, text="Применить", width=20, command=self.D_A_E, background="#555",foreground="#ccc",
             font="8").place(x=5, y=560)
        self.button5 = tk.Button(self, text="Сбросить", width=20, command=self.D_A_E, background="#555",foreground="#ccc",
             font="8").place(x=5, y=600)

        # Радио кнопки, можно открыть для них отдельную функцию == Фильтр
        self.var = IntVar()
        self.var.set(False)
        self.r1 = tk.Radiobutton(self, text='По номеру транзакций', variable=self.var, command=self.D_A_E, value=0).place(x=5, y=280)
        self.r2 = tk.Radiobutton(self, text='По товарам', variable=self.var, value=1).place(x=5, y=360)
        self.r2 = tk.Radiobutton(self, text='По дате', variable=self.var, value=2).place(x=5, y=440)

        self.message = StringVar()

        self.message_entry = tk.Entry(self,width=20,
                                   font="8", bd='3')
        self.message_entry.place(x=5, y=520)


    # D_A_E == Delete_Add_Edit
    def D_A_E(self):
        self.text.insert(tk.END, 'Delete!\n')

        self.text1.insert(tk.END, 'Add!\n')

        self.text2.insert(tk.END, 'Edit!\n', )



    # def add(self):
    #     self.text.insert(tk.END, 'Add!\n')
    #
    #
    # def edit(self):
    #     self.text.insert(tk.END, 'Edit!\n', )
    #
    # def radio_b(self):
    #     self.var = IntVar()
    #     self.var.set(False)
    #     self.r1 = Radiobutton(text='По номеру транзакций', variable=self.var, value=0).place(x = 5, y = 280)
    #     self.r2 = Radiobutton(text='По товарам',variable=self.var, value=1 ).place(x = 5, y = 360)
    #     self.r2 = Radiobutton(text='По дате', variable=self.var, value=2).place(x=5, y=440)



    # def entry_search(self):
    #
    #     self.message = StringVar()
    #
    #     self.message_entry = Entry(width = 20,
    #          font="8", bd = '3')
    #     self.message_entry.place(x = 5, y = 520)



