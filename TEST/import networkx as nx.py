import networkx as nx
import plotly.graph_objects as go
import random

# Create an empty graph
G = nx.Graph()

# Add central nodes
central_nodes = list(range(1, 11))
G.add_nodes_from(central_nodes)

# Connect central nodes
for i in range(1, 10):
    for j in range(i+1, 11):
        G.add_edge(i, j)

# Add secondary nodes
secondary_nodes = list(range(11, 31))
G.add_nodes_from(secondary_nodes)

# Connect secondary nodes to central nodes
for central_node in central_nodes:
    for secondary_node in secondary_nodes:
        # Connect each secondary node to at most 3 central nodes
        if G.degree(secondary_node) < 3:
            G.add_edge(central_node, secondary_node)

# Add additional nodes
additional_nodes = list(range(31, 101))
G.add_nodes_from(additional_nodes)

# Connect additional nodes to central or secondary nodes
for additional_node in additional_nodes:
    # Connect each additional node to at most 3 central or secondary nodes
    while G.degree(additional_node) < 3:
        random_node = random.choice(list(G.nodes()))
        if G.degree(random_node) < 3:
            G.add_edge(random_node, additional_node)

# Create Plotly figure
fig = go.Figure()

# Add nodes
pos = nx.spring_layout(G)  # Compute node positions
for node in G.nodes():
    x, y = pos[node]
    fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers', marker=dict(size=10, color='skyblue'), text=str(node)))

# Add edges
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(color='gray', width=1)))

# Update layout
fig.update_layout(title='Interactive Graph', showlegend=False, hovermode='closest')

# Show plot
fig.show()
