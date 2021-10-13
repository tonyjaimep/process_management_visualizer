"""
Generates a tkinter window that illustrates the
way processes are managed by a ProcessManager
"""
from application import Application
from process import Process

if __name__ == "__main__":
    processes = [
        Process(),
        Process(),
        Process(),
        Process(),
        Process(),
        Process(),
    ]
    app = Application(processes)
    app.mainloop()
