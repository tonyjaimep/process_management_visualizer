import time
import random
import string


class Process:
    def __init__(self, time_to_complete, arrives_at=0, identifier=None):
        # 0.0 = none, 1.0 = complete
        self.time_to_complete = time_to_complete
        self.arrives_at = arrives_at
        self.resumed_at = None
        self.id = identifier
        self.is_active = False
        self.time_dedicated_to_self = 0
        # random identifier if none is provided
        if identifier is None:
            self.id = self.make_random_id()
        else:
            self.id = identifier

    def make_random_id(self):
        return "".join(random.choice(string.ascii_lowercase) for _ in range(3))

    def reset(self):
        self.is_active = False
        self.resumed_at = None
        self.time_dedicated_to_self = 0

    def start(self):
        self.is_active = True
        self.resumed_at = time.time()

    def pause(self):
        if self.resumed_at is None:
            raise Exception("Cannot pause a Process that has not been started.")

        self.is_active = False
        self.time_dedicated_to_self += time.time() - self.resumed_at

    def get_progress(self):
        total_running_time = self.time_dedicated_to_self

        if self.is_active and self.resumed_at is not None:
            total_running_time += time.time() - self.resumed_at

        return total_running_time / self.time_to_complete
