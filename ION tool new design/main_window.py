import tkinter as tk
from tkinter import ttk, messagebox
from add_node_window import AddNodeWindow
from remove_node_window import RemoveNodeWindow
from modify_node_window import ModifyNodeWindow
from network_drawer import draw_network
from graph_drawer import GraphDrawer

class MainWindow(tk.Frame):
    def __init__(self, root, node_manager):
        super().__init__(root)
        self.root = root
        self.root.title("Node Tool")
        self.node_manager = node_manager

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.grid(row=1, column=0, sticky="nsew")
        self.buttons_frame.grid_columnconfigure(0, weight=1)

        self.draw_network_button = ttk.Button(self.buttons_frame, text="Draw Network", command=self.draw_network)
        self.draw_network_button.grid(row=0, column=0, padx=5, pady=5)

        self.add_node_button = ttk.Button(self.buttons_frame, text="Add Node", command=self.open_add_node_window)
        self.add_node_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.remove_node_button = ttk.Button(self.buttons_frame, text="Remove Node", command=self.open_remove_node_window)
        self.remove_node_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.modify_node_button = ttk.Button(self.buttons_frame, text="Modify Node", command=self.open_modify_node_window)
        self.modify_node_button.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        self.set_button_color("light blue")

    def set_button_color(self, color):
        style = ttk.Style()
        style.configure("TButton", background=color)

    def draw_network(self):
        nodes = self.node_manager.get_node_info()
        edges = self.node_manager.get_edges()
        draw_network(nodes, edges, self.canvas)
        if not nodes:
            self.display_error_window("No nodes found.")
            return
        self.canvas.delete("all")
        GraphDrawer(nodes, edges, self.canvas)

    def open_add_node_window(self):
        AddNodeWindow(self.root, self.node_manager)

    def open_remove_node_window(self):
        nodes = self.node_manager.get_node_info()
        if not nodes:
            self.display_error_window("No nodes found.")
            return
        RemoveNodeWindow(self.root, self.node_manager, nodes)

    def open_modify_node_window(self):
        nodes = self.node_manager.get_node_info()
        if not nodes:
            self.display_error_window("No nodes found.")
            return
        ModifyNodeWindow(self.root, self.node_manager, nodes)

    def display_error_window(self, message):
        messagebox.showerror("Error", message)


if __name__ == "__main__":
    node_manager = NodeManager()  # Replace with your NodeManager implementation
    root = tk.Tk()
    root.geometry("800x600")
    MainWindow(root, node_manager).pack(fill="both", expand=False)
    root.mainloop()
