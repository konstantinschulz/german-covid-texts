# Named Entities
The named entity layer points to [token](token.md) identifiers. It marks spans of tokens as belonging to one of the 4 classes described in [OpeNER](https://www.opener-project.eu/getting-started/#named-entity-resolution):
- Person
- Location
- Organization
- Miscellaneous

Other layers that directly reference this layer:
- [Relations](relation.md)
## Unnamed Entities
Entities without a name are **not** annotated in this layer.
### Example
"generell kann man nie sagen **wer** schon vielleicht Antikörper hat"
## Coreference Resolution
Coreferences through pronouns or other pointers ("") are **not** resolved in this layer. Therefore, they do **not** get annotated as entities, due to our policy on Unnamed Entities.
### Example
50% meiner Bekannten **die** sich Impfen lassen haben und vorher kein Leiden hatten sind jetzt zum Teil Arbeitsunfähig und Krank
