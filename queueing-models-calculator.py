import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        lam = float(entry_lambda.get())
        mu = float(entry_mu.get())

        if lam >= mu:
            messagebox.showerror("Error", "λ debe ser menor que μ")
            return

        P0 = 1 - (lam / mu)
        Lq = (lam ** 2) / (mu * (mu - lam))
        L = Lq + (lam / mu)
        Wq = Lq / lam
        W = Wq + (1 / mu)
        Pw = lam / mu
        n = int(entry_n.get())
        Pn = ((lam / mu) ** n) * P0

        result_P0.config(text=f"P0: {P0:.4f}")
        result_Lq.config(text=f"Lq: {Lq:.4f}")
        result_L.config(text=f"L: {L:.4f}")
        result_Wq.config(text=f"Wq: {Wq:.4f}")
        result_W.config(text=f"W: {W:.4f}")
        result_Pw.config(text=f"Pw: {Pw:.4f}")
        result_Pn.config(text=f"Pn: {Pn:.4f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")


app = tk.Tk()
app.title("Modelo de Colas M/M/1")

tk.Label(app, text="λ (tasa de llegadas)").grid(row=0, column=0)
entry_lambda = tk.Entry(app)
entry_lambda.grid(row=0, column=1)

tk.Label(app, text="μ (tasa de servicios)").grid(row=1, column=0)
entry_mu = tk.Entry(app)
entry_mu.grid(row=1, column=1)

tk.Label(app, text="n (número de unidades en el sistema)").grid(row=2, column=0)
entry_n = tk.Entry(app)
entry_n.grid(row=2, column=1)

tk.Button(app, text="Calcular", command=calcular).grid(row=3, column=0, columnspan=2)

result_P0 = tk.Label(app, text="P0: ")
result_P0.grid(row=4, column=0, columnspan=2)

result_Lq = tk.Label(app, text="Lq: ")
result_Lq.grid(row=5, column=0, columnspan=2)

result_L = tk.Label(app, text="L: ")
result_L.grid(row=6, column=0, columnspan=2)

result_Wq = tk.Label(app, text="Wq: ")
result_Wq.grid(row=7, column=0, columnspan=2)

result_W = tk.Label(app, text="W: ")
result_W.grid(row=8, column=0, columnspan=2)

result_Pw = tk.Label(app, text="Pw: ")
result_Pw.grid(row=9, column=0, columnspan=2)

result_Pn = tk.Label(app, text="Pn: ")
result_Pn.grid(row=10, column=0, columnspan=2)

app.mainloop()
