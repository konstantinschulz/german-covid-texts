# Named Entities
The named entity layer points to [token](../span_types/token.md) identifiers. It marks spans of tokens as belonging to one of the following classes described in [ACE annotation guidelines](https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-entities-guidelines-v6.6.pdf):

- **Person** - Person entities are limited to humans. A person may be a single individual or a group.
- **Location** - Location entities are limited to geographical entities such as geographical areas and landmasses, bodies of water, and geological formations. They also include Geo-political entities are geographical regions defined by political and/or social groups (nations, regions).
- **Organization** - Organization entities are limited to corporations, agencies, and other groups of people defined by an established organizational structure

We modified the ACE classes by joining Location and geo-political entities into one class, and only include the top-classes.

Additionally, we add the following labels:

- **Duration** - an entity describing a time span, e.g. "Die verordnete Quarantänezeit beträgt **14 Tage**."  
- **Time** - an entity describing a point in time, e.g. "**Gestern** wurde die neue Verordnung verabschiedet." 
- Desease - for example "Der Verlauf von **Covid** war bei mir zunächst mild, das Fieber kam erst am folgenden Tag."
- **Symptom** - Symptoms of a deasease (Covid or other) or resulting from side effects of a medicine/vaccine, e.g.  "Der Verlauf von Covid war bei mir zunächst mild, das **Fieber** kam erst am folgenden Tag."
- **Measure** - An entity describing a measure and decision by the federal governmenty related to Covid-19, e.g. "Die verordnete **Quarantänezeit** beträgt 14 Tage."  

generally, negations should be included into the annotation, e.g.  
"In der letzten Änderung des Impfschemas gibt es ja nun die FN 5, die in diesem Fall [**keine** Auffrischungsimpfung] mehr empfiehlt (wenn  die [Infektion] [3 Monate nach] [2. Impfung] erfolgt.)."

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
