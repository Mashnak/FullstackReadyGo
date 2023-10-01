import tkinter as tk
from tkinter import ttk


def create_frontend_ui(root, uncheck_others):
    # Frontend section
    frontend_label = ttk.Label(root, text="Frontend:")
    frontend_label.pack(pady=10, anchor=tk.W)

    angular_var = tk.IntVar()
    angular_var.set(1)
    react_var = tk.IntVar()

    frontends = [angular_var, react_var]

    frontend_texts = ["Angular", "React"]
    frontend_vars = [angular_var, react_var]

    frontend_frame = ttk.Frame(root)
    frontend_frame.pack(fill=tk.X, padx=5)

    for i, (text, var) in enumerate(zip(frontend_texts, frontend_vars)):
        cb = ttk.Checkbutton(
            frontend_frame,
            text=text,
            variable=var,
            command=lambda v=var: uncheck_others(v, frontends),
        )
        cb.grid(row=0, column=i, padx=10)

    return frontends  # You can return whatever components you may need in the main UI
