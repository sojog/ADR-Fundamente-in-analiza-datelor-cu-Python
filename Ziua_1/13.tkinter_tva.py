import tkinter as tk

fereastra = tk.Tk()
fereastra.geometry("500x500")

label = tk.Label(fereastra)
label.config(text="Introdu valoarea fara TVA")
label.pack()

input_valoare = tk.Entry(fereastra)
input_valoare.pack()

label_rezutat = tk.Label(fereastra)
label_rezutat.config(text="Aici va fi valoarea")
label_rezutat.pack()

def calculeaza_tva():
    valoare_input = input_valoare.get()
    valoare_input = int(valoare_input)
    print("Valoare cu tva este:", valoare_input * 1.19 )
    label_rezutat.config(text=valoare_input * 1.19 )

button = tk.Button(fereastra, text="Calculeaza", command=calculeaza_tva)
button.pack()

fereastra.mainloop()
