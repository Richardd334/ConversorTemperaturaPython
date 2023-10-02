
import tkinter as tk

def convertidor_a_celsius():
    fahrenheit = float(Entry1.get())
    celsius=(fahrenheit-32)*5.0/9.0
    Entry2.delete(0,tk.END)
    Entry2.insert(0, f"{celsius:.2f}")

def convertidor_a_fahrenheit():
    celsius= float(Entry2.get())
    fahrenheit=(celsius*9/5)+32
    Entry1.delete(0,tk.END)
    Entry1.insert(0, f"{fahrenheit:.2f}")

def reset():
    Entry1.delete(0, tk.END)
    Entry1.insert(0, "0.0")
    Entry2.delete(0, tk.END)
    Entry2.insert(0, "0.0")


Pantalla = tk.Tk()
Pantalla.title("conversor de temperatura")

#Pantalla.geometry("255x180")

label1=tk.Label(Pantalla, text= "Fahrenheit:")
label1.grid(row=0, column=0)

Entry1=tk.Entry()
Entry1.grid(row=0, column=1)

Boton1=tk.Button(Pantalla, text="Convertir a Celsius", command=convertidor_a_celsius)
Boton1.grid(row=0, column=2)

label2=tk.Label(Pantalla, text= "Celsius:")
label2.grid(row=1, column=0)

Entry2=tk.Entry()
Entry2.grid(row=1, column=1)

Boton2=tk.Button(Pantalla, text="Convertir a Fahrenheit", command=convertidor_a_fahrenheit)
Boton2.grid(row=1, column=2)

Boton3=tk.Button(Pantalla, text="Restablecer", command=reset)
Boton3.grid(row=2, column=1)


Pantalla.mainloop()