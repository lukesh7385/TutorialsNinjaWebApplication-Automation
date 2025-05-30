import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_user_email():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_user_password():
        password = config.get('common info', 'password')
        return password
