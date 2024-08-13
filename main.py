import customtkinter as ctk
from colors import *
from button import *


class App(ctk.CTk):
    def __init__(self, title: str, size: tuple):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#000")

        # Variables
        self.output_var = ctk.StringVar(value="0")
        self.output_operation = ctk.StringVar()

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
        clear_btn = Semi_Operator_Btn(frame, "C")
        clear_btn.configure(command=self.clear_display)
        clear_btn.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)

        pos_minus_btn = Semi_Operator_Btn(frame, "±")
        pos_minus_btn.configure(command=self.invert_sign)
        pos_minus_btn.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)

        percent_btn = Semi_Operator_Btn(frame, "%")
        percent_btn.configure(command=self.percent_display)
        percent_btn.grid(row=0, column=2, sticky="nswe", padx=5, pady=5)

        divide_btn = Operator_Btn(frame, "÷")
        divide_btn.configure(command=lambda: self.operation("/", divide_btn))
        divide_btn.grid(row=0, column=3, sticky="nswe", padx=5, pady=5)

        # Second Row
        seven_btn = Number_Btn(frame, "7")
        seven_btn.configure(command=lambda: self.concat_display("7"))
        seven_btn.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)

        eight_btn = Number_Btn(frame, "8")
        eight_btn.configure(command=lambda: self.concat_display("8"))
        eight_btn.grid(row=1, column=1, sticky="nswe", padx=5, pady=5)

        nine_btn = Number_Btn(frame, "9")
        nine_btn.configure(command=lambda: self.concat_display("9"))
        nine_btn.grid(row=1, column=2, sticky="nswe", padx=5, pady=5)

        times_btn = Operator_Btn(frame, "×")
        times_btn.configure(command=lambda: self.operation("*", times_btn))
        times_btn.grid(row=1, column=3, sticky="nswe", padx=5, pady=5)

        # Third Row
        four_btn = Number_Btn(frame, "4")
        four_btn.configure(command=lambda: self.concat_display("4"))
        four_btn.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)

        five_btn = Number_Btn(frame, "5")
        five_btn.configure(command=lambda: self.concat_display("5"))
        five_btn.grid(row=2, column=1, sticky="nswe", padx=5, pady=5)

        six_btn = Number_Btn(frame, "6")
        six_btn.configure(command=lambda: self.concat_display("6"))
        six_btn.grid(row=2, column=2, sticky="nswe", padx=5, pady=5)

        minus_btn = Operator_Btn(frame, "-")
        minus_btn.configure(command=lambda: self.operation("-", minus_btn))
        minus_btn.grid(row=2, column=3, sticky="nswe", padx=5, pady=5)

        # Fourth Row
        one_btn = Number_Btn(frame, "1")
        one_btn.configure(command=lambda: self.concat_display("1"))
        one_btn.grid(row=3, column=0, sticky="nswe", padx=5, pady=5)

        two_btn = Number_Btn(frame, "2")
        two_btn.configure(command=lambda: self.concat_display("2"))
        two_btn.grid(row=3, column=1, sticky="nswe", padx=5, pady=5)

        three_btn = Number_Btn(frame, "3")
        three_btn.configure(command=lambda: self.concat_display("3"))
        three_btn.grid(row=3, column=2, sticky="nswe", padx=5, pady=5)

        add_btn = Operator_Btn(frame, "+")
        add_btn.configure(command=lambda: self.operation("+", add_btn))
        add_btn.grid(row=3, column=3, sticky="nswe", padx=5, pady=5)

        # Fifth Row
        zero_btn = Number_Btn(frame, "0")
        zero_btn.configure(command=lambda: self.concat_display("0"))
        zero_btn.grid(row=4, column=0, sticky="nswe", padx=5, pady=5, columnspan=2)

        point_btn = Number_Btn(frame, ".")
        point_btn.configure(command=lambda: self.concat_display("."))
        point_btn.grid(row=4, column=2, sticky="nswe", padx=5, pady=5)

        equal_btn = Operator_Btn(frame, "=")
        equal_btn.grid(row=4, column=3, sticky="nswe", padx=5, pady=5)

        return frame

    def concat_display(self, digit: str):
        current_digit = self.output_var.get()

        if digit == "." and "." in current_digit:
            self.output_var.set(current_digit)
        elif digit == "." and current_digit == "0":
            self.output_var.set("0.")
        elif current_digit == "0":
            self.output_var.set(digit)
        else:
            self.output_var.set(current_digit + digit)

    def clear_display(self):
        self.output_var.set("0")

    def invert_sign(self):
        if "." in self.output_var.get():
            value = float(self.output_var.get())
        else:
            value = int(self.output_var.get())

        if value == 0:
            new_value = str(0)
        elif value > 0:
            new_value = str(-abs(value))
        else:
            new_value = str(abs(value))

        self.output_var.set(new_value)

    def percent_display(self):
        value = self.output_var.get()

        if value == "0":
            self.output_var.set(str(float(value)))
            return

        # if "." in value:
        #     index = value.index(".") - 2
        #     print(index)

    def operation(self, sign: str, button):
        self.output_operation.set(sign)

        button.configure(fg_color=operator_active_color, hover=False)


if __name__ == '__main__':
    # Run the App
    App("iOS Calculator App", (350, 600))
