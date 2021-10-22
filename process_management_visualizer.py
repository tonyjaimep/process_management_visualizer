"""
Generates a tkinter window that illustrates the
way processes are managed by a ProcessManager
"""
from application import Application
from process import Process

if __name__ == "__main__":
    processes = [
        Process(1, 0, "#0"),
        Process(1, 1, "#1"),
        Process(1, 1, "#2"),
        Process(1, 2, "#3"),
        Process(1, 4, "#4"),
    ]
    app = Application(processes)
    app.mainloop()
