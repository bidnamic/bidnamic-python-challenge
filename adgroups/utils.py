# create class for threading functions to fast tract loading of data to database

import threading

class LoadThread(threading.Thread):
    # each instance of thread runs for each data that is to be loaded into database

    def __init__(self, data):
        self.data= data
        threading.Thread.__init__(self)

    def run(self):
        self.data

class Load:
    @staticmethod
    def load_data(data):
        info= data
        LoadThread(info).start()
