# QuestionAnswering
The Question-Answering layer contains one feature pointing to [token](token.md) identifiers with two annotation labels: Answer and Context, and is attached to a free-text Question layer. The annotators are asked, given a text, to find questions whose answers can be directly found in the given text.

### Answer and Context Labels 
The Answer laybel marks the shortest possible span of tokens for an answer to one or more questions. With the Context label a segment surrounding the Aswer segment is marked.

### Question Relations
The Question-Answering layer is attached to a relation layer called Question. The Question relation layer allows a free-text annotation containing the questions for the annotated answers. 

 
