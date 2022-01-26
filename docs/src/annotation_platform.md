# Annotation Platform
We use version 22.1 of the annotation tool [INCEpTION](https://inception-project.github.io/) (Klie et al., 2018), hosted on internal servers at [DFKI](https://www.dfki.de/). The annotation platform is password-protected, but all annotations will be made publicly available in this repository.
## Data Import
Inception is able to import plain text data from .txt files where each segment is on a new line and tokens are separated by a single whitespace.
## Data Export
### Data Format
Annotations are exported to XML files based on the [UIMA CAS XMI](https://uima.apache.org/d/uimaj-current/references.html#ugr.ref.xmi) specification.
### Standoff Annotations
Additional layers and their annotations are serialized in a standoff manner, i.e., with references to their respective base layer (such as IDs of tokens or segments).
## References
Klie, J.-C., Bugert, M., Boullosa, B., de Castilho, R. E., & Gurevych, I. (2018,
Juni). The INCEpTION Platform: Machine-Assisted and Knowledge-
Oriented Interactive Annotation. In Proceedings of the 27th International
Conference on Computational Linguistics: System Demonstrations (pp.
5–9). Santa Fe, New Mexico: Association for Computational Linguistics.
Retrieved from https://aclanthology.org/C18-2002
