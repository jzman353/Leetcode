import pandas as pd
import numpy as np
from webcolors import hex_to_rgb
# %matplotlib inline

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objects as go  # Import the graphical object

#node_label = ["A1", "A2", "B1", "B2", "B3", "C1", "C2"]
node_label = ["E-commerce North America", "E-commerce International", "AWS Cloud", "Revenue", "Cost of Sales", "Gross Profit", "Operating Profit", "Operating Expenses", "AWS Cloud profit", "E-commerce North America Profit", 'E-commerce International Profit', 'Fulfilment', 'Tech & Content', 'sales & Marketing', 'General & admin']
node_dict = {y: x for x, y in enumerate(node_label)}
#node_color = ['#F94144', '#F3722C', '#F8961E', '#F9C74F', '#5a5a5a', '#43AA8B', '#577590', '#5a5a5a', '#F8961E', '#5a5a5a', '#5a5a5a', '#5a5a5a', '#5a5a5a', '#5a5a5a', '#5a5a5a']
node_color = ['#F8961E', '#F8961E', '#F8961E', '#F8961E', '#5a5a5a', '#F8961E', '#F8961E', '#5a5a5a', '#F8961E', '#5a5a5a', '#5a5a5a', '#5a5a5a', '#5a5a5a', '#5a5a5a', '#5a5a5a']
node_label_color = {x:y for x, y in zip(node_label, node_color)}

"""source = ['A1', 'A1', 'A1', 'A2', 'A2', 'A2', 'B1', 'B2', 'B2', 'B3', 'B3']
target = ['B1', 'B2', 'B3', 'B1', 'B2', 'B3', 'C1', 'C1', 'C2', 'C1', 'C2']"""
source = ['E-commerce North America', 'E-commerce International', 'AWS Cloud', 'Revenue', 'Revenue', 'Gross Profit', 'Gross Profit', "Operating Expenses", "Operating Expenses", "Operating Expenses", "Operating Expenses", 'Operating Profit', 'Operating Profit', 'Operating Profit']
target = ['Revenue', 'Revenue', 'Revenue', 'Cost of Sales', 'Gross Profit', 'Operating Profit', "Operating Expenses", 'Fulfilment', 'Tech & Content', 'sales & Marketing', 'General & admin', 'AWS Cloud profit', "E-commerce North America Profit", 'E-commerce International Profit']
values = [315.880, 118.007, 80.096, 288.831, 225.152, 12.248, 212.904, 84.299, 73.213, 42.238, 11.891, 22.841, 2.847, 7.746]
source_node = [node_dict[x] for x in source]
target_node = [node_dict[x] for x in target]
link_color = [node_label_color[x] for x in target]

link_color = ['rgba({},{},{}, 0.4)'.format(
    hex_to_rgb(x)[0],
    hex_to_rgb(x)[1],
    hex_to_rgb(x)[2]) for x in link_color]

fig = go.Figure(
    data=[go.Sankey(  # The plot we are interest
        # This part is for the node information
        node=dict(
            label=node_label,
            color=node_color
        ),
        # This part is for the link information
        link=dict(
            source=source_node,
            target=target_node,
            value=values,
            color=link_color,
        ))])

# With this save the plots
plot(fig,
     image_filename='sankey_plot_1',
     image='png',
     image_width=1000,
     image_height=600
     )
# And shows the plot
fig.show()

#In Billions:
#Revenue: 513.983, North America E-commerce 315.880, International E-commerce 118.007, AWS 80.096
#Operating Profit: 12.248
#Gross Profit: 225.152
#Operating Income (Loss), North America E-commerce $ (2.847), International E-commerce (7.746), AWS 22.841
#Operating Expenses Cost of sales $ 288.831, Fulfillment 84.299,Technology and content 73.213, Sales and marketing 42.238, General and administrative 11.891, Other operating expense (income), net 1.263, total 501.735  (no sales is 212.904)

#In Millions:
#Revenue: 513,983, North America E-commerce 315,880, International E-commerce 118,007, AWS 80,096
#Operating Profit: 12,248
#Gross Profit = Revenue - cost of sales = 513,983-288,831=225152
#Operating Income (Loss), North America E-commerce $ (2,847), International E-commerce (7,746), AWS 22,841
#Operating Expenses Cost of sales $ 288,831, Fulfillment 84,299,Technology and content 73,213, Sales and marketing 42,238, General and administrative 11,891, Other operating expense (income), net 1,263, total 501735


#Gross Profit: 67,640
#Operating Expense: 55,392
