import logging

class Configure_Log:

    def __init__(self, Name):
        self.Name = Name

    def configure(self, Message):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=self.Name, level=10, filemode='a', format=Message, datefmt='%Y-%m-%d %H:%M:%S')