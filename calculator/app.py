# calculator/app.py
import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")

        self.entry = tk.Entry(self, width=20, font=('Arial', 24), bd=5, relief='ridge', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 1, 4)  
        ]


        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            rowspan = btn[3] if len(btn) > 3 else 1
            colspan = btn[4] if len(btn) > 4 else 1

            b = tk.Button(self, text=text, width=5, height=2, font=('Arial', 20),
                        command=lambda t=text: self.on_click(t))
            b.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew")

    def on_click(self, char):
        if char == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, char)
