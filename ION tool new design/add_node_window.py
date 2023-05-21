import tkinter as tk
from tkinter import ttk

class AddNodeWindow(tk.Toplevel):
    def __init__(self, root, node_manager):
        super().__init__(root)
        self.root = root
        self.node_manager = node_manager
        self.title("Add Node")

        self.name_label = ttk.Label(self, text="Name:")
        self.name_label.pack()
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack()

        self.ip_label = ttk.Label(self, text="IP Address:")
        self.ip_label.pack()
        self.ip_entry = ttk.Entry(self)
        self.ip_entry.pack()

        self.add_button = ttk.Button(self, text="Add", command=self.add_node)
        self.add_button.pack()

    def add_node(self):
        name = self.name_entry.get()
        ip = self.ip_entry.get()

        if name and ip:
            self.node_manager.add_node(name, ip)
            self.destroy()  # Close the window after adding the node
