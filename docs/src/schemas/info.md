# Informativeness
## Credibility Layer and Pipeline: Informativeness
The credibility layer points to [segment](segment.md) identifiers, whereby full tweets are annotated (*document-based annotation*). 
Informativeness annotations are the first step in the topic-focused credibility annotation pipeline: 

**(1) [Informativeness](info.md)**  - (2) [Topics](topic.md)  - (3) [Credibility](credibility.md).  

It marks single segments as being ``related`` and ``containing covid-related information``. Informativeness is only annotated for tweets.

## Informativeness Definition
The annotations aim to exclude tweets that do not primarily provide covid-related information, e.g. because they are humorous or sarcastic comments or contain personal opinions or attacks. Tweets with vulgar or offensive langauge should also be excluded (`None`). If in doubt if the tweet is covid-related, select `Informative (Borderline)`, as the next annotation step involves a more fine-grained topic annotation.  
  

## Informativeness Annotations
*Do you consider that the tweet’s content containes information about one covid-19 (e.g., about the virus, governmental decisions, risk reduction, treatments, vaccinations, etc.)?*

**(1) Related and Informative**  
The tweet contains information about one aspect related to covid-19.

**(2) Informative (Borderline)**  
The tweet is informative and somewhat related (needs to be decided in the next annotation step). 

**(3) None**  
The tweet is not related to the covid-19. 
Or the tweet is related to covid-19 but does not contain any information, e.g. it is a personal statements (opinion) without an informative background, or if it is a humorous/sarcastic comment. 
Also select `None` if the tweet contains personal attacks or offensive language.


