# Credibilty

The credibility layer points to [segment](segment.md) identifiers, whereby full tweets are annotated (*document-based annotation*).
Credibility annotations are the last step in the topic-focused annotation pipeline:  

It marks single segments as having either `high` or `low` credibility. If `None` was selected for either [Informativeness](informativeness.md) or [Topic-related annotation](topic.md), the tweet is excluded for subsequent annotation steps (select `Excluded`). Credibility is only annotated for 

## Credibility Annotations

*Based on the [topic](topic.md) of the tweet, do you believe that the information it contains is to some extent credible?*

**(1) High credibility**  
The tweet and its content seems to be to some extent credible.

**(2) Low credibility** 
The tweet and its content seems to be non-credible and it is highly questionable whether it can be trusted.  

**(3) None**
Based on the tweet, it is not possible to decide if the content is credible or not.

**(4) Excluded (skip tweet)**  
Based on prior decisions on the [Informativeness](informativeness.md) or [Topic-related annotation](topic.md) (annotated as `None`), the tweet got excluded for further annoattions in the Credibility layer. 

