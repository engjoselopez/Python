# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:03:54 2024

@author: USER
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - Cantidad: {self.cantidad}"

class Tienda:
    def __init__(self):
        self.inventario = []
        self.ventas = {}

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def listar_productos(self):
        return "\n".join(str(producto) for producto in self.inventario)

    def vender_producto(self, nombre, cantidad):
        for producto in self.inventario:
            if producto.nombre == nombre:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    if nombre in self.ventas:
                        self.ventas[nombre] += cantidad
                    else:
                        self.ventas[nombre] = cantidad
                    return f"Venta realizada: {cantidad} x {producto.nombre}"
                else:
                    return "Cantidad insuficiente en el inventario."
        return "Producto no encontrado."

    def generar_reporte_ventas(self, intervalo):
        if not self.ventas:
            return "No se han realizado ventas."
        else:
            resultado = []
            ahora = datetime.now()
            
            for producto, cantidad in self.ventas.items():
                if intervalo == "diario":
                    tiempo_inicio = ahora - timedelta(days=1)
                elif intervalo == "semanal":
                    tiempo_inicio = ahora - timedelta(weeks=1)
                elif intervalo == "mensual":
                    tiempo_inicio = ahora - timedelta(days=30)
                else:
                    tiempo_inicio = datetime.min

                # Aqui se deberia filtrar las ventas por la fecha, actualmente solo se listan todas
                resultado.append(f"Producto: {producto} - Cantidad Vendida: {cantidad}")

            return "\n".join(resultado)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación de Venta de Licores")
        self.geometry("600x400")
        self.tienda = Tienda()

        # Configurar menú
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        archivo_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Salir", command=self.quit)

        # Botones principales
        ttk.Button(self, text="Agregar Producto", command=self.ventana_agregar_producto).pack(pady=10)
        ttk.Button(self, text="Listar Productos", command=self.listar_productos).pack(pady=10)
        ttk.Button(self, text="Vender Producto", command=self.ventana_vender_producto).pack(pady=10)
        ttk.Button(self, text="Generar Reporte de Ventas", command=self.ventana_generar_reporte).pack(pady=10)

        # Ventana principal
        self.salida_text = tk.Text(self, height=15, width=70, font=('Helvetica', 12))
        self.salida_text.pack(pady=10)

    def ventana_agregar_producto(self):
        agregar_ventana = tk.Toplevel(self)
        agregar_ventana.title("Agregar Producto")

        ttk.Label(agregar_ventana, text="Nombre del Producto:").pack(pady=5)
        nombre_entry = ttk.Entry(agregar_ventana, font=('Helvetica', 12))
        nombre_entry.pack(pady=5)

        ttk.Label(agregar_ventana, text="Precio del Producto:").pack(pady=5)
        precio_entry = ttk.Entry(agregar_ventana, font=('Helvetica', 12))
        precio_entry.pack(pady=5)

        ttk.Label(agregar_ventana, text="Cantidad del Producto:").pack(pady=5)
        cantidad_entry = ttk.Entry(agregar_ventana, font=('Helvetica', 12))
        cantidad_entry.pack(pady=5)

        def agregar_producto():
            nombre = nombre_entry.get()
            try:
                precio = float(precio_entry.get())
                cantidad = int(cantidad_entry.get())
                producto = Producto(nombre, precio, cantidad)
                self.tienda.agregar_producto(producto)
                messagebox.showinfo("Información", f"Producto {nombre} agregado exitosamente.")
                agregar_ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, introduce valores válidos para precio y cantidad.")

        ttk.Button(agregar_ventana, text="Agregar Producto", command=agregar_producto).pack(pady=5)

    def ventana_vender_producto(self):
        vender_ventana = tk.Toplevel(self)
        vender_ventana.title("Vender Producto")

        ttk.Label(vender_ventana, text="Nombre del Producto:").pack(pady=5)
        nombre_combo = ttk.Combobox(vender_ventana, values=[producto.nombre for producto in self.tienda.inventario], font=('Helvetica', 12))
        nombre_combo.pack(pady=5)

        ttk.Label(vender_ventana, text="Cantidad a vender:").pack(pady=5)
        cantidad_entry = ttk.Entry(vender_ventana, font=('Helvetica', 12))
        cantidad_entry.pack(pady=5)

        def vender_producto():
            nombre = nombre_combo.get()
            try:
                cantidad = int(cantidad_entry.get())
                resultado = self.tienda.vender_producto(nombre, cantidad)
                messagebox.showinfo("Información", resultado)
                vender_ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, introduce un valor válido para la cantidad.")

        ttk.Button(vender_ventana, text="Vender Producto", command=vender_producto).pack(pady=5)

    def ventana_generar_reporte(self):
        reporte_ventana = tk.Toplevel(self)
        reporte_ventana.title("Generar Reporte de Ventas")

        ttk.Label(reporte_ventana, text="Selecciona el tipo de reporte:").pack(pady=5)
        reporte_combo = ttk.Combobox(reporte_ventana, values=["diario", "semanal", "mensual"], font=('Helvetica', 12))
        reporte_combo.pack(pady=5)

        def generar_reporte():
            intervalo = reporte_combo.get()
            reporte = self.tienda.generar_reporte_ventas(intervalo)
            self.salida_text.delete(1.0, tk.END)
            self.salida_text.insert(tk.END, reporte)
            reporte_ventana.destroy()

        ttk.Button(reporte_ventana, text="Generar Reporte", command=generar_reporte).pack(pady=5)

    def listar_productos(self):
        productos = self.tienda.listar_productos()
        self.salida_text.delete(1.0, tk.END)
        self.salida_text.insert(tk.END, productos)

if __name__ == "__main__":
    app = App()
    app.mainloop()
