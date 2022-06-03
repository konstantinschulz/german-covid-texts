# Data Processing
## Text Extraction
Raw source data is processed using [Apache Tika](https://tika.apache.org/) to extract plain text from any given file format. 
## Normalization
Tabs and duplicate whitespaces are removed from the plain text using regular expressions.
## Segmentation & Tokenization
The plain text is segmented and tokenized using the [Natural Language Toolkit](https://www.nltk.org/).