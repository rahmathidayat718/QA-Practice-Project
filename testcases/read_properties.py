import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_url_login():
        url = config.get('user login info', 'url_login')
        return url

    @staticmethod
    def get_email():
        email = config.get('user login info', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('user login info', 'password')
        return password

    @staticmethod
    def get_login_title():
        login_title = config.get('user login info', 'login_title')
        return login_title