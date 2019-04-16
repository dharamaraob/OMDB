import configparser

def read_config_file(file_name):    
    config = configparser.ConfigParser()
    config.read(file_name)
    return config
