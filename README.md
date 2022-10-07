# Repository of code and data created during my internship at the IHA/DHI Paris.
## Introduction
This repository is a collection of all scripts used for (pre-)processing and visualising the data from the
Constance de Salm correspondence. It also includes the original data (CSV file) that was used plus almost 
all visualisations as demonstrative PNG or GIFs.

## Histograms of Correspondence Frequencies
Some visualisations that are included are histograms of correspondences throughout the decades. In lieu
of visualising them in Python, further steps were taken in Excel for better team-intern accessibility, readability
and reusability. The script mainly provides tools for filtering the data basis for Excel.
![Histogram of Correspondence Frequencies](data/vis/decades_freq.png)
This is a first try of visualising the correspondence frequencies (y-axis) throughout the decades (x-axis)
using [matplotlib](https://matplotlib.org/). Given the fact that the visualisation did not quite fit
the initial expectations plus the rather complicate handling, I decided to only use Python in this step to retrieve
the filtered data from the CSV and import it into Excel.
![Histogram in Excel](data/vis/histogram_freqs.png)
As can be seen in this visualisation, in Excel, I was able to filter the frequencies not only by decades but also by
the people with whom Constance de Salm corresponded. The visualisation is interactive due to Excel's integrated filtering tool
and can be read modified even without further technological expertise.
## Network of Constance de Salm's Correspondence.
Firstly, I wanted to create a network that allows a user to interact with it and that has filters that can be modified
and applied to the data. Pre-existing tool like Gephi or Cytoscape both do not include filtering techniques for graph data
so instead I chose to use a Python and Javascript framework to create a virtual server on which a HTML page is launched
that can be used by other people to explore the graph data.
The interactive network was created using the modules [Networkx](https://networkx.org/), [Plotly](https://plotly.com/python/) and [Dash](https://dash.plotly.com/).
Moreover, the script was inspired by the following Medium [article](https://towardsdatascience.com/python-interactive-network-visualization-using-networkx-plotly-and-dash-e44749161ed7)
and adjusted to my needs.
![Interactive Network](data/vis/graph_interactions.gif) 
Further information will be added following the example of Semantic Web graphs.
## Enriching the Network with Semantic Information
![](data/vis/g.png)
Visualisation of current OWL ontology in Protégé.
![](data/vis/ontograph.png)
Visualisation in Protégé.
![](data/vis/ontograph-1.png)
After importing the finished, in XML/RDF serialised OWL file into GraphDB, it is possible to visualise
the graph.
![](data/vis/rdf_cds_graph.gif)