import tkinter as tk
from node_manager import NodeManager
from main_window import MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    node_manager = NodeManager()
    app = MainWindow(root, node_manager)
    app.pack(fill="both", expand=False)
    root.mainloop()
