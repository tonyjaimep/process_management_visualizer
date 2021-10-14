"""
A Canvas is where processes are drawn/displayed
"""

import tkinter as tk

FPS = 30
GAP = 16
ACTIVE_PROCESS_FILL = "#2faf7d"
COMPLETED_PROCESS_FILL = "#2fdf9d"
INACTIVE_PROCESS_FILL = "#071610"


class Canvas(tk.Canvas):
    """
    Where processes are displayed
    """

    def __init__(self, processes, **kwargs):
        super().__init__(**kwargs)
        self.processes = processes
        self.process_count = len(processes)
        self.is_playing = False

    def play(self):
        """
        Resumes dynamic drawing
        """
        self.is_playing = True
        self.loop()

    def pause(self):
        """
        Pauses dynamic drawing
        """
        self.is_playing = False

    def loop(self):
        """
        Draws processes over and over
        """
        if self.is_playing:
            self.draw_processes()
            self.after(int((1 / FPS) * 1000), self.loop)

    def draw_processes(self):
        """
        Iterates through processes, representing their progress as their x-axis position
        """
        self.delete(tk.ALL)
        process_height = (
            (self.winfo_height() - (self.process_count + 1) * GAP) / self.process_count
            if self.process_count > 0
            else 0
        )
        process_index = 0
        for process in self.processes:
            process_progress = process.get_progress()
            process_progress = 1.0 if process_progress >= 1.0 else process_progress
            process_x = GAP + process_progress * (
                self.winfo_width() - GAP * 2 - process_height
            )
            process_y = GAP * (process_index + 1) + process_index * process_height
            self.create_rectangle(
                process_x,
                process_y,
                process_x + process_height,
                process_y + process_height,
                fill=(
                    COMPLETED_PROCESS_FILL
                    if process_progress >= 1.0
                    else (
                        ACTIVE_PROCESS_FILL
                        if process.get_progress() > 0
                        else INACTIVE_PROCESS_FILL
                    )
                ),
            )
            process_index += 1
