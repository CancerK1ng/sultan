import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame
from tkinter import ttk
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
        self.data1 = {'Country': ['US', 'CA', 'GER', 'UK', 'FR'],
                 'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]
                 }
        self.df1 = DataFrame(self.data1, columns=['Country', 'GDP_Per_Capita'])
        style = ttk.Style()
        style.theme_use('clam')
        #
        self.data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
                 'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
                 }
        self.df2 = DataFrame(self.data2, columns=['Year', 'Unemployment_Rate'])

        self.data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
                 'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
                 }
        self.df3 = DataFrame(self.data3, columns=['Interest_Rate', 'Stock_Index_Price'])

        self.figure1 = plt.Figure(figsize=(3, 2), dpi=70)
        self.ax1 = self.figure1.add_subplot(111)
        self.bar1 = FigureCanvasTkAgg(self.figure1, self)
        self.bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        self.df1 = self.df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()
        self.df1.plot(kind='bar', legend=True, ax=self.ax1)
        self.ax1.set_title('Country Vs. GDP Per Capita')

        self.figure2 = plt.Figure(figsize=(3, 2), dpi=70)
        self.ax2 = self.figure2.add_subplot(111)
        self.line2 = FigureCanvasTkAgg(self.figure2, self)
        self.line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, )
        self.df2 = self.df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()
        self.df2.plot(kind='line', legend=True, ax=self.ax2, color='r', marker='o', fontsize=10)
        self.ax2.set_title('Year Vs. Unemployment Rate')

        self.figure3 = plt.Figure(figsize=(3, 2), dpi=70)
        self.ax3 = self.figure3.add_subplot(111)
        self.ax3.scatter(self.df3['Interest_Rate'], self.df3['Stock_Index_Price'], color='g')
        self.scatter3 = FigureCanvasTkAgg(self.figure3, self)
        self.scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        self.ax3.legend(['Stock_Index_Price'])
        self.ax3.set_xlabel('Interest Rate')
        self.ax3.set_title('Interest Rate Vs. Stock Index Price')




