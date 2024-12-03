import configparser

class Read_Config:
    config = configparser.ConfigParser()
    try:
        config.read(".\\data\\login.ini")
        print("Config loaded successfully:", config.sections())  # Debugging
    except Exception as e:
        print("Error loading config file:", e)

    @staticmethod
    def get_login_url_page():
        return Read_Config.config.get("settings", "login_url_page", fallback=None)

    @staticmethod
    def get_login_ecommerce_data():
        login_data = []
        for section in Read_Config.config.sections():
            if "login" in section:
                email = Read_Config.config.get(section, 'email', fallback=None)
                password = Read_Config.config.get(section, 'password', fallback=None)
                exp_result = Read_Config.config.get(section, 'exp_result', fallback=None)
                if email is not None and password is not None and exp_result is not None:
                    login_data.append((email, password, exp_result, section))
                else:
                    print(f"Invalid data in section {section}: email={email}, password={password}, exp_result={exp_result}")
        print(f"Login data loaded: {login_data}")  # Debugging
        return login_data