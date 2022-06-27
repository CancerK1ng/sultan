import tkinter as tk
import tkinter.ttk as ttk
import pan
class Example(tk.Frame):
    def __init__(self, parent, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()


        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

    def init_ui(self):
        self.text = tk.Text(self, width=20, height=10)
        self.text.pack()
        self.text.insert(1.0, 'Hello World!\nFoo\nBar\n\n123\n')

        self.button1 = tk.Button(self, text="Удалить Транзакцию",width = 20, command=self.delete)
        self.button2 = tk.Button(self, text="Добавить Транзакцию", width = 20, command=self.add)
        self.button3 = tk.Button(self, text="Изменить Транзакцию", width = 20, command=self.edit)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def delete(self):
        self.text.insert(tk.END, 'Delete!\n')


    def add(self):
        self.text.insert(tk.END, 'Add!\n')


    def edit(self):
        self.text.insert(tk.END, 'Edit!\n')

table = open("Day_1.xlsx")
df = table.read()