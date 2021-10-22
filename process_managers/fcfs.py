import time
from queue import Queue
from operator import attrgetter
from threading import Thread

from process_managers.process_manager import ProcessManager

# updates per second
UPS = 60

class FCFSProcessManager(ProcessManager):
    def __init__(self, processes, *args):
        super().__init__(processes, *args)
        self.process_queue = None
        self.start_time = None
        self.sorted_processes = sorted(processes, key=attrgetter("arrives_at"))
        self.management_thread = None

    def start(self):
        del self.process_queue
        self.process_queue = Queue()

        for process in self.sorted_processes:
            self.process_queue.put(process)

        self.management_thread = Thread(target=self._loop)
        self.start_time = time.time()
        self.log("Starting process management thread")
        self.management_thread.start()

    def _loop(self):
        while self.start_time is not None:
            self._update()
            time.sleep(1 / UPS)

    def stop(self):
        if self.management_thread is None:
            raise Exception("Cannot stop() a ProcessManager that has not been started.")

        super().stop()

        self.start_time = None

        self.management_thread.join(0)
        del self.management_thread
        self.management_thread = None

    def _update(self):
        if self.start_time is None or self.process_queue is None:
            raise Exception(
                "Cannot update() a ProcessManager that has not been started."
            )

        if len(self.process_queue.queue) is 0:
            return

        current_time = time.time()
        ellapsed_time = current_time - self.start_time
        current_process = self.process_queue.queue[0]

        if not current_process.is_active:
            if current_process.arrives_at <= ellapsed_time:
                current_process.start()
                self.log(
                    "Starting process %s after %d seconds"
                    % (
                        current_process.id,
                        current_time - self.start_time,
                    )
                )
        elif current_process.get_progress() >= 1.0:
            self.process_queue.get()
            self.log(
                "Process %s finished at %d seconds,"
                " after running for %d seconds"
                % (
                    current_process.id,
                    ellapsed_time,
                    current_process.time_dedicated_to_self,
                )
            )
