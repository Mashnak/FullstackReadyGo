import tkinter as tk
from tkinter import ttk


def create_backend_ui(root, uncheck_others):
    # Backend section
    backend_label = ttk.Label(root, text="Backend:")
    backend_label.pack(pady=10, anchor=tk.W)

    flask_var = tk.IntVar()
    django_var = tk.IntVar()
    spring_var = tk.IntVar()
    spring_var.set(1)

    backends = [flask_var, django_var, spring_var]

    backend_texts = ["Flask", "Django", "Spring Boot"]
    backend_vars = [flask_var, django_var, spring_var]

    backend_frame = ttk.Frame(root)
    backend_frame.pack(fill=tk.X, padx=5)

    for i, (text, var) in enumerate(zip(backend_texts, backend_vars)):
        cb = ttk.Checkbutton(
            backend_frame,
            text=text,
            variable=var,
            command=lambda v=var: uncheck_others(v, backends),
        )
        cb.grid(row=0, column=i, padx=10)

    return backends  # You can return whatever components you may need in the main UI
