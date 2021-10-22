import tkinter as tk
from tkinter import ttk
from canvas import Canvas
from controls import Controls
from process_managers import RoundRobinProcessManager

BACKGROUND_COLOR = "#03000F"

BUTTON_BACKGROUND_MAP = [("active", "#0A0A0F"), ("pressed", "#13101F")]

BUTTON_BACKGROUND = "#03000F"
BUTTON_FOREGROUND = "#F0F0FF"


class Application(tk.Tk):
    """
    Controls how processes are managed and displays them in a tkinter canvas
    """

    def __init__(self, processes=[], **kwargs):
        super().__init__(**kwargs)
        self.process_manager = RoundRobinProcessManager(processes, self._log)

        self.canvas = Canvas(
            processes=self.process_manager.processes,
            master=self,
            relief=tk.FLAT,
        )
        self.controls_container = Controls(
            master=self,
            play_handler=self._play_visualization,
            stop_handler=self._stop_visualization,
            quit_handler=self._quit_visualization,
        )
        self.log_box_container = tk.Frame(self)
        self.log_box = tk.Text(
            master=self.log_box_container,
            relief=tk.FLAT,
            height=5,  # lines
            foreground="#FFFFFF",
        )
        self.log_box["bg"] = BACKGROUND_COLOR
        self._create_widgets()
        self._init_styles()

    def _init_styles(self):
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

    def _create_widgets(self):
        self._create_canvas()
        self._create_log_box()
        self._create_controls()

    def _log(self, text):
        text_line = text if text.endswith("\n") else text + "\n"
        self.log_box.insert("1.0", text_line)

    def _play_visualization(self):
        self._log("Playing visualization")
        self.canvas.play()
        self.process_manager.start()

    def _stop_visualization(self):
        self._log("Stopping visualization")
        self.canvas.pause()
        try:
            self.process_manager.stop()
        except:
            self._log("Cannot stop a visualization that has not started")

    def _quit_visualization(self):
        self._log("Quitting visualization")
        self.canvas.pause()
        try:
            self.process_manager.stop()
        except:
            pass
        self.quit()

    def _create_canvas(self):
        self.canvas["bg"] = BACKGROUND_COLOR
        self.canvas.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

    def _create_controls(self):
        self.controls_container.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

    def _create_log_box(self):
        self.log_box_container.pack(expand=False, side=tk.RIGHT)
        self.log_box.pack(expand=True, fill="both")
