import tkinter as tk
from tkinter import messagebox, filedialog
import mysql.connector

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',  # Cambia esto según tu configuración de MySQL
    'password': '',  # Cambia esto según tu configuración de MySQL
    'host': '127.0.0.1',
    'database': 'gestion_documentos'
}

def login_usuario(id_usuario, nombre_usuario, area_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    # Consulta para verificar las credenciales
    query = "SELECT id, nombre, area_id FROM usuarios WHERE id = %s AND nombre = %s AND area_id = %s"
    cursor.execute(query, (id_usuario, nombre_usuario, area_id))
    
    usuario = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return usuario

def mostrar_mensaje_area(nombre_usuario, area_id, root):
    # Crear una nueva ventana para mostrar el mensaje de área
    area_window = tk.Toplevel()
    area_window.title("Área Correspondiente")
    area_window.geometry("400x300")
    
    # Mensaje de bienvenida con el área correspondiente
    mensaje = f"Bienvenido, {nombre_usuario}!\n\nHas ingresado al área con ID {area_id}."
    mensaje_label = tk.Label(area_window, text=mensaje, padx=20, pady=20)
    mensaje_label.pack()
    
    # Botón para subir documentos
    subir_documento_button = tk.Button(area_window, text="Subir Documento", command=lambda: abrir_dialogo_subir_documento(area_window))
    subir_documento_button.pack(pady=10)
    
    # Caja de texto para comentarios
    comentarios_label = tk.Label(area_window, text="Comentarios:")
    comentarios_label.pack(pady=(20, 5))
    
    comentarios_text = tk.Text(area_window, height=4, width=40)
    comentarios_text.pack()
    
    # Botón para regresar al login
    regresar_button = tk.Button(area_window, text="Regresar", command=lambda: regresar_login(area_window, root))
    regresar_button.pack(pady=10)

def abrir_dialogo_subir_documento(parent):
    filetypes = (
        ("Archivos PDF", "*.pdf"),
        ("Archivos Excel", "*.xls *.xlsx"),
        ("Archivos Word", "*.doc *.docx"),
        ("Archivos PowerPoint", "*.ppt *.pptx"),
        ("Todos los archivos", "*.*")
    )
    filename = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=filetypes)
    if filename:
        messagebox.showinfo("Documento Subido", f"Se ha subido el documento:\n{filename}")

def regresar_login(area_window, root):
    area_window.destroy()  # Cerrar la ventana actual
    root.deiconify()  # Mostrar nuevamente la ventana de login

# Crear ventana principal para el login
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Marco con bordes redondeados
frame = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
frame.pack(pady=20)

# Etiqueta y entrada para ID
id_label = tk.Label(frame, text="ID:")
id_label.grid(row=0, column=0, sticky="w", pady=5)
id_entry = tk.Entry(frame, width=20)
id_entry.grid(row=0, column=1, pady=5)

# Etiqueta y entrada para Nombre
nombre_label = tk.Label(frame, text="Nombre:")
nombre_label.grid(row=1, column=0, sticky="w", pady=5)
nombre_entry = tk.Entry(frame, width=20)
nombre_entry.grid(row=1, column=1, pady=5)

# Etiqueta y entrada para Área ID
area_label = tk.Label(frame, text="Área ID:")
area_label.grid(row=2, column=0, sticky="w", pady=5)
area_entry = tk.Entry(frame, width=20)
area_entry.grid(row=2, column=1, pady=5)

# Botón de login
login_button = tk.Button(frame, text="Login", command=lambda: on_login(root))
login_button.grid(row=3, columnspan=2, pady=10)

# Función para procesar el login
def on_login(root):
    id_usuario = id_entry.get()
    nombre_usuario = nombre_entry.get()
    area_id = area_entry.get()
    
    # Validar campos
    if not id_usuario or not nombre_usuario or not area_id:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
        return
    
    # Intentar hacer login
    usuario = login_usuario(id_usuario, nombre_usuario, area_id)
    
    if usuario:
        # Mostrar mensaje de área correspondiente y opciones de documentos
        mostrar_mensaje_area(usuario[1], usuario[2], root)
        root.withdraw()  # Ocultar la ventana de login después de iniciar sesión correctamente
    else:
        messagebox.showerror("Error", "Credenciales incorrectas. Por favor, verifica tus datos.")

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
