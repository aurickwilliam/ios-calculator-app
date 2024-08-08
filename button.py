import customtkinter as ctk
from colors import *


class Operator_Btn(ctk.CTkButton):
    def __init__(self, parent, text: str):
        super().__init__(master=parent)

        self.configure(text=text,
                       fg_color=operator_color,
                       text_color=operator_text,
                       font=arial_reg)


class Number_Btn(ctk.CTkButton):
    def __init__(self, parent, text: str):
        super().__init__(master=parent)

        self.configure(text=text,
                       fg_color=num_color,
                       text_color=num_text,
                       font=arial_reg)


class Semi_Operator_Btn(ctk.CTkButton):
    def __init__(self, parent, text: str):
        super().__init__(master=parent)

        self.configure(text=text,
                       fg_color=semi_operator_color,
                       text_color=semi_operator_text,
                       font=arial_reg)
