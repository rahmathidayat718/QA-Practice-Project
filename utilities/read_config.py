import configparser


class Read_Config:
    config = configparser.ConfigParser()
    config.read(".\\config\\login_config.ini")

    @staticmethod
    def get_login_url_page():
        return Read_Config.config.get("settings", "login_url_page")

    # all
    @staticmethod
    def get_all_login_data(section):
        email = Read_Config.config.get(section, 'email')
        password = Read_Config.config.get(section, 'password')
        exp_result = Read_Config.config.get(section,'exp_result')
        return email, password, exp_result