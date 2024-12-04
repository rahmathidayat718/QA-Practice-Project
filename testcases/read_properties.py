import configparser

class Read_Config:

    config = configparser.ConfigParser()
    config.read(".\\config\\login_config.ini")

    @staticmethod
    def get_login_url_page():
        return Read_Config.config.get("settings", "login_url_page")

    @staticmethod
    def get_login_ecommerce_data():
        login_data = []
        for section in Read_Config.config.sections():
            if "login" in section.lower():
                email = Read_Config.config.get(section, 'email', fallback=None)
                password = Read_Config.config.get(section, 'password', fallback=None)
                exp_result = Read_Config.config.get(section, 'exp_result', fallback=None)
                login_data.append((email, password, exp_result, section))
        return login_data