import tkinter as tk
from tkinter import ttk

from logic import utils

from .docker import create_general_settings
from .frontend import create_frontend_ui
from .backend import create_backend_ui
from .database import create_database_ui


def create_main_ui(root, generate_fullstack, horizontal_line):
    docker_var = create_general_settings(root)
    horizontal_line(root)
    frontend_vars = create_frontend_ui(root, utils.uncheck_others)
    horizontal_line(root)
    backend_vars = create_backend_ui(root, utils.uncheck_others)
    horizontal_line(root)
    db_vars = create_database_ui(root, utils.uncheck_others)
    horizontal_line(root)

    # Generate fullstack button
    generate_btn = ttk.Button(
        root,
        text="Generate Fullstack",
        command=lambda: generate_fullstack(
            frontend_vars, backend_vars, db_vars, docker_var
        ),
    )
    generate_btn.pack(pady=10)
