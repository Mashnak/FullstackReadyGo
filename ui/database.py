import tkinter as tk
from tkinter import ttk


def create_database_ui(root, uncheck_others):
    # Database section
    db_label = ttk.Label(root, text="Database:")
    db_label.pack(pady=10, anchor=tk.W)

    neo4j_var = tk.IntVar()
    mongo_var = tk.IntVar()
    postgres_var = tk.IntVar()
    mysql_var = tk.IntVar()

    dbs = [neo4j_var, mongo_var, postgres_var, mysql_var]

    db_texts = ["Neo4J", "MongoDB", "PostgreSQL", "MySQL"]
    db_vars = [neo4j_var, mongo_var, postgres_var, mysql_var]

    db_frame = ttk.Frame(root)
    db_frame.pack(fill=tk.X, padx=5)

    for i, (text, var) in enumerate(zip(db_texts, db_vars)):
        cb = ttk.Checkbutton(
            db_frame,
            text=text,
            variable=var,
            command=lambda v=var: uncheck_others(v, dbs),
        )
        cb.grid(row=0, column=i, padx=10)

    return dbs  # Return the list of db checkbutton variables
