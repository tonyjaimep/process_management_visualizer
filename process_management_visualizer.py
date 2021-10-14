"""
Generates a tkinter window that illustrates the
way processes are managed by a ProcessManager
"""
from application import Application
from process import Process

if __name__ == "__main__":
    processes = [
        Process(3, 0, "#0"),
        Process(5, 1, "#1"),
        Process(2, 3, "#2"),
        Process(5, 9, "#3"),
        Process(5, 12, "#4"),
    ]
    app = Application(processes)
    app.mainloop()
