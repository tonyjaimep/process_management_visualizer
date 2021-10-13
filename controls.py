import tkinter as tk
from tkinter import ttk

class Controls(ttk.Frame):
    """
    Shows three control buttons, like so:
    ┌──────────┬──────────┬──────────┐
    │   Play   │   Stop   │   Quit   │
    └──────────┴──────────┴──────────┘
    """
    def __init__(self, play_handler, stop_handler, quit_handler, **kwargs):
        super().__init__(**kwargs)
        self.create_widgets(play_handler, stop_handler, quit_handler)

    def create_widgets(self, play_handler, stop_handler, quit_handler):
        self.play_button = ttk.Button(
            self,
            text="Play",
            command=play_handler,
            style="C.TButton",
        )
        self.play_button.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

        self.stop_button = ttk.Button(
            self, text="Stop", command=stop_handler, style="C.TButton"
        )
        self.stop_button.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

        self.quit_button = ttk.Button(
            self,
            text="Quit",
            command=quit_handler,
            style="C.TButton",
        )
        self.quit_button.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)
