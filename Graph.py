import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import plotly.graph_objs as go
import networkx as nx
import pandas as pd

init_notebook_mode(connected=True)

# G = nx.random_geometric_graph(200, 0.125)
G = nx.Graph()
df = pd.read_csv('C:\\Spring 22\\Network Security\\Project1\\AfterDoS.csv')
A = list(df["Source"].unique())
B = list(df["Destination"].unique())

node_list = set(A+B)

for i in node_list:
    G.add_node(i)
    
for i,j in df.iterrows():
    G.add_edges_from([(j["Source"],j["Destination"])])
    
pos = nx.random_layout(G)

for n, p in pos.items():
    G.nodes[n]['pos'] = p

# G = nx.from_pandas_edgelist(df, 'connection', 'node')

edge_trace = go.Scatter(
    x=[],
    y=[],
    line=dict(width=0.5,color='#2d2d2d'),
    hoverinfo='none',
    mode='lines')

for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_trace['x'] += tuple([x0, x1, None])
    edge_trace['y'] += tuple([y0, y1, None])
    
node_trace = go.Scatter(
    x=[],
    y=[],
    text=[],
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='RdBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=10,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line=dict(width=0)))

for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])
    
for node, adjacencies in enumerate(G.adjacency()):
    node_trace['marker']['color']+=tuple([len(adjacencies[1])])
    node_info = str(adjacencies[0])+' # of connections: '+str(len(adjacencies[1]))
    node_trace['text']+=tuple([node_info])
#     node_trace['marker']['size'] += tuple([5*G.nodes()[node]])


# for node, adjacencies in enumerate(G.adjacency()):
#     node_adjacencies.append(len(adjacencies[1]))
#     node_text.append('# of connections: '+str(len(adjacencies[1])))
    
fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Router Connections',
                titlefont=dict(size=16),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="No. of packets received",
                    showarrow=False,
                    xref="paper", yref="paper") ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

fig.show()
