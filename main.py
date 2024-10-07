from tkinter import Tk,END,Entry,N,E,S,W,Button
from tkinter import font
from tkinter import Label
from functools import partial

def get_input(entry,argu):
    entry.insert(END,argu)

def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

