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
## Enriching the Network with Semantic Information.
To visualise a correspondence – an already existing corpus of connections between people who communicated with each other –
in an ontology, can come with many advantages. Not only does Linked (Open) Data make data more findable, accessible, interoperable
and reusable, it also brings the entire basis into a new context. Thereby, pre-existing statements, for example those about exchanged
letters of Constance de Salm, can be seen from a new point of view. More information about people, their relationships,
the places of expositions or the keywords used in the letters can be added.

### *First steps*
The first step of transforming this data basis into an ontology is to find and/or create a model
that fits the data and represents the wanted information. In the Semantic Web, one of the main goals is the enrichment
of data collections with "richer" information, meaning to enhance its expressiveness. Semantics or ``knowledge`` make such 
bases not only more accessible to humans but also more interoperable on the web.
Thinking of a model can be hard: Finding a fitting format, like RDF, or finding the best vocabulary to express what 
we want to say. Hence, it can be useful to model some examples by hand. It is also absolutely necessary to *know* the data.
![](data/vis/g.png)
Here, I tried to model what I want the CdS ontology to look like. Using Lucidchart provided me with a first idea of
what statements might be in the graph and what datatypes could be necessary.
![](data/vis/ontograph.png)
These were the first tries of modelling all information in aan OWL ontology in Protégé.
![](data/vis/ontograph-1.png)
After importing the finished, in XML/RDF serialised OWL file into GraphDB, it is possible to visualise
the graph.
![](data/vis/rdf_cds_graph.gif)