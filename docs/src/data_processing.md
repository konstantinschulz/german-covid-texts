# Data Processing
## Text Extraction
Raw source data is processed using [Apache Tika](https://tika.apache.org/) to extract plain text from any given file format. 
## Normalization
Tabs and duplicate whitespaces are removed from the plain text using regular expressions.
## Segmentation & Tokenization
The plain text is segmented and tokenized using the [Natural Language Toolkit](https://www.nltk.org/).

Hashtags receive additional tokenization through [Wordninja](https://github.com/keredson/wordninja), which is basically a [Viterbi algorithm](https://en.wikipedia.org/wiki/Viterbi_algorithm) trained on the [German part of the Twitter data in WorldLex](http://worldlex.lexique.org/files/De.Freq.2.rar). This is particularly helpful for hashtags that are concatenations of multiple words (case-insensitive).

## GDPR
We address [§89 of the GDPR](https://gdpr-info.eu/art-89-gdpr/) by restricting the usage of this dataset to scientific purposes. In particular, we aim to collect and curate as little data as possible: Personal information in the texts (such as Twitter handles, or particularly sensitive hashtags) are either removed or pseudonymized. Our goal is that no single person can be unambiguously identified through the information present in our dataset.
