import customtkinter as ctk
import button
from colors import *


class App(ctk.CTk):
    def __init__(self, title: str, size: tuple):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#000")

        # Variables
        self.output_var = ctk.StringVar(value="10000")

        self.output = self.display()
        self.button = self.button_frame()

        self.mainloop()

    def display(self):
        frame = ctk.CTkFrame(master=self, fg_color="transparent")
        frame.place(relx=0, rely=0, relwidth=1, relheight=0.3)

        output = ctk.CTkLabel(master=frame,
                              text_color=output_text,
                              font=output_font,
                              textvariable=self.output_var)
        output.place(relx=0.98, rely=0.8, anchor="se")

        return frame

    def button_frame(self):
        frame = ctk.CTkFrame(master=self, fg_color="transparent")
        frame.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

        # Grid Configuration
        frame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # First Row
        clear_btn = button.Semi_Operator_Btn(frame, "C")
        clear_btn.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)

        pos_minus_btn = button.Semi_Operator_Btn(frame, "±")
        pos_minus_btn.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)

        percent_btn = button.Semi_Operator_Btn(frame, "%")
        percent_btn.grid(row=0, column=2, sticky="nswe", padx=5, pady=5)

        divide_btn = button.Operator_Btn(frame, "÷")
        divide_btn.grid(row=0, column=3, sticky="nswe", padx=5, pady=5)

        # Second Row
        seven_btn = button.Number_Btn(frame, "7")
        seven_btn.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)

        eight_btn = button.Number_Btn(frame, "8")
        eight_btn.grid(row=1, column=1, sticky="nswe", padx=5, pady=5)

        nine_btn = button.Number_Btn(frame, "9")
        nine_btn.grid(row=1, column=2, sticky="nswe", padx=5, pady=5)

        times_btn = button.Operator_Btn(frame, "×")
        times_btn.grid(row=1, column=3, sticky="nswe", padx=5, pady=5)

        # Third Row
        four_btn = button.Number_Btn(frame, "4")
        four_btn.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)

        five_btn = button.Number_Btn(frame, "5")
        five_btn.grid(row=2, column=1, sticky="nswe", padx=5, pady=5)

        six_btn = button.Number_Btn(frame, "6")
        six_btn.grid(row=2, column=2, sticky="nswe", padx=5, pady=5)

        minus_btn = button.Operator_Btn(frame, "-")
        minus_btn.grid(row=2, column=3, sticky="nswe", padx=5, pady=5)

        # Fourth Row
        one_btn = button.Number_Btn(frame, "1")
        one_btn.grid(row=3, column=0, sticky="nswe", padx=5, pady=5)

        two_btn = button.Number_Btn(frame, "2")
        two_btn.grid(row=3, column=1, sticky="nswe", padx=5, pady=5)

        three_btn = button.Number_Btn(frame, "3")
        three_btn.grid(row=3, column=2, sticky="nswe", padx=5, pady=5)

        add_btn = button.Operator_Btn(frame, "+")
        add_btn.grid(row=3, column=3, sticky="nswe", padx=5, pady=5)

        # Fifth Row
        zero_btn = button.Number_Btn(frame, "0")
        zero_btn.grid(row=4, column=0, sticky="nswe", padx=5, pady=5, columnspan=2)

        point_btn = button.Number_Btn(frame, ".")
        point_btn.grid(row=4, column=2, sticky="nswe", padx=5, pady=5)

        equal_btn = button.Operator_Btn(frame, "=")
        equal_btn.grid(row=4, column=3, sticky="nswe", padx=5, pady=5)

        return frame


if __name__ == '__main__':
    # Run the App
    App("iOS Calculator App", (350, 600))
