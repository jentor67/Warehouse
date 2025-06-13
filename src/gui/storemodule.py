import tkinter as tk


class AddWarehouse():
    self.WarehouseNameTextBox = ''
    self.WarehouseDescriptionTextBox = ''

    def add_name_of_warehouse( window):
        global myWarehouse

        # Warehouse name
        myWarehouse.name = self.WarehouseNameTextBox.get("1.0", "end-1c") 
    
        # Warehouse Description
        myWarehouse.description = self.WarehouseDescriptionTextBox.get("1.0", "end-1c")
    
    
        window.destroy()
