# Topics
## Credibility Layer and Pipeline: Topics
The credibility layer points to [segment](segment.md) identifiers, whereby full tweets are annotated (*document-based annotation*).
Topic annotations are the second step in the topic-focused credibility annotation pipeline and prior to the actual credibility annotations: 

(1)  [Informativeness](info.md) - **(2) [Topics](topic.md)** - (3) [Credibility](credibility.md).  

It marks single segments as containing one of the covid-related topics listed below. If `None` was selected for [Informativeness](info.md), the tweet is excluded for subsequent annotation steps (select `Excluded`).
Topics are only annotated for Tweets.


## Topic Annotations

*Please choose, which of the covid-19-related aspects are covered by the tweet.*

**(1) The origin of the virus; its sources;**

**(2) Ways of mitigating the risk of infection;**

**(3) Measures and decisions by the federal government and its impact on people, countries, and the economy;**

**(4) Consequences of a Covid infection (long-covid, psychological aspects, etc.);**

**(5) Vaccination: general information about the vaccine, availability, side-effects;**

**(6) Treatments of an infection;**

**(7) Case reports/statistics;**

**(8) None;**  
The tweet is not about any of the above topics, or it is unclear what topic is, e.g. because the context is missing or because the content only indicates what it is about. The tweet is excluded for the next annotation step.

**(9) Excluded (skip tweet)**  
Choose `Excluded`, if the tweet was annotated as `None` for [informativeness](info.md) and therefore excluded for further annotation steps.