import tkinter as tk
from tkinter import ttk


def create_docker_settings(root):
    # General Settings
    general_label = ttk.Label(root, text="General Settings:")
    general_label.pack(pady=10, anchor=tk.W)

    general_frame = ttk.Frame(root)
    general_frame.pack(fill=tk.X, padx=5)

    docker_var = tk.IntVar()
    docker_var.set(1)
    docker_cb = ttk.Checkbutton(general_frame, text="Use Docker", variable=docker_var)
    docker_cb.grid(row=0, column=0, padx=10)

    return docker_var  # Return whatever you may need later
