#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import math

class ScientificCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")
        self.master.config(bg="#2F4F4F")  
        
        self.expression = ""  
        self.memory = 0  
        
        self.equation = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        
        self.expression_field = tk.Entry(self.master, textvariable=self.equation, font=("Arial", 18), bd=10, relief="sunken", width=30, borderwidth=5, fg="white", bg="#333333")
        self.expression_field.grid(row=0, column=0, columnspan=5, pady=10)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('log', 4, 4),
            ('sqrt', 5, 0), ('^', 5, 1), ('M+', 5, 2), ('M-', 5, 3), ('MS', 5, 4),
            ('MR', 6, 0), ('(', 6, 1), (')', 6, 2), ('pi', 6, 3), ('e', 6, 4),
            ('C', 7, 0)  # Clear button
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, fg='white', bg='#444444', font=("Arial", 16), command=lambda t=text: self.on_button_click(t), relief="solid", bd=3)
            button.grid(row=row, column=col, sticky="nsew", ipadx=20, ipady=20, padx=5, pady=5)
            
        
        for i in range(8):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)
        
        self.customize_button_colors()

    def customize_button_colors(self):
        # Custom color scheme
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button):
                if widget.cget("text") in ['+', '-', '*', '/', '=', '^', 'log', 'sqrt', 'ln']:
                    widget.config(bg="#8A2BE2", fg="white")  # Operators and scientific
                elif widget.cget("text") in ['M+', 'M-', 'MS', 'MR']:
                    widget.config(bg="#FF6347", fg="white")  # Memory buttons
                elif widget.cget("text") in ['sin', 'cos', 'tan', 'pi', 'e']:
                    widget.config(bg="#1E90FF", fg="white")  # Trigonometric and constants
                elif widget.cget("text") == 'C':
                    widget.config(bg="#FF4500", fg="white")  # Clear button color

    def on_button_click(self, button):
        if button == "=":
            try:
                
                if self.expression.startswith("e^"):
                    # Handling e^x by splitting and using math.exp(x)
                    _, exp = self.expression.split("^")
                    result = math.exp(float(exp))  # e^x using math.exp
                    self.equation.set(str(result))
                    self.expression = str(result)
                # General case for exponentiation
                elif "^" in self.expression:
                    base, exp = self.expression.split("^")
                    result = float(base) ** float(exp)
                    self.equation.set(str(result))
                    self.expression = str(result)
                else:
                    result = str(eval(self.expression))  # Evaluationg- normal cases
                    self.equation.set(result)
                    self.expression = result  # Expression update with result
            except Exception as e:
                self.equation.set("Error")
                self.expression = ""
        elif button == "C":
            self.clear()
        elif button == "sqrt":
            self.calculate_square_root()
        elif button == "log":
            self.expression += "log("
            self.equation.set(self.expression)
        elif button == "ln":
            self.calculate_ln()  #ln is for natural log
        elif button == "sin":
            self.calculate_sine()
        elif button == "cos":
            self.calculate_cosine()
        elif button == "tan":
            self.calculate_tangent()
        elif button == "^":
            self.expression += "^"
            self.equation.set(self.expression)
        elif button == "M+":
            self.memory_add()
        elif button == "M-":
            self.memory_subtract()
        elif button == "MS":
            self.memory_store()
        elif button == "MR":
            self.memory_recall()
        elif button == "pi":
            self.expression += str(math.pi)
            self.equation.set(self.expression)
        elif button == "e":
            self.expression += str(math.e)
            self.equation.set(self.expression)
        elif button == "(":
            self.expression += "("
            self.equation.set(self.expression)
        elif button == ")":
            self.expression += ")"
            self.equation.set(self.expression)
        else:
            self.expression += str(button)  
            self.equation.set(self.expression)

    def calculate_square_root(self):
        try:
            result = math.sqrt(float(self.expression))  
            self.equation.set(str(result))
            self.expression = str(result)
        except ValueError:
            self.equation.set("Error")
            self.expression = ""

    def calculate_ln(self):
        try:
            result = math.log(float(self.expression))  
            self.equation.set(str(result))
            self.expression = str(result)
        except ValueError:
            self.equation.set("Error")
            self.expression = ""

# trigonometric values (in radians).
    def calculate_sine(self):
        try:
            result = math.sin(math.radians(float(self.expression)))  
            self.equation.set(str(result))
            self.expression = str(result)
        except ValueError:
            self.equation.set("Error")
            self.expression = ""

    def calculate_cosine(self):
        try:
            result = math.cos(math.radians(float(self.expression)))  
            self.equation.set(str(result))
            self.expression = str(result)
        except ValueError:
            self.equation.set("Error")
            self.expression = ""

    def calculate_tangent(self):
        try:
            result = math.tan(math.radians(float(self.expression)))  
            self.equation.set(str(result))
            self.expression = str(result)
        except ValueError:
            self.equation.set("Error")
            self.expression = ""

    def memory_add(self):
        try:
            self.memory += float(self.expression)
            self.equation.set(f"Memory: {self.memory}")
        except ValueError:
            self.equation.set("Error")
            self.expression = ""

    def memory_subtract(self):
        try:
            self.memory -= float(self.expression)
            self.equation.set(f"Memory: {self.memory}")
        except ValueError:
            self.equation.set("Error")
            self.expression = ""

    def memory_store(self):
        try:
            self.memory = float(self.expression)
            self.equation.set(f"Memory stored: {self.memory}")
        except ValueError:
            self.equation.set("Error")
            self.expression = ""

    def memory_recall(self):
        self.equation.set(str(self.memory))  # Recall memory
        self.expression = str(self.memory)

    def clear(self):
        """ Clears the current expression """
        self.expression = ""
        self.equation.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculatorApp(root)
    root.mainloop()

