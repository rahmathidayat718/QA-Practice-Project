import configparser

class Read_Config:

    config = configparser.ConfigParser()
    config.read(".\\config\\login_config.ini")

    @staticmethod
    def get_login_url_page():
        return Read_Config.config.get("settings", "login_url_page")

    @staticmethod
    def get_data_login():
        email = Read_Config.config.get("DataLogin", "email")
        password = Read_Config.config.get("DataLogin", "password")
        return email, password