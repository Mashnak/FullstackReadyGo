import os
import tkinter as tk
from tkinter import ttk, filedialog


def uncheck_others(current_var, variables):
    for var in variables:
        if var is not current_var:
            var.set(0)


def horizontal_line(parent):
    ttk.Separator(parent, orient="horizontal").pack(fill=tk.X, pady=10)


def generate_fullstack(frontend_var, backend_vars, db_var, docker_var, root_directory):
    directories = {
        "Angular": "frontend_angular",
        "React": "frontend_react",
        "Flask": "backend_flask",
        "Django": "backend_django",
        "Spring Boot": "backend_spring_boot",
        "Neo4J": "database_neo4j",
        "MongoDB": "database_mongodb",
        "PostgreSQL": "database_postgresql",
        "MySQL": "database_mysql",
    }

    selected = []
    if frontend_var.get() == 1:
        selected.append("Angular")
    else:
        selected.append("React")

    for var, name in zip(backend_vars, ["Flask", "Django", "Spring Boot"]):
        if var.get() == 1:
            selected.append(name)

    for var, name in zip(db_var, ["Neo4J", "MongoDB", "PostgreSQL", "MySQL"]):
        if var.get() == 1:
            selected.append(name)

    docker_selected = docker_var.get() == 1

    for name in selected:
        directory_path = os.path.join(root_directory, directories[name])
        os.makedirs(directory_path, exist_ok=True)
        if (
            docker_selected
        ):  # If Docker is selected, create a Dockerfile in each directory
            with open(os.path.join(directory_path, "Dockerfile"), "w") as file:
                file.write(f"# Dockerfile for {name}\n")
                file.write(
                    f"# You can add the necessary commands to build the Docker image for {name} here\n"
                )

    if docker_selected:
        with open(os.path.join(root_directory, "docker-compose.yml"), "w") as file:
            file.write('version: "3"\n')
            file.write("services:\n")
            for name in selected:
                file.write(f"  {directories[name]}:\n")
                file.write(
                    f"    build: ./{directories[name]}\n"
                )  # Pointing to the directory of the service

    print(f"Directories and files created at: {root_directory}")


def main():
    root = tk.Tk()
    root.title("FullstackReadyGo")
    root.resizable(False, False)

    # General Settings
    general_label = ttk.Label(root, text="General Settings:")
    general_label.pack(pady=10, anchor=tk.W)

    general_frame = ttk.Frame(root)
    general_frame.pack(fill=tk.X, padx=5)

    docker_var = tk.IntVar()
    docker_cb = ttk.Checkbutton(general_frame, text="Use Docker", variable=docker_var)
    docker_cb.grid(row=0, column=0, padx=10)

    # Frontend section
    frontend_label = ttk.Label(root, text="Frontend:")
    frontend_label.pack(pady=10, anchor=tk.W)

    angular_var = tk.IntVar()
    react_var = tk.IntVar()

    frontend_frame = ttk.Frame(root)
    frontend_frame.pack(fill=tk.X, padx=5)

    angular_cb = ttk.Checkbutton(
        frontend_frame,
        text="Angular",
        variable=angular_var,
        command=lambda: uncheck_others(angular_var, [angular_var, react_var]),
    )
    angular_cb.grid(row=0, column=0, padx=10)

    react_cb = ttk.Checkbutton(
        frontend_frame,
        text="React",
        variable=react_var,
        command=lambda: uncheck_others(react_var, [angular_var, react_var]),
    )
    react_cb.grid(row=0, column=1, padx=10)

    horizontal_line(root)

    # Backend section
    backend_label = ttk.Label(root, text="Backend:")
    backend_label.pack(pady=10, anchor=tk.W)

    flask_var = tk.IntVar()
    django_var = tk.IntVar()
    spring_var = tk.IntVar()

    backends = [flask_var, django_var, spring_var]

    backend_frame = ttk.Frame(root)
    backend_frame.pack(fill=tk.X, padx=5)

    backend_texts = ["Flask", "Django", "Spring Boot"]
    backend_vars = [flask_var, django_var, spring_var]

    for i, (text, var) in enumerate(zip(backend_texts, backend_vars)):
        cb = ttk.Checkbutton(
            backend_frame,
            text=text,
            variable=var,
            command=lambda v=var: uncheck_others(v, backends),
        )
        cb.grid(row=0, column=i, padx=10)

    horizontal_line(root)

    # Database section
    db_label = ttk.Label(root, text="Database:")
    db_label.pack(pady=10, anchor=tk.W)

    neo4j_var = tk.IntVar()
    mongo_var = tk.IntVar()
    postgres_var = tk.IntVar()
    mysql_var = tk.IntVar()

    dbs = [neo4j_var, mongo_var, postgres_var, mysql_var]

    db_frame = ttk.Frame(root)
    db_frame.pack(fill=tk.X, padx=5)

    db_texts = ["Neo4J", "MongoDB", "PostgreSQL", "MySQL"]
    db_vars = [neo4j_var, mongo_var, postgres_var, mysql_var]

    for i, (text, var) in enumerate(zip(db_texts, db_vars)):
        cb = ttk.Checkbutton(
            db_frame,
            text=text,
            variable=var,
            command=lambda v=var: uncheck_others(v, dbs),
        )
        cb.grid(row=0, column=i, padx=10)

    horizontal_line(root)

    # Button to choose directory
    directory_var = tk.StringVar()
    directory_var.set("Choose a directory...")
    directory_btn = ttk.Button(
        root,
        text="Choose Directory",
        command=lambda: directory_var.set(filedialog.askdirectory()),
    )
    directory_btn.pack(pady=10)
    directory_label = ttk.Label(root, textvariable=directory_var)
    directory_label.pack(pady=5)

    # Generate fullstack button
    generate_btn = ttk.Button(
        root,
        text="Generate Fullstack",
        command=lambda: generate_fullstack(
            angular_var, backends, dbs, docker_var, directory_var.get()
        ),
    )
    generate_btn.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
