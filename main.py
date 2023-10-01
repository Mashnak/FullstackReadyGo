import tkinter as tk
from tkinter import ttk

from ui import main_ui
from logic import generate


def horizontal_line(root):
    ttk.Separator(root, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)


def main():
    root = tk.Tk()
    root.title("FullstackReadyGo")
    root.resizable(False, False)

    main_ui.create_main_ui(root, generate.generate_fullstack, horizontal_line)

    root.mainloop()


if __name__ == "__main__":
    main()
