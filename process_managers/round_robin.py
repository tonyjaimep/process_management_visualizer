import time
from random import randint
from queue import Queue
from operator import attrgetter
from threading import Thread
from process_managers.process_manager import ProcessManager

# updates per second
MIN_QUANTUM = 2
MAX_QUANTUM = 10


class RoundRobinProcessManager(ProcessManager):
    def __init__(self, processes, *args):
        super().__init__(processes, *args)
        self.process_queue = None
        self.start_time = None
        self.sorted_processes = sorted(processes, key=attrgetter("arrives_at"))
        self.management_thread = None
        self.current_process_index = None
        self.quantum = 1 / randint(MIN_QUANTUM, MAX_QUANTUM)

    def start(self):
        del self.process_queue
        self.process_queue = Queue()

        self.management_thread = Thread(target=self._loop)
        self.start_time = time.time()
        self.log("Starting process management thread")
        self.management_thread.start()

    def _loop(self):
        while self.start_time is not None:
            self._update()

    def stop(self):
        if self.management_thread is None:
            raise Exception("Cannot stop() a ProcessManager that has not been started.")

        super().stop()

        self.start_time = None
        self.current_process_index = None

        self.process_queue = None
        self.management_thread.join(0)
        del self.management_thread
        self.management_thread = None

    def _update(self):
        if self.start_time is None or self.process_queue is None:
            raise Exception(
                "Cannot _update() a ProcessManager that has not been started."
            )

        current_time = time.time()
        ellapsed_time = current_time - self.start_time

        # if there are processes yet to add to the queue
        if len(self.sorted_processes) > 0:
            if self.sorted_processes[0].arrives_at <= ellapsed_time:
                self.process_queue.put(self.sorted_processes.pop(0))
                if self.current_process_index is None:
                    self.current_process_index = 0

        if self.current_process_index is None:
            return

        # find next unfinished process to serve
        processes_yet_to_check = len(self.process_queue.queue)
        found_unfinished_process = False

        while processes_yet_to_check > 0 and not found_unfinished_process:
            self.current_process_index += 1
            self.current_process_index %= len(self.process_queue.queue)
            processes_yet_to_check -= 1

            if self.process_queue.queue[self.current_process_index].get_progress() < 1:
                found_unfinished_process = True

        # if found an unfinished process, serve that process for a quantum
        if found_unfinished_process:
            self.process_queue.queue[self.current_process_index].start()
            time.sleep(self.quantum)
            self.process_queue.queue[self.current_process_index].pause()
