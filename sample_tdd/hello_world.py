class HelloWorld:

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    def __init__(self, message: str = None):
        self.__message = message

    def say(self):
        print(self.__message)
