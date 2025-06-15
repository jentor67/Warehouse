import tkinter as tk


class AddWarehouse():
    def __init__(self):
        self.WarehouseNameTextBox = ''
        self.WarehouseDescriptionTextBox = ''

    #def add_name_of_warehouse(self, window):
    #def add_name_of_warehouse(self):
    def add_name_of_warehouse(self,window):
        global myWarehouse

        # Warehouse name
        myWarehouse.name = self.WarehouseNameTextBox.get("1.0", "end-1c") 
        #dummy1 = self.WarehouseNameTextBox.get("1.0", "end-1c")  # not defined
        #dummy1 = WarehouseNameTextBox.get("1.0", "end-1c") # not defined
    
        # Warehouse Description
        #myWarehouse.description = self.WarehouseDescriptionTextBox.get("1.0", "end-1c")
    
    
        window.destroy()
