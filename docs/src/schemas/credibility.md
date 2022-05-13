# Credibility
The credibility layer points to [token](token.md) identifiers. It marks spans of tokens as having either `high` or `low` credibility. Credibility is only annotated for Tweets.

Following the definitions of Navok et al. and Gupta et al. we define credibility as the property of being trusted, i.e. a text is declared credible if a user, e.g. based on common sense, believes that the information it contains is to some extent credible [3,4]. 
Based on the hypothesis in Castillo et al., that there are signals available in the social media environment itself that enable users to assess information credibility, we explore the credibility only based on the information the content of a post is giving. In contrast to Castillo et al., we anonymize the users’ names to avoid gender and other biases that distract the annotators from the content.
For the annotations, we follow a two-step approach, including a [topic-related annotation](topic.md) and, as a second step, if the tweet’s content seems to be credible to the annotator. We present the annotator one tweet.

Based on the [topic](topic.md) of the tweet, do you believe that the information it contains is to some extent credible?
- R1 High credibility 
- R2 Low credibility
- R3 None of the above (skip tweet)

Castillo, Carlos & Mendoza, Marcelo & Poblete, Barbara. (2011). Information credibility on Twitter. Proceedings of the 20th International Conference on World Wide Web. 675-684. 10.1145/1963405.1963500.
 
Nakov P, Mihaylova T, M`arquez L, Shiroya Y, Koychev I. Do Not Trust the Trolls: Predicting Credibility in Community Question Answering Forums. In: Proceedings of the International Conference Recent Advances in Natural Language Processing, RANLP 2017. Varna, Bulgaria: INCOMA Ltd.; 2017. p. 551-60. Available from: https://doi.org/10.26615/978-954-452-049-6 072.

Gupta A, Kumaraguru P, Castillo C, Meier P. In: Aiello LM, McFarland D, editors. TweetCred: Real-Time Credibility Assessment of Content on Twitter. Cham: Springer International Publishing; 2014. p. 228-43. Available from: https://doi.org/10.1007/978-3-319-13734-616
