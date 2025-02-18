import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

desired_directory = r"Classification-Projects-main-new"
os.chdir(desired_directory)
print("Current Working Directory:", os.getcwd()) 

# project_root = os.path.abspath(os.path.dirname(__file__))
log_dir = "logs"

# sys.path.append(os.path.join(project_root, log_dir))

log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")