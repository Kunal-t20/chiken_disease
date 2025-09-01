import os 
from pathlib import Path
import logging 





project_name="chicken_disease_clissifier"

list_of_file=[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componenets/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/constsants/__init__.py",
    f"src/{project_name}/config/configuration.py/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]