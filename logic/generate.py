from tkinter import ttk, filedialog, messagebox
import subprocess
import shutil
import os
import tkinter as tk


def get_selected_technologies(variables, names):
    return [name for var, name in zip(variables, names) if var.get() == 1]


def create_angular_project(directory, root_directory):
    try:
        cmd = f"ng new {directory} --routing=true --style=css --skip-install --skip-git"
        subprocess.check_call(cmd, cwd=root_directory, shell=True)
        print(f"Successfully created Angular project {directory}")

    except subprocess.CalledProcessError as e:
        print(f"Error creating Angular project: {e}")


def setup_directories(root_directory, selected, directories, docker_selected):
    for name in selected:
        directory_path = os.path.join(root_directory, directories[name])

        if name == "Angular":
            create_angular_project(directories[name], root_directory)
        else:
            os.makedirs(directory_path, exist_ok=True)

        if docker_selected:
            with open(os.path.join(directory_path, "Dockerfile"), "w") as file:
                file.write(f"# Dockerfile for {name}\n")
                file.write(
                    f"# You can add the necessary commands to build the Docker image for {name} here\n"
                )


def create_docker_compose(root_directory, selected, directories):
    with open(os.path.join(root_directory, "docker-compose.yml"), "w") as file:
        file.write('version: "3"\n')
        file.write("services:\n")
        for name in selected:
            file.write(f"  {directories[name]}:\n")
            file.write(f"    build: ./{directories[name]}\n")


def generate_fullstack(frontend_var, backend_vars, db_var, docker_var):
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

    root_directory = "fullstack_temp"
    os.makedirs(root_directory, exist_ok=True)

    frontend_selected = get_selected_technologies(frontend_var, ["Angular", "React"])
    backend_selected = get_selected_technologies(
        backend_vars, ["Flask", "Django", "Spring Boot"]
    )
    db_selected = get_selected_technologies(
        db_var, ["Neo4J", "MongoDB", "PostgreSQL", "MySQL"]
    )

    selected = frontend_selected + backend_selected + db_selected
    docker_selected = docker_var.get() == 1

    setup_directories(root_directory, selected, directories, docker_selected)

    if docker_selected:
        create_docker_compose(root_directory, selected, directories)

    # Saving the entire structure as a zip
    save_directory = filedialog.asksaveasfilename(
        title="Save Zip As",
        defaultextension=".zip",
        filetypes=[("Zip files", "*.zip")],
        initialfile="FullstackReadyGo.zip",
        initialdir=os.path.expanduser("~/Documents"),
    )
    if not save_directory:
        shutil.rmtree(root_directory)  # Removing the temporary directory
        return

    shutil.make_archive(save_directory.replace(".zip", ""), "zip", root_directory)
    shutil.rmtree(root_directory)  # Removing the temporary directory
    messagebox.showinfo("Success", f"Files zipped and saved at: {save_directory}")
