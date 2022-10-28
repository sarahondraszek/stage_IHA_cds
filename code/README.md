# Overview and Description of Usage of All Scripts Implemented and Stored in This Repository

## Scripts Categorised by Their Usage
The scripts in this repository serve different purposes whose backgrounds and motivations are explained in detail
in the [README](../README.md).
### Cleaning, Filtering and Merging
The scripts [merge_spreadsheets](merge_spreadsheets.ipynb) and [filtering_and_visualisation](filtering_and_visualisation.py)
implement functions for cleaning and merging the spreadsheets/CSV files of the correspondence. 
#### List of required modules:
* [Matplotlib](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
* [Pandas](https://pandas.pydata.org)

### Interactive Networks
The script [network_visualisation](network_visualisation.ipynb) can be used to visualise CSV files with information about nodes
and edges of a graph in an interactive environment. 
#### List of required modules:
* [Colour](https://pypi.org/project/colour/)
* [Dash](https://dash.plotly.com)
* [Networkx](https://networkx.org)
* [Pandas](https://pandas.pydata.org)
* [Plotly](https://plotly.com)
* [Textwrap](https://docs.python.org/fr/3/library/textwrap.html)

### Ontologies, RDFification, Semantic Modelling
The scripts [semantic_modelling_with_owlready](semantic_modelling_with_owlready.ipynb) [enriching_database](enriching_database.ipynb) 
and [interactive_RDF](interactive_RDF.ipynb) revolve around the topic of ontologies and the Semantic Web.
However, the last two are rather experimental – `enriching_database` is a framework that portrays how information
could be added to the data using SPARQL queries and `interactive_RDF` is the approach to the visualisation mentioned in the
last section of the [README](../README.md#interactive-visualisation-of-knowledge-graphs).

#### List of required modules:
* [Geocoder](https://geocoder.readthedocs.io)
* [Owlready2](https://owlready2.readthedocs.io/en/v0.37/)
* [Pandas](https://pandas.pydata.org)
