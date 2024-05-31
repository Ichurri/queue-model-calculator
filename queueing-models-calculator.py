import tkinter as tk
from tkinter import messagebox
from math import factorial


def calcular():
    try:
        lam = float(entry_lambda.get())
        mu = float(entry_mu.get())

        if model_var.get() == "M/M/1":
            n = int(entry_n.get())
            if lam >= mu:
                messagebox.showerror("Error", "λ debe ser menor que μ")
                return
            P0 = 1 - (lam / mu)
            Lq = (lam ** 2) / (mu * (mu - lam))
            L = Lq + (lam / mu)
            Wq = Lq / lam
            W = Wq + (1 / mu)
            Pw = lam / mu
            Pn = ((lam / mu) ** n) * P0

            result_P0.config(text=f"P0: {P0:.4f}")
            result_Lq.config(text=f"Lq: {Lq:.4f}")
            result_L.config(text=f"L: {L:.4f}")
            result_Wq.config(text=f"Wq: {Wq:.4f}")
            result_W.config(text=f"W: {W:.4f}")
            result_Pw.config(text=f"Pw: {Pw:.4f}")
            result_Pn.config(text=f"Pn: {Pn:.4f}")

        elif model_var.get() == "M/M/k":
            n = int(entry_n.get())
            k = int(entry_k.get())
            if lam >= mu * k:
                messagebox.showerror("Error", "λ debe ser menor que k * μ")
                return
            sumatoria = sum((lam / mu) ** i / factorial(i) for i in range(k))
            P0 = 1 / (sumatoria + ((lam / mu) ** k / factorial(k)) * (k * mu / (k * mu - lam)))
            Lq = ((lam / mu) ** k * lam * mu) / (factorial(k) * ((k * mu - lam) ** 2)) * P0
            L = Lq + lam / mu
            Wq = Lq / lam
            W = Wq + 1 / mu
            Pw = (1 / factorial(k)) * (lam / mu) ** k * (k * mu / (k * mu - lam)) * P0
            if n <= k:
                Pn = ((lam / mu) ** n / factorial(n)) * P0
            else:
                Pn = ((lam / mu) ** n / (factorial(k) * (k ** (n - k)))) * P0

            result_P0.config(text=f"P0: {P0:.4f}")
            result_Lq.config(text=f"Lq: {Lq:.4f}")
            result_L.config(text=f"L: {L:.4f}")
            result_Wq.config(text=f"Wq: {Wq:.4f}")
            result_W.config(text=f"W: {W:.4f}")
            result_Pw.config(text=f"Pw: {Pw:.4f}")
            result_Pn.config(text=f"Pn: {Pn:.4f}")

        elif model_var.get() == "M/G/1":
            n = int(entry_n.get())
            sigma = float(entry_sigma.get())
            if lam >= mu:
                messagebox.showerror("Error", "λ debe ser menor que μ")
                return
            P0 = 1 - (lam / mu)
            Lq = (lam ** 2 * sigma ** 2 + (lam / mu) ** 2) / (2 * (1 - lam / mu))
            L = Lq + (lam / mu)
            Wq = Lq / lam
            W = Wq + (1 / mu)
            Pw = lam / mu
            Pn = ((lam / mu) ** n) * P0

            result_P0.config(text=f"P0: {P0:.4f}")
            result_Lq.config(text=f"Lq: {Lq:.4f}")
            result_L.config(text=f"L: {L:.4f}")
            result_Wq.config(text=f"Wq: {Wq:.4f}")
            result_W.config(text=f"W: {W:.4f}")
            result_Pw.config(text=f"Pw: {Pw:.4f}")
            result_Pn.config(text=f"Pn: {Pn:.4f}")

        elif model_var.get() == "M/M/k (fuente finita)":
            k = int(entry_k.get())
            N = int(entry_N.get())
            if lam >= mu * k:
                messagebox.showerror("Error", "λ debe ser menor que k * μ")
                return

            def C(n, lam, mu, k):
                if n < k:
                    return (lam / mu) ** n / factorial(n)
                else:
                    return (lam / mu) ** n / (factorial(k) * k ** (n - k))

            sumatoria1 = sum(C(n, lam, mu, k) for n in range(k))
            sumatoria2 = sum(factorial(N) / (factorial(N - n) * C(n, lam, mu, k)) for n in range(k, N + 1))
            P0 = 1 / (sumatoria1 + sumatoria2)

            def Pn(n, P0, lam, mu, k, N):
                if n < k:
                    return C(n, lam, mu, k) * P0
                else:
                    return (factorial(N) / (factorial(N - n) * C(n, lam, mu, k))) * P0

            Pn_values = [Pn(n, P0, lam, mu, k, N) for n in range(N + 1)]
            L = sum(n * Pn_values[n] for n in range(N + 1))
            lam_e = sum((N - n) * lam * Pn_values[n] for n in range(N + 1))
            W = L / lam_e
            rho = lam_e / (k * mu)
            Wq = W - 1 / mu
            Lq = Wq * lam_e
            Pw = 1 - sum(Pn_values[n] for n in range(k))

            result_P0.config(text=f"P0: {P0:.4f}")
            result_Lq.config(text=f"Lq: {Lq:.4f}")
            result_L.config(text=f"L: {L:.4f}")
            result_Wq.config(text=f"Wq: {Wq:.4f}")
            result_W.config(text=f"W: {W:.4f}")
            result_Pw.config(text=f"Pw: {Pw:.4f}")
            result_Pn.config(text=f"Pn: {Pn_values[-1]:.4f}")

        elif model_var.get() == "M/M/1 con fuente finita":
            n = int(entry_n.get())
            N = int(entry_N.get())
            if lam >= mu:
                messagebox.showerror("Error", "λ debe ser menor que μ")
                return

            sumatoria = sum((factorial(N) / (factorial(N - n)) * (lam / mu) ** n) for n in range(N + 1))
            P0 = 1 / sumatoria
            # Lq = N - (lam / mu) * (1 - P0)
            Lq = N - ((lam + mu) / lam) * (1 - P0)
            L = Lq + (1 - P0)
            Wq = Lq / ((N - L) * lam)
            W = Wq + (1 / mu)
            Pw = 1 - P0
            Pn = [(factorial(N) / (factorial(N - n)) * (lam / mu) ** n) * P0]

            result_P0.config(text=f"P0: {P0:.4f}")
            result_Lq.config(text=f"Lq: {Lq:.4f}")
            result_L.config(text=f"L: {L:.4f}")
            result_Wq.config(text=f"Wq: {Wq:.4f}")
            result_W.config(text=f"W: {W:.4f}")
            result_Pw.config(text=f"Pw: {Pw:.4f}")
            result_Pn.config(text=f"Pn: {Pn[-1]:.4f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")


