import menumodule
import storemodule
import tkinter as tk


class NewWarehouse(tk.Toplevel):
    def __init__(self, parent, theWarehouse):
        super().__init__(parent)
        
        #  create object
        aw = storemodule.AddWarehouse(theWarehouse)
        
        new_window = self #tk.Toplevel(self)
        new_window.title("New Warehouse")
        new_window.geometry('400x300')
       

        # add menu
        menu_bar = menumodule.NewWareHouse(self)
        self.config( menu = menu_bar)

    
        # Add widgets to the new window
        labelWarehouseName = tk.Label(new_window, text="Warehouse name")
        labelWarehouseName.pack(padx=20, pady=20)
   
        # create text box of warehouse name
        aw.WarehouseNameTextBox = tk.Text(new_window, height=1, width=30)
        aw.WarehouseNameTextBox.pack()
   
        labelWarehouseDescription = tk.Label(
                new_window, 
                text="Warehouse Description")
        labelWarehouseDescription.pack(padx=20, pady=20)
   
        # create text box of warehouse name
        aw.WarehouseDescriptionTextBox = tk.Text(
                new_window, 
                height=1, 
                width=30)
        aw.WarehouseDescriptionTextBox.pack()
   
        # create button to update name
        button = tk.Button(
                new_window, 
                text="Click Me", 
                command = lambda:aw.add_name_of_warehouse( new_window ) )
        
        button.pack()

        


