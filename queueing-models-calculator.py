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
            Lq = (((lam / mu) ** k) * lam * mu) / (factorial(k - 1) * ((k * mu - lam) ** 2)) * P0
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

            sumatoria = sum((factorial(N) / factorial(N - n)) * ((lam / mu) ** n) for n in range(N + 1))
            P0 = 1 / sumatoria
            Lq = N - ((lam + mu) / lam) * (1 - P0)
            L = Lq + (1 - P0)
            Wq = Lq / ((N - L) * lam)
            W = Wq + (1 / mu)
            Pw = 1 - P0
            Pn = [factorial(N) / (factorial(N - n) * (lam / mu) ** n) * P0 for n in range(N + 1)]

            result_P0.config(text=f"P0: {P0:.4f}")
            result_Lq.config(text=f"Lq: {Lq:.4f}")
            result_L.config(text=f"L: {L:.4f}")
            result_Wq.config(text=f"Wq: {Wq:.4f}")
            result_W.config(text=f"W: {W:.4f}")
            result_Pw.config(text=f"Pw: {Pw:.4f}")
            result_Pn.config(text=f"Pn: {Pn[-1]:.4f}")

        elif model_var.get() == "M/D/1":
            if lam >= mu:
                messagebox.showerror("Error", "λ debe ser menor que μ")
                return
            P0 = 1 - (lam / mu)
            Lq = (lam ** 2) / (2 * mu * (mu - lam))
            L = Lq + (lam / mu)
            Wq = Lq / lam
            W = Wq + (1 / mu)
            Pw = lam / mu

            result_P0.config(text=f"P0: {P0:.4f}")
            result_Lq.config(text=f"Lq: {Lq:.4f}")
            result_L.config(text=f"L: {L:.4f}")
            result_Wq.config(text=f"Wq: {Wq:.4f}")
            result_W.config(text=f"W: {W:.4f}")
            result_Pw.config(text=f"Pw: {Pw:.4f}")
            result_Pn.config(text="N/A")  # No aplica para M/D/1

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
    elif model_var.get() == "M/D/1":
        k_label.grid_remove()
        entry_k.grid_remove()
        N_label.grid_remove()
        entry_N.grid_remove()
        sigma_label.grid_remove()
        entry_sigma.grid_remove()
        entry_n.grid_remove()
        label_n.grid_remove()
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
app.title("Cálculo de Líneas de Espera")
app.geometry("800x600")

title_label = tk.Label(app, text="Cálculo de Líneas de Espera", font=("Arial", 24))
title_label.pack(pady=20)

model_var = tk.StringVar(value="M/M/1")
frame = tk.Frame(app)
frame.pack(pady=10)

tk.Radiobutton(frame, text="M/M/1", variable=model_var, value="M/M/1", command=toggle_entries, font=("Arial", 14)).grid(
    row=0, column=0, padx=5)
tk.Radiobutton(frame, text="M/M/k", variable=model_var, value="M/M/k", command=toggle_entries, font=("Arial", 14)).grid(
    row=0, column=1, padx=5)
tk.Radiobutton(frame, text="M/G/1", variable=model_var, value="M/G/1", command=toggle_entries, font=("Arial", 14)).grid(
    row=0, column=2, padx=5)
tk.Radiobutton(frame, text="M/M/k (fuente finita)", variable=model_var, value="M/M/k (fuente finita)",
               command=toggle_entries, font=("Arial", 14)).grid(row=0, column=3, padx=5)
tk.Radiobutton(frame, text="M/M/1 con fuente finita", variable=model_var, value="M/M/1 con fuente finita",
               command=toggle_entries, font=("Arial", 14)).grid(row=0, column=4, padx=5)
tk.Radiobutton(frame, text="M/D/1", variable=model_var, value="M/D/1", command=toggle_entries, font=("Arial", 14)).grid(
    row=0, column=5, padx=5)

inputs_frame = tk.Frame(app)
inputs_frame.pack(pady=20)

tk.Label(inputs_frame, text="λ (tasa de llegadas)", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=5,
                                                                             sticky="e")
entry_lambda = tk.Entry(inputs_frame, font=("Arial", 14))
entry_lambda.grid(row=1, column=1, padx=10, pady=5)

tk.Label(inputs_frame, text="μ (tasa de servicios)", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=5,
                                                                              sticky="e")
entry_mu = tk.Entry(inputs_frame, font=("Arial", 14))
entry_mu.grid(row=2, column=1, padx=10, pady=5)

k_label = tk.Label(inputs_frame, text="k (número de canales)", font=("Arial", 14))
k_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_k = tk.Entry(inputs_frame, font=("Arial", 14))
entry_k.grid(row=3, column=1, padx=10, pady=5)

N_label = tk.Label(inputs_frame, text="N (tamaño de la fuente)", font=("Arial", 14))
N_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_N = tk.Entry(inputs_frame, font=("Arial", 14))
entry_N.grid(row=4, column=1, padx=10, pady=5)

sigma_label = tk.Label(inputs_frame, text="σ (desviación estándar)", font=("Arial", 14))
sigma_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_sigma = tk.Entry(inputs_frame, font=("Arial", 14))
entry_sigma.grid(row=5, column=1, padx=10, pady=5)

label_n = tk.Label(inputs_frame, text="n (número de unidades en el sistema)", font=("Arial", 14))
label_n.grid(row=6, column=0, padx=10, pady=5, sticky="e")
entry_n = tk.Entry(inputs_frame, font=("Arial", 14))
entry_n.grid(row=6, column=1, padx=10, pady=5)

tk.Button(app, text="Calcular", command=calcular, font=("Arial", 14)).pack(pady=20)

results_frame = tk.Frame(app)
results_frame.pack(pady=10)

result_P0 = tk.Label(results_frame, text="P0: ", font=("Arial", 14))
result_P0.grid(row=0, column=0, padx=10, pady=5)

result_Lq = tk.Label(results_frame, text="Lq: ", font=("Arial", 14))
result_Lq.grid(row=1, column=0, padx=10, pady=5)

result_L = tk.Label(results_frame, text="L: ", font=("Arial", 14))
result_L.grid(row=2, column=0, padx=10, pady=5)

result_Wq = tk.Label(results_frame, text="Wq: ", font=("Arial", 14))
result_Wq.grid(row=3, column=0, padx=10, pady=5)

result_W = tk.Label(results_frame, text="W: ", font=("Arial", 14))
result_W.grid(row=4, column=0, padx=10, pady=5)

result_Pw = tk.Label(results_frame, text="Pw: ", font=("Arial", 14))
result_Pw.grid(row=5, column=0, padx=10, pady=5)

result_Pn = tk.Label(results_frame, text="Pn: ", font=("Arial", 14))
result_Pn.grid(row=6, column=0, padx=10, pady=5)

toggle_entries()  # Ensure correct initial state

app.mainloop()
