
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def cargar_imagen(ruta, tamaño=(200, 200)):
    imagen = Image.open(ruta)
    imagen = imagen.resize(tamaño)
    return ImageTk.PhotoImage(imagen)

ventana = tk.Tk()
ventana.title("Simulador: Ka del Rojo de Metilo")

def fase1():
    limpiar_ventana()
    tk.Label(ventana, text="Preparación de solución madre", font=("Arial", 16)).pack()
    img_balanza = cargar_imagen("balanza.png")
    tk.Label(ventana, image=img_balanza).pack()
    ventana.img_balanza = img_balanza
    tk.Button(ventana, text="Pese 0.1 gramos de rojo de metilo", command=pedir_peso).pack()

def pedir_peso():
    limpiar_ventana()
    tk.Label(ventana, text="Ingrese la masa pesada (g):").pack()
    entrada = tk.Entry(ventana)
    entrada.pack()
    def verificar():
        if entrada.get() == "0.1":
            preparar_estandar()
        else:
            messagebox.showerror("Error", "Debe ser exactamente 0.1 g")
    tk.Button(ventana, text="Confirmar", command=verificar).pack()

def preparar_estandar():
    limpiar_ventana()
    tk.Label(ventana, text="Preparación de solución estándar", font=("Arial", 14)).pack()
    img_pipeta = cargar_imagen("pipeta.png")
    tk.Label(ventana, image=img_pipeta).pack()
    ventana.img_pipeta = img_pipeta
    texto = "Se pipetea 5 mL de la solución madre,\nse añade 50 mL de etanol al 95%\ny se afora con agua destilada."
    tk.Label(ventana, text=texto).pack()
    tk.Button(ventana, text="Continuar", command=preparacion_acida).pack()

def preparacion_acida():
    limpiar_ventana()
    tk.Label(ventana, text="Preparación de solución ácida", font=("Arial", 14)).pack()
    img_hcl = cargar_imagen("vaso_HCl.png")
    img_acetato = cargar_imagen("vaso_acetato.png")
    btn_hcl = tk.Button(ventana, image=img_hcl, command=correcto_acido)
    btn_acetato = tk.Button(ventana, image=img_acetato, command=incorrecto)
    btn_hcl.pack(side="left", padx=20)
    btn_acetato.pack(side="right", padx=20)
    ventana.img_hcl = img_hcl
    ventana.img_acetato = img_acetato

def correcto_acido():
    limpiar_ventana()
    img_sol_roja = cargar_imagen("disolucion_roja.png")
    tk.Label(ventana, image=img_sol_roja).pack()
    ventana.img_sol_roja = img_sol_roja
    tk.Label(ventana, text="Disolución rojo púrpura obtenida.").pack()
    tk.Button(ventana, text="Preparación de solución básica", command=preparacion_basica).pack()

def incorrecto():
    messagebox.showerror("Incorrecto", "Esta no es la opción correcta.")

def preparacion_basica():
    limpiar_ventana()
    tk.Label(ventana, text="Preparación de solución básica", font=("Arial", 14)).pack()
    img_hcl = cargar_imagen("vaso_HCl.png")
    img_acetato = cargar_imagen("vaso_acetato.png")
    btn_hcl = tk.Button(ventana, image=img_hcl, command=incorrecto)
    btn_acetato = tk.Button(ventana, image=img_acetato, command=correcto_basico)
    btn_hcl.pack(side="left", padx=20)
    btn_acetato.pack(side="right", padx=20)
    ventana.img_hcl = img_hcl
    ventana.img_acetato = img_acetato

def correcto_basico():
    limpiar_ventana()
    img_sol_amarilla = cargar_imagen("disolucion_amarilla.png")
    tk.Label(ventana, image=img_sol_amarilla).pack()
    ventana.img_sol_amarilla = img_sol_amarilla
    tk.Label(ventana, text="Disolución amarilla obtenida.").pack()
    tk.Button(ventana, text="Finalizar", command=fase_final).pack()

def fase_final():
    limpiar_ventana()
    img_espectro = cargar_imagen("espectrofotometro.png")
    tk.Label(ventana, image=img_espectro).pack()
    ventana.img_espectro = img_espectro
    tk.Label(ventana, text="Coloque las disoluciones ácida y básica...").pack()
    tk.Label(ventana, text="Error: algo falta. ¿Qué paso hace falta?").pack()
    entrada = tk.Entry(ventana)
    entrada.pack()
    def verificar_respuesta():
        if entrada.get().strip().lower() == "medir blanco":
            mostrar_espectro()
        else:
            messagebox.showwarning("Incorrecto", "Pista: falta una medición previa...")
    tk.Button(ventana, text="Confirmar", command=verificar_respuesta).pack()

def mostrar_espectro():
    limpiar_ventana()
    img_espectro_final = cargar_imagen("espectro.png", tamaño=(400, 300))
    tk.Label(ventana, image=img_espectro_final).pack()
    ventana.img_espectro_final = img_espectro_final
    tk.Label(ventana, text="Se observa el espectro con la longitud de onda máxima.").pack()

def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

fase1()
ventana.mainloop()
