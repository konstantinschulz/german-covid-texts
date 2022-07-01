# Named Entities
The named entity layer points to [token](token.md) identifiers. It marks spans of tokens as belonging to one of the 4 classes described in [OpeNER](https://www.opener-project.eu/getting-started/#named-entity-resolution):
- Person
- Location
- Organization
- Miscellaneous

Additionally, we add the following labels:

- Duration - an entity describing a time span, e.g. "Die verordnete Quarantänezeit beträgt **14 Tage**."  
- Time- an entity describing a point in time, e.g. "**Gestern** wurde die neue Verordnung verabschiedet." 
- Desease - for example "Der Verlauf von **Covid** war bei mir zunächst mild, das Fieber kam erst am folgenden Tag."
- Symptom - Symptoms of an Covid-19 deasease, e.g.  "Der Verlauf von Covid war bei mir zunächst mild, das **Fieber** kam erst am folgenden Tag."
- Measure - An entity describing a measure and decision by the federal governmenty related to Covid-19, e.g. "Die verordnete **Quarantänezeit** beträgt 14 Tage."  

Entity annotations are the last step in the topic-focused annotation pipeline: 

(1)  [Informativeness](informativeness.md) - (2) [Topics](topic.md) - **(3) [Named Entities](entity.md)**.  

Other layers that directly reference this layer:
- [Relations](relation.md)
## Unnamed Entities
Entities without a name are **not** annotated in this layer. This also applies to anonymized mentions (e.g., Twitter handles).
### Example
"generell kann man nie sagen **wer** schon vielleicht Antikörper hat"
## Coreference Resolution
Coreferences through pronouns or other pointers ("") are **not** resolved in this layer. Therefore, they do **not** get annotated as entities, due to our policy on Unnamed Entities.
### Example
50% meiner Bekannten **die** sich Impfen lassen haben und vorher kein Leiden hatten sind jetzt zum Teil Arbeitsunfähig und Krank
