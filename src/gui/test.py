#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class Pump():
    # member variable
    # account_holder
    # balance_amount

    # constructor
    def __init__(self,ah,bal):
        self.account_holder = ah
        self.balance_amount = bal

    def getPumps(self):
        print("The details of your account are:"+self.account_holder + " " + str(self.balance_amount))

# object = class(*passing values to constructor*)

p = Pump("Tahir",12000)

p.getPumps()
