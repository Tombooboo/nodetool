import tkinter as tk

class GraphDrawer(tk.Frame):
    def __init__(self, parent, nodes, edges, width, height):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack()
        self.draw_network(nodes, edges)

    def draw_network(self, nodes, edges):
        for node in nodes:
            self.canvas.create_oval(node.x, node.y, node.x+30, node.y+30, fill="lightblue", outline="black")

        for edge in edges:
            start_x, start_y = edge.start.x+15, edge.start.y+15
            end_x, end_y = edge.end.x+15, edge.end.y+15
            self.canvas.create_line(start_x, start_y, end_x, end_y, fill="black", width=2)
