import time
import random
import string

class Process:

    def __init__(self, time_to_complete, arrives_at=0, identifier=None):
        # 0.0 = none, 1.0 = complete
        self.time_to_complete = time_to_complete
        self.arrives_at = arrives_at
        self.started_running_at = None
        self.id = identifier
        # random identifier if none is provided
        if identifier is None:
            self.id = "".join(random.choice(string.ascii_lowercase) for i in range(3))
        else:
            self.id = identifier

    def reset(self):
        self.started_running_at = None

    def start(self):
        self.started_running_at = time.time()

    def get_progress(self):
        if self.started_running_at is None:
            return 0

        time_dedicated_to_self = time.time() - self.started_running_at
        progress = time_dedicated_to_self / self.time_to_complete

        return progress
