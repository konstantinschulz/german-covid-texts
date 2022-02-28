# Question Answering
The Question Answering layer contains one feature pointing to [token](token.md) identifiers with two annotation labels: Answer and Context, and is attached to a free-text Question layer. The annotators are asked, given a text, to find questions whose answers can be directly found in the given text.

### Answer and Context Labels 
The Answer label marks the shortest possible span of tokens for an answer to one or more questions. With the Context label a span surrounding the Answer span is marked.

### Question Relations
The Question Answering layer is attached to a relation layer called Question. The Question relation layer allows a free-text annotation containing the questions for the annotated answers.

## Contexts
The context layer points to [segment](./segment.md) identifiers. It marks multiple segments as containing contextually relevant content for a [question-answer](./question_answering.md) pair. 
### Beginning and End
The beginning and the end of a context must coincide with sentence boundaries.
### Length
A context should consist of at least 20 and at most 200 words.
### Position of Answer
The position of the answers with their associated context must vary systematically: Sometimes, the answer will be at the beginning of the context, sometimes in the end, sometimes in the middle.
#### Randomization
The exact answer position in a concrete case is to be chosen randomly. This choice will not be part of the [inter-annotator agreement](../inter_annotator_agreement.md).

 
