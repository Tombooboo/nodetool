import tkinter as tk
from tkinter import ttk, messagebox

class RemoveNodeWindow(tk.Toplevel):
    def __init__(self, root, node_manager, nodes):
        super().__init__(root)
        self.root = root
        self.node_manager = node_manager
        self.nodes = nodes

        label_name = tk.Label(self, text="Name:")
        label_name.pack(pady=5)
        self.entry_name = tk.Entry(self)
        self.entry_name.pack(pady=5)

        button_remove = tk.Button(self, text="Remove", command=self.remove_node)
        button_remove.pack(pady=10)

    def remove_node(self):
        name = self.entry_name.get()
        self.node_manager.remove_node(name)
        self.node_manager.print_nodes()
        self.destroy()