def toggle_entries():
    if model_var.get() == "M/M/k":
        k_label.grid()
        entry_k.grid()
        N_label.grid_remove()
        entry_N.grid_remove()
        sigma_label.grid_remove()
        entry_sigma.grid_remove()
        entry_n.grid()
        label_n.grid()
    elif model_var.get() == "M/M/k (fuente finita)":
        k_label.grid()
        entry_k.grid()
        N_label.grid()
        entry_N.grid()
        sigma_label.grid_remove()
        entry_sigma.grid_remove()
        entry_n.grid()
        label_n.grid()
    elif model_var.get() == "M/G/1":
        sigma_label.grid()
        entry_sigma.grid()
        k_label.grid_remove()
        entry_k.grid_remove()
        N_label.grid_remove()
        entry_N.grid_remove()
        entry_n.grid()
        label_n.grid()
    elif model_var.get() == "M/M/1 con fuente finita":
        entry_n.grid()
        label_n.grid()
        N_label.grid()
        entry_N.grid()
        k_label.grid_remove()
        entry_k.grid_remove()
        sigma_label.grid_remove()
        entry_sigma.grid_remove()
    else:  # M/M/1
        k_label.grid_remove()
        entry_k.grid_remove()
        sigma_label.grid_remove()
        entry_sigma.grid_remove()
        N_label.grid_remove()
        entry_N.grid_remove()
        entry_n.grid()
        label_n.grid()


app = tk.Tk()
app.title("Modelos de Colas")

model_var = tk.StringVar(value="M/M/1")
tk.Radiobutton(app, text="M/M/1", variable=model_var, value="M/M/1", command=toggle_entries).grid(row=0, column=0)
tk.Radiobutton(app, text="M/M/k", variable=model_var, value="M/M/k", command=toggle_entries).grid(row=0, column=1)
tk.Radiobutton(app, text="M/G/1", variable=model_var, value="M/G/1", command=toggle_entries).grid(row=0, column=2)
tk.Radiobutton(app, text="M/M/k (fuente finita)", variable=model_var, value="M/M/k (fuente finita)",
               command=toggle_entries).grid(row=0, column=3)
tk.Radiobutton(app, text="M/M/1 con fuente finita", variable=model_var, value="M/M/1 con fuente finita",
               command=toggle_entries).grid(row=0, column=4)

tk.Label(app, text="λ (tasa de llegadas)").grid(row=1, column=0)
entry_lambda = tk.Entry(app)
entry_lambda.grid(row=1, column=1)

tk.Label(app, text="μ (tasa de servicios)").grid(row=2, column=0)
entry_mu = tk.Entry(app)
entry_mu.grid(row=2, column=1)

k_label = tk.Label(app, text="k (número de canales)")
k_label.grid(row=3, column=0)
entry_k = tk.Entry(app)
entry_k.grid(row=3, column=1)

N_label = tk.Label(app, text="N (tamaño de la fuente)")
N_label.grid(row=4, column=0)
entry_N = tk.Entry(app)
entry_N.grid(row=4, column=1)

sigma_label = tk.Label(app, text="σ (desviación estándar)")
sigma_label.grid(row=5, column=0)
entry_sigma = tk.Entry(app)
entry_sigma.grid(row=5, column=1)

label_n = tk.Label(app, text="n (número de unidades en el sistema)")
label_n.grid(row=6, column=0)
entry_n = tk.Entry(app)
entry_n.grid(row=6, column=1)

tk.Button(app, text="Calcular", command=calcular).grid(row=7, column=0, columnspan=2)

result_P0 = tk.Label(app, text="P0: ")
result_P0.grid(row=8, column=0, columnspan=2)

result_Lq = tk.Label(app, text="Lq: ")
result_Lq.grid(row=9, column=0, columnspan=2)

result_L = tk.Label(app, text="L: ")
result_L.grid(row=10, column=0, columnspan=2)

result_Wq = tk.Label(app, text="Wq: ")
result_Wq.grid(row=11, column=0, columnspan=2)

result_W = tk.Label(app, text="W: ")
result_W.grid(row=12, column=0, columnspan=2)

result_Pw = tk.Label(app, text="Pw: ")
result_Pw.grid(row=13, column=0, columnspan=2)

result_Pn = tk.Label(app, text="Pn: ")
result_Pn.grid(row=14, column=0, columnspan=2)

toggle_entries()  # Ensure correct initial state

app.mainloop()
