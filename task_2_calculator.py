import tkinter as tk
import math

root = tk.Tk()
root.title('Scientific Calculator')
root.configure(bg='#0000FF')
root.resizable(width=False, height=False)

ent_field = tk.Entry(
    root, bg='#ADD8E6', fg='#000080',
    font=('Arial', 25), borderwidth=10,
    justify="right"
)
ent_field.grid(row=0, columnspan=10, padx=10, pady=10, sticky='nsew')
ent_field.insert(0, '0')

FONT = ('Arial', 10, 'bold')


class SC_Calculator:
    def __init__(self):   # FIXED
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str + val)
            self.inp_value = False
        except:
            self.Entry('Error')

    def Clear_Entry(self):
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

    def SQ_Root(self):
        try:
            self.current = math.sqrt(float(ent_field.get()))
            self.Entry(self.current)
        except:
            self.Entry('Error')

    def Pi(self):
        self.Entry(math.pi)

    def E(self):
        self.Entry(math.e)

    def Deg(self):
        try:
            self.Entry(math.degrees(float(ent_field.get())))
        except:
            self.Entry('Error')

    def Rad(self):
        try:
            self.Entry(math.radians(float(ent_field.get())))
        except:
            self.Entry('Error')

    def Exp(self):
        try:
            self.Entry(math.exp(float(ent_field.get())))
        except:
            self.Entry('Error')

    def Fact(self):
        try:
            self.Entry(math.factorial(int(float(ent_field.get()))))
        except:
            self.Entry('Error')

    def Sin(self):
        try:
            self.Entry(math.sin(math.radians(float(ent_field.get()))))
        except:
            self.Entry('Error')

    def Cos(self):
        try:
            self.Entry(math.cos(math.radians(float(ent_field.get()))))
        except:
            self.Entry('Error')

    def Tan(self):
        try:
            self.Entry(math.tan(math.radians(float(ent_field.get()))))
        except:
            self.Entry('Error')

    def Sinh(self):
        try:
            self.Entry(math.sinh(math.radians(float(ent_field.get()))))
        except:
            self.Entry('Error')

    def Cosh(self):
        try:
            self.Entry(math.cosh(math.radians(float(ent_field.get()))))
        except:
            self.Entry('Error')

    def Tanh(self):
        try:
            self.Entry(math.tanh(math.radians(float(ent_field.get()))))
        except:
            self.Entry('Error')

    def Ln(self):
        try:
            self.Entry(math.log(float(ent_field.get())))
        except:
            self.Entry('Error')

    def Log_10(self):
        try:
            self.Entry(math.log10(float(ent_field.get())))
        except:
            self.Entry('Error')

    def Log_2(self):
        try:
            self.Entry(math.log2(float(ent_field.get())))
        except:
            self.Entry('Error')

    def Pow_2(self):
        try:
            self.Entry(float(ent_field.get()) ** 2)
        except:
            self.Entry('Error')

    def Pow_3(self):
        try:
            self.Entry(float(ent_field.get()) ** 3)
        except:
            self.Entry('Error')

    def Pow_10_n(self):
        try:
            self.Entry(10 ** int(float(ent_field.get())))
        except:
            self.Entry('Error')

    def One_div_x(self):
        try:
            self.Entry(1 / float(ent_field.get()))
        except:
            self.Entry('Error')

    def Abs(self):
        try:
            self.Entry(abs(float(ent_field.get())))
        except:
            self.Entry('Error')


# Create Calculator object
sc_app = SC_Calculator()


# --- NUMBER PAD ---
numberpad = "789456123"
i = 0
button = []
for j in range(2, 5):
    for k in range(3):
        btn = tk.Button(
            root, text=numberpad[i], font=FONT, fg="red",
            width=6, height=2, highlightbackground='#ADD8E6',
            highlightthickness=2,
            command=lambda x=numberpad[i]: sc_app.Enter_Num(x)
        )
        btn.grid(row=j, column=k, padx=10, pady=10, sticky='nsew')
        button.append(btn)
        i += 1


# --- SPECIAL BUTTONS ---
tk.Button(root, text='CE', command=sc_app.Clear_Entry, font=FONT).grid(row=1, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='√', command=sc_app.SQ_Root, font=FONT).grid(row=1, column=2, sticky='nsew', padx=10, pady=10)

tk.Button(root, text='0', command=lambda: sc_app.Enter_Num('0'), font=FONT).grid(row=5, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='.', command=lambda: sc_app.Standard_Ops('.'), font=FONT).grid(row=5, column=2, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='=', command=lambda: sc_app.Standard_Ops('='), font=FONT).grid(row=5, column=3, sticky='nsew', padx=10, pady=10)

# Operators
ops = ['+', '-', '*', '/']
for idx, op in enumerate(ops):
    tk.Button(root, text=op, command=lambda x=op: sc_app.Standard_Ops(x), font=FONT).grid(row=1 + idx, column=3, sticky='nsew', padx=10, pady=10)

# Scientific buttons
tk.Button(root, text='π', command=sc_app.Pi, font=FONT).grid(row=1, column=4, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='e', command=sc_app.E, font=FONT).grid(row=1, column=5, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='Deg', command=sc_app.Deg, font=FONT).grid(row=1, column=6, sticky='nsew', padx=10, pady=10)

tk.Button(root, text='Exp', command=sc_app.Exp, font=FONT).grid(row=2, column=4, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='x!', command=sc_app.Fact, font=FONT).grid(row=2, column=5, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='Rad', command=sc_app.Rad, font=FONT).grid(row=2, column=6, sticky='nsew', padx=10, pady=10)

tk.Button(root, text='sin', command=sc_app.Sin, font=FONT).grid(row=3, column=4, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='cos', command=sc_app.Cos, font=FONT).grid(row=3, column=5, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='tan', command=sc_app.Tan, font=FONT).grid(row=3, column=6, sticky='nsew', padx=10, pady=10)

tk.Button(root, text='sinh', command=sc_app.Sinh, font=FONT).grid(row=4, column=4, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='cosh', command=sc_app.Cosh, font=FONT).grid(row=4, column=5, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='tanh', command=sc_app.Tanh, font=FONT).grid(row=4, column=6, sticky='nsew', padx=10, pady=10)

tk.Button(root, text='ln', command=sc_app.Ln, font=FONT).grid(row=5, column=4, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='log2', command=sc_app.Log_2, font=FONT).grid(row=5, column=5, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='log10', command=sc_app.Log_10, font=FONT).grid(row=5, column=6, sticky='nsew', padx=10, pady=10)

tk.Button(root, text='x²', command=sc_app.Pow_2, font=FONT).grid(row=1, column=7, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='x³', command=sc_app.Pow_3, font=FONT).grid(row=2, column=7, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='10ⁿ', command=sc_app.Pow_10_n, font=FONT).grid(row=3, column=7, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='1/x', command=sc_app.One_div_x, font=FONT).grid(row=4, column=7, sticky='nsew', padx=10, pady=10)
tk.Button(root, text='Abs', command=sc_app.Abs, font=FONT).grid(row=5, column=7, sticky='nsew', padx=10, pady=10)


# Run App
if __name__ == '__main__':   # FIXED
    root.mainloop()

