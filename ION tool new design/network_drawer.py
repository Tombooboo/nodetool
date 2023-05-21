import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def draw_network(nodes, edges, canvas):
    G = nx.Graph()

    # Extract the node names or identifiers from the Node objects
    node_names = [node.name for node in nodes]

    G.add_nodes_from(node_names)
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

    labels = {node: node for node in G.nodes}
    nx.draw_networkx_labels(G, pos, labels, font_size=12)

    plt.axis('off')

    # Create the root window
    root = tk.Tk()

    # Retrieve the position of the current window
    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()

    # Set the initial size and position of the window
    root.geometry(f"800x600+{x}+{y}")  # Set your desired width and height

    # Create a Matplotlib Figure and attach it to the canvas
    fig = plt.gcf()
    figure_canvas = FigureCanvasTkAgg(fig, master=root)
    figure_canvas.draw()

    # Get the Tkinter Canvas widget and pack it with fixed size and no expansion
    canvas_widget = figure_canvas.get_tk_widget()
    canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

    # Update the canvas
    canvas.update()

    # Start the Tkinter event loop
    root.mainloop()
