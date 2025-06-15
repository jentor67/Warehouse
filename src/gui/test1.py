#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class Pump():

    # constructor
    def __init__(self):
        self.account_holder = ''
        self.balance_amount = 0

    def getPumps(self):
        print("The details of your account are:"+self.account_holder + " " + str(self.balance_amount))

# object = class(*passing values to constructor*)

p = Pump()
p.account_holder = "John"
p.balance_amount = 120000
p.getPumps()
