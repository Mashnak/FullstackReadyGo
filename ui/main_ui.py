import tkinter as tk
from tkinter import ttk, Menu, messagebox
from logic import utils

from .docker import create_docker_settings
from .frontend import create_frontend_ui
from .backend import create_backend_ui
from .database import create_database_ui


def new_project():
    print("Creating a new project...")


def open_project():
    print("Opening a project...")


def undo_action():
    print("Undoing the last action...")


def show_about():
    about_title = "About FullstackReadyGo"
    about_message = """
FullstackReadyGo

Version: 1.0.0

This tool helps in quickly setting up a full-stack project with multiple frontend, backend, and database options.

You can easily choose which technology you want for each part and then generate a zipped project structure.
    
Visit our GitHub repository for more information and updates.
    """
    messagebox.showinfo(about_title, about_message.strip())


def create_menu(root):
    # Create the main menu bar
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    # Create a menu and add it to the menu bar
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Add menu items to the 'File' menu
    file_menu.add_command(label="New Project", command=new_project)
    file_menu.add_command(label="Open", command=open_project)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # Add more menus to the menu bar as needed
    edit_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Undo", command=undo_action)

    # Add Help menu
    help_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=show_about)


def create_main_ui(root, generate_fullstack, horizontal_line):
    create_menu(root)  # This line integrates the menu bar

    docker_var = create_docker_settings(root)
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
