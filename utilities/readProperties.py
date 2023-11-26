import configparser


config = configparser.RawConfigParser()
config.read("C:\\Users\\UmeshKanojiya\\PycharmProjects\\DemoPytest\\Configuration\\config.ini")


class Readconfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password





