# Contexts
The context layer points to [segment](./segment.md) identifiers. It marks multiple segments as containing contextually relevant content for a [question](./question.md)-[answer](./answer.md) pair. 
## Beginning and End
The beginning and the end of a context must coincide with sentence boundaries.
## Length
A context should consist of at least 20 and at most 200 words.
## Position of Answer
The position of the answers with their associated context must vary systematically: Sometimes, the answer will be at the beginning of the context, sometimes in the end, sometimes in the middle.
### Randomization
The exact answer position in a concrete case is to be chosen randomly. This choice will not be part of the [inter-annotator agreement](../inter_annotator_agreement.md).
