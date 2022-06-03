# Credibilty
## Credibility Layer and Pipeline: Credibility
The credibility layer points to [segment](segment.md) identifiers, whereby full tweets are annotated (*document-based annotation*).
Credibility annotations are the last step in the topic-focused credibility annotation pipeline: 

(1)  [Informativeness](info.md) - (2) [Topics](topic.md) - **(3) [Credibility](credibility.md)**.  

It marks single segments as having either `high` or `low` credibility. If `None` was selected for either [Informativeness](info.md) or [Topic-related annotation](topic.md), the tweet is excluded for subsequent annotation steps (select `Excluded`). Credibility is only annotated for Tweets.

## Credibility Definition
Following the definitions of Navok et al. and Gupta et al. we define credibility as the property of being trusted, i.e. a text is declared credible if a user, e.g. based on common sense, believes that the information it contains is to some extent credible [3,4]. 
Based on the hypothesis in Castillo et al., that there are signals available in the social media environment itself that enable users to assess information credibility, we explore the credibility only based on the information the content of a post is giving. In contrast to Castillo et al., we anonymize the users’ names to avoid gender and other biases that distract the annotators from the content.

For the annotations, we follow a three-step approach, including a [Informativeness](info.md) and [Topic-related annotation](topic.md) step. Only if the prior two steps were NOT annotated as `None` or `Excluded` the annotator needs to decide if the tweet’s content seems to be credible. Othewise, the tweets is excluded choosing the tag *Excluded*. We present the annotator one tweet per annotation.



## Credibility Annotations

*Based on the [topic](topic.md) of the tweet, do you believe that the information it contains is to some extent credible?*

**(1) High credibility**  
The tweet and its content seems to be to some extent credible.

**(2) Low credibility** 
The tweet and its content seems to be non-credible and it is highly questionable whether it can be trusted.  

**(3) None**
Based on the tweet, it is not possible to decide if the content is credible or not.

**(4) Excluded (skip tweet)**  
Based on prior decisions on the [Informativeness](info.md) or [Topic-related annotation](topic.md) (annotated as `None`), the tweet got excluded for further annoattions in the Credibility layer. 

---
#### Literature
Castillo, Carlos & Mendoza, Marcelo & Poblete, Barbara. (2011). Information credibility on Twitter. Proceedings of the 20th International Conference on World Wide Web. 675-684. 10.1145/1963405.1963500.
 
Nakov P, Mihaylova T, M`arquez L, Shiroya Y, Koychev I. Do Not Trust the Trolls: Predicting Credibility in Community Question Answering Forums. In: Proceedings of the International Conference Recent Advances in Natural Language Processing, RANLP 2017. Varna, Bulgaria: INCOMA Ltd.; 2017. p. 551-60. Available from: https://doi.org/10.26615/978-954-452-049-6 072.

Gupta A, Kumaraguru P, Castillo C, Meier P. In: Aiello LM, McFarland D, editors. TweetCred: Real-Time Credibility Assessment of Content on Twitter. Cham: Springer International Publishing; 2014. p. 228-43. Available from: https://doi.org/10.1007/978-3-319-13734-616
