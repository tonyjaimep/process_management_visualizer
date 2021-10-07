import tkinter as tk
from tkinter import ttk

BACKGROUND_COLOR = "#03000F"

BUTTON_BACKGROUND_MAP = [
    ("active", "#0A0A0F"),
    ("pressed", "#13101F")
]

BUTTON_BACKGROUND = "#13101F"
BUTTON_FOREGROUND = "#F0F0FF"

class Process:

    def __init__(self, delay):
        self.delay = delay


class Application(tk.Tk):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_widgets()
        self.init_styles()
        self.processes = []

    def init_styles(self):
        self["bg"] = BACKGROUND_COLOR
        self.style = ttk.Style(self)
        self.style.configure(
                "TButton",
                background=BUTTON_BACKGROUND,
                foreground=BUTTON_FOREGROUND,
                relief=tk.FLAT,
                )
        self.style.map(
                "C.TButton",
                background=BUTTON_BACKGROUND_MAP,
                )

    def create_widgets(self):
        self.canvas = Canvas(processes=[], master=self)
        self.controls = Controls(
                master=self,
                play_handler=self.play_visualization,
                stop_handler=self.stop_visualization,
                quit_handler=self.quit_visualization,
                )
        # log_box should not be editable by user
        self.log_box = tk.Text(master=self, relief=tk.FLAT)

        self.canvas.grid(column=0, row=0, columnspan=3, rowspan=2)
        self.controls.grid(column=0, row=2, columnspan=2, rowspan=1)
        self.log_box.grid(column=2, row=2, columnspan=1, rowspan=1)

    def log(self, text):
        text_line = text if text.endswith("\n") else text + "\n"
        self.log_box.insert(tk.INSERT, text_line)

    def play_visualization(self):
        self.log("Playing visualization")

    def stop_visualization(self):
        self.log("Stopping visualization")

    def quit_visualization(self):
        self.log("Quitting visualization")
        self.quit()


class Controls(ttk.Frame):

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
        self.play_button.grid(column=0, row=0)

        self.stop_button = ttk.Button(
                self,
                text="Stop",
                command=stop_handler,
                style="C.TButton"
                )
        self.stop_button.grid(column=1, row=0)

        self.quit_button = ttk.Button(
                self,
                text="Quit",
                command=quit_handler,
                style="C.TButton",
                )
        self.quit_button.grid(column=2, row=0)


class Canvas(tk.Canvas):

    def __init__(self, processes, **kwargs):
        super().__init__(**kwargs)
        self.processes = processes

