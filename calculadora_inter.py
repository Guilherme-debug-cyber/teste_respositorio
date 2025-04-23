import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        numero1 = int(entry_numero1.get())
        numero2 = int(entry_numero2.get())
        operador = entry_operador.get()

        if operador not in ['+', '-', '/', '*']:
            raise ValueError("Operador inválido! Use +, -, / ou *.")

        if operador == '+':
            resultado = numero1 + numero2
        elif operador == '-':
            resultado = numero1 - numero2
        elif operador == '/':
            if numero2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida!")
            resultado = numero1 / numero2
        elif operador == '*':
            resultado = numero1 * numero2

        messagebox.showinfo("Resultado", f"O resultado é: {resultado}")
    except ValueError as ve:
        messagebox.showerror("Erro de entrada", str(ve))
    except ZeroDivisionError as zde:
        messagebox.showerror("Erro de cálculo", str(zde))
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Widgets
tk.Label(janela, text="Primeiro número:").grid(row=0, column=0, padx=10, pady=5)
entry_numero1 = tk.Entry(janela)
entry_numero1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Operador (+, -, /, *):").grid(row=1, column=0, padx=10, pady=5)
entry_operador = tk.Entry(janela)
entry_operador.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Segundo número:").grid(row=2, column=0, padx=10, pady=5)
entry_numero2 = tk.Entry(janela)
entry_numero2.grid(row=2, column=1, padx=10, pady=5)

btn_calcular = tk.Button(janela, text="Calcular", command=calcular)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

# Inicia o loop principal da interface
janela.mainloop()
