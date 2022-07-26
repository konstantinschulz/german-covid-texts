# Events and Factuality Values Pipeline

An entity is a span of text that indicates a certain type of information. A text span can consist of one or more words. In Named Entity Recognition (NER), entities represent the information that the user wants to extract from the text.
We tag entities within our data (tweets) with the needed entities to express a meaningfull relation. The entity-relation-entity-tripple is called an event. With NER, the goal is to categorize and represent structured information taken from unstructured text.

Going one step further, we want to explor if events related to covid in twitter tweets express different qualities of being factual. In other words, are claims in tweets expressed as hypotheses, speculations, or opinions, rather than explicit facts (propositions)?

The factuality-based events annotation pipeline  includes three annotation layers in the following order:

(1) [Named Entities](entity.md), (2) [Relations](relations.md), (3) [Factuality](factuality.md)

---
## Literature

Kilicoglu H, Rosemblat G, Rindflesch TC. Assigning factuality values to semantic relations extracted from biomedical research literature. PLoS One. 2017 Jul 5;12(7):e0179926. doi: 10.1371/journal.pone.0179926. PMID: 28678823; PMCID: PMC5497973.