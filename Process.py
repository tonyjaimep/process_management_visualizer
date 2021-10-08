#pip3 install thread6
import threading
import time


class Process:

    def __init__(self, name, delay):
        self.name = name
        self.delay = delay
        self.__create_thread()

    def __create_thread(self):
        try:
            self.thread = threading.Thread(target=self.__thread_process)
        except:
            print("ERROR: unable to start thread")


    def __thread_process(self):
        # example of process
        for i in range(5):
            print(f":{self.name} > {i+1}")
            time.sleep(self.delay)

    def work(self):
        self.thread.start()
        return f">{self.name}: process started"