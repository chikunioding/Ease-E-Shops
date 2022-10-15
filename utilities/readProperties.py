import configparser

config=configparser.RawConfigParser()
config.read(r"C:\Users\Mayur\PycharmProjects\Ease-E-Shops\Configurations\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get('common info','baseURl')
        return url

    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password
