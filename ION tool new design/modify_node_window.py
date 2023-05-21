import tkinter as tk
from tkinter import ttk, messagebox

class ModifyNodeWindow(tk.Toplevel):
    def __init__(self, root, node_manager, nodes):
        super().__init__(root)
        self.root = root
        self.node_manager = node_manager
        self.nodes = nodes

        label_name = tk.Label(self, text="Current Name:")
        label_name.pack(pady=5)
        self.entry_name = tk.Entry(self)
        self.entry_name.pack(pady=5)

        label_new_name = tk.Label(self, text="New Name:")
        label_new_name.pack(pady=5)
        self.entry_new_name = tk.Entry(self)
        self.entry_new_name.pack(pady=5)

        label_ip = tk.Label(self, text="New IP Address:")
        label_ip.pack(pady=5)
        self.entry_ip = tk.Entry(self)
        self.entry_ip.pack(pady=5)

        button_modify = tk.Button(self, text="Modify", command=self.modify_node)
        button_modify.pack(pady=10)

    def modify_node(self):
        name = self.entry_name.get()
        new_name = self.entry_new_name.get()
        new_ip = self.entry_ip.get()
        self.node_manager.modify_node(name, new_name, new_ip)
        self.node_manager.print_nodes()
        self.destroy()
