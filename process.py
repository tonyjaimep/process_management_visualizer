

class Process:
    def __init__(self):
        # 0.0 = none, 1.0 = complete
        self.progress = 0.0

    def reset(self):
        self.progress = 0.0
