import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

# Add nodes to graph
nodes = [
    "start",
    "SportsComplex",
    "Siwaka",
    "Ph.1A",
    "Ph.1B",
    "Phase2",
    "J1",
    "Mada",
    "STC",
    "Phase3",
    "Parking Lot",
]
G.add_nodes_from(nodes)

# Position the nodes accordingly
G.nodes["start"]["pos"] = [-1, 0]
G.nodes["SportsComplex"]["pos"] = (0, 0)
G.nodes["Siwaka"]["pos"] = (2, 0)
G.nodes["Ph.1A"]["pos"] = (4, 0)
G.nodes["Ph.1B"]["pos"] = (4, -2)
G.nodes["Phase2"]["pos"] = (6, -2)
G.nodes["J1"]["pos"] = (8, -2)
G.nodes["Mada"]["pos"] = (10, -2)
G.nodes["STC"]["pos"] = (4, -4)
G.nodes["Phase3"]["pos"] = (8, -4)
G.nodes["Parking Lot"]["pos"] = (8, -6)

node_pos = nx.get_node_attributes(G, "pos")

# Add edges to graph
straight_edges = [
    ("start", "SportsComplex"),
    ("SportsComplex", "Siwaka", {"weight": 450, "name": "UnkRoad"}),
    ("Siwaka", "Ph.1A", {"weight": 10, "name": "SangaleRd"}),
    ("Ph.1A", "Ph.1B", {"weight": 100, "name": "ParkingWalkWay"}),
    ("Ph.1B", "Phase2", {"weight": 112, "name": "KeriRd"}),
    ("Ph.1B", "STC", {"weight": 50, "name": "KeriRd"}),
    ("Phase2", "J1", {"weight": 600, "name": "KeriRd"}),
    ("J1", "Mada", {"weight": 200, "name": "SangaleRd"}),
    ("STC", "Parking Lot", {"weight": 250, "name": "LibraryWalkWay"}),
    ("Phase3", "Parking Lot", {"weight": 450, "name": "HimaGardensRd"}),
]

G.add_edges_from(straight_edges)

curved_out_edges = [
    ("Ph.1A", "Mada", {"weight": 850, "name": "SangaleRd"}),
    ("Mada", "Parking Lot", {"weight": 700, "name": "langataRd"}),
    ("Phase2", "Phase3", {"weight": 500, "name": "KeriRd"}),
    ("Phase2", "STC", {"weight": 50, "name": "STCwalkway"}),
]

G.add_edges_from(curved_out_edges)

curved_in_edges = [
    ("Siwaka", "Ph.1B", {"weight": 230, "name": "SangaleLink"}),
]
G.add_edges_from(curved_in_edges)

ax = plt.gca()
for edge in curved_out_edges:
    ax.annotate(
        "",
        xy=node_pos[edge[0]],
        xycoords="data",
        xytext=node_pos[edge[1]],
        textcoords="data",
        arrowprops=dict(
            arrowstyle="-",
            color="0.5",
            shrinkA=5,
            shrinkB=5,
            patchA=None,
            patchB=None,
            connectionstyle="arc3,rad=0.3",
        ),
    )

for edge in curved_in_edges:
    ax.annotate(
        "",
        xy=node_pos[edge[0]],
        xycoords="data",
        xytext=node_pos[edge[1]],
        textcoords="data",
        arrowprops=dict(
            arrowstyle="-",
            color="0.5",
            shrinkA=5,
            shrinkB=5,
            patchA=None,
            patchB=None,
            connectionstyle="arc3,rad=-0.3",
        ),
    )

path_names = nx.get_edge_attributes(G, "name")

nx.draw_networkx(G, node_pos, node_size=300, edgelist=straight_edges)
# nx.draw_networkx_edge_labels(
#     G, node_pos, edge_labels=path_names, verticalalignment="bottom"
# )


plt.axis("off")
plt.show()
