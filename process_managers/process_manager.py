

class ProcessManager:
    def __init__(self, processes, logging_function=print):
        self.processes = processes
        self.log = logging_function

    def start(self):
        pass

    def _update(self):
        pass

    def stop(self):
        for process in self.processes:
            process.reset()
