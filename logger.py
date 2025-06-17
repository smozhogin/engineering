import os
import logging

log_dir = '/app/project/medic_pipeline/logs'
max_size_mb = 5
backups_num = 3

def logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.handlers:
        os.makedirs(log_dir, exist_ok=True)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, f'{name}.log'), maxBytes=(max_size_mb * 1024 * 1024), backupCount=backups_num
        )
        
        file_handler.setLevel(level)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        
    return logger
