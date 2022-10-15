import configparser

config=configparser.RawConfigParser()
config.read(r"C:\Users\Mayur\PycharmProjects\Ease-E-Shops\Configurations\config1.ini")

class ReadConfig1:
    @staticmethod
    def getApplicationUrl():
        url=config.get('common information','baseurl')
        return url

    @staticmethod
    def getUsername():
        username=config.get('common information','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common information','password')
        return password