import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    config = configparser.ConfigParser()
    config.read(".\\data\\login.ini")

    @staticmethod
    def get_login_url_page():
        return Read_Config.config.get("settings", "login_url_page")

    # all
    @staticmethod
    def all_ecommerce_login(section):
        email = Read_Config.config.get(section, 'username')
        password = Read_Config.config.get(section, 'password')
        exp_result = Read_Config.config.get(section,'expected_result')
        return email, password, exp_result