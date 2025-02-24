import os
from pathlib import Path

desired_directory = r"c:\Users\RodrigoMartínezAlons\OneDrive - Sparrow Networks GmbH\Python\Classification-Projects-main-new"
os.chdir(desired_directory)
print("Current Working Directory:", os.getcwd()) 

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

print(CONFIG_FILE_PATH)