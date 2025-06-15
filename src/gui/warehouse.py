#!/usr/bin/python3
import warehousemodule
import menumodule
import tkinter as tk
from tkinter import ttk


myWarehouse = warehousemodule.Warehouse

class App(tk.Tk):
    def __init__( self, title, size):

        # main setup
        super().__init__()
        self.title( title )
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize( size[0], size[1])


        # add menu
        menu_bar = menumodule.Menu(self, myWarehouse)
        self.config( menu = menu_bar)

        self.mainloop()



App( 'Warehouse Creater', (600,600) )
