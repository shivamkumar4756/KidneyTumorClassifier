import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[                              # It will print all the log messages to the console and also to the file
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)    
    ]
)

logger = logging.getLogger("cnnClassifierLogger")