import tkinter as tk


class AddWarehouse():
    def __init__(self,theWarehouse):
        self.theWarehouse = theWarehouse
        self.WarehouseNameTextBox = ''
        self.WarehouseDescriptionTextBox = ''

    def add_name_of_warehouse(self,window):

        # Warehouse name
        self.theWarehouse.name = self.WarehouseNameTextBox.get("1.0", "end-1c") 
    
        # Warehouse Description
        self.theWarehouse.description = self.WarehouseDescriptionTextBox.get("1.0", "end-1c")
    
    
        window.destroy()
