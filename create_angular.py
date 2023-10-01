import subprocess

project_name = "my-angular-app"

try:
    cmd = f"ng new {project_name} --routing=true --style=scss --skip-install"
    subprocess.check_call(cmd, shell=True)
    print(f"Successfully created Angular project {project_name}")

except subprocess.CalledProcessError as e:
    print(f"Error creating Angular project: {e}")
