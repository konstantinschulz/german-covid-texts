# Named Entities

The named entity layer points to [token](../span_types/token.md) identifiers. It marks spans of tokens as belonging to one of the following classes described in [ACE annotation guidelines](https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-entities-guidelines-v6.6.pdf):

- **Person** - Person entities are limited to humans. A person may be a single individual or a group.
- **Location** - Location entities are limited to geographical entities such as geographical areas and landmasses, bodies of water, and geological formations. They also include Geo-political entities are geographical regions defined by political and/or social groups (nations, regions).
- **Organization** - Organization entities are limited to corporations, agencies, and other groups of people defined by an established organizational structure

We modified the ACE classes by joining Location and geo-political entities into one class, and only include the top-classes.

Additionally, we add the following labels:

- **Time** - an entity describing a point in time or atime span, e.g.  
*[Gestern] wurde die neue Verordnung verabschiedet; Die verordnete Quarantänezeit beträgt [14 Tage].*  
The distinction between a point in time or duration is made using entities from the relation layer.
- **Desease** - all mentioned deseases in a tweet, e.g.  
*Der Verlauf von [Covid] war bei mir zunächst mild, das Fieber kam erst am folgenden Tag. Danach kam [Long-Covid].*
- **Symptom** - Symptoms of a deasease (Covid or other) or resulting from side effects of a medicine/vaccine, e.g.  
*Der Verlauf von Covid war bei mir zunächst mild, das [Fieber] kam erst am folgenden Tag.*
- **Measure** - An entity describing a measure and decision by the federal governmenty related to Covid-19, e.g.  
*Die verordnete [Quarantänezeit] beträgt 14 Tage.*

We do not include preceding articles, titles or addresses into the annotation, e.g. "Frau Dr. *[Merkel]*".

Other layers that directly reference this layer:

- [Relations](relation.md)

## Specifications

### 1. Unnamed Entities

Entities without a name are **not** annotated in this layer. This also applies to anonymized mentions (e.g., Twitter handles). Example:  
*generell kann man nie sagen **wer** schon vielleicht Antikörper hat*

### 2. Coreference Resolution

Coreferences through pronouns or other pointers ("") are **not** resolved in this layer. Therefore, they do **not** get annotated as entities, due to our policy on Unnamed Entities. Example:  
*50% meiner Bekannten **die** sich Impfen lassen haben und vorher kein Leiden hatten sind jetzt zum Teil Arbeitsunfähig und Krank*

### 3. Negations

Generally, negations should be included into the annotation if it affects the resulting event, e.g.:  
*In der letzten Änderung des Impfschemas gibt es ja nun die FN 5, die in diesem Fall [**keine** Auffrischungsimpfung] mehr empfiehlt (wenn  die Infektion 3 Monate nach 2. Impfung erfolgt.).*

### 4. Attributes

Attributes are only annotated if they are essential for understanding. Examples
(symptoms):

- *[laufende Nase]* ("Nase" alone is not a symptom)
- *[erhöhte Temperatur]*
- *[schwerer Verlauf]*

The general rule is to only annotate what is essential for understanding.

In the case of nominalised verbs, the corresponding arguments should also be annotated, if the meaning is otherwise not clearly preserved.

- *Die [Einstufung eines Landes als Hochrisiko- bzw. Virusvariantengebiet]*  
- incorrect: *\*Die [Einstufung] eines Landes als Hochrisiko- bzw. Virusvariantengebiet*

Based on: *jmd./etw. "stuft" jmdn./etw. als ein solches "ein"*. The arguments only serve as orientation to estimate the scope of the NE annotation.

Not annotated should be what is not essential for the main entity meaning.

- *Neben Erst-, Zweit- und Boosterimpfungen besteht auch ein Impfangebot mit Novavax sowie [Schutzimpfungen für Kinder] zwischen 5 und 11 Jahren.*
- incorrect: *\*Neben Erst-, Zweit- und Boosterimpfungen besteht auch ein Impfangebot mit Novavax sowie [Schutzimpfungen für Kinder zwischen 5 und 11 Jahren].*

- *[Astra Zeneca], der Impfstoff der in Großbritannien genutzt wurde, (...))*  
- incorrect: *\*[Astra Zeneca, der Impfstoff der in Großbritannien genutzt wurde, (...)]*

In case of doubt which arguments to include, a look into verb lexicons like [Elektronisches Valenzlexikon](https://grammis.ids-mannheim.de/verbvalenz) or [Netzverb](https://www.verben.de/) can help.

Only measures related to Covid are annotated. Therefore, like the following example, the annotation should be as follows:

- *Die [Impfung] gegen Covid ist nun seit längerer Zeit verfügbar*
- incorrect: *\*Die [Impfung gegen Covid] ist nun seit längerer Zeit verfügbar*

### 5. Hyphenated compunds

Hyphenated compund words are marked as one entity, e.g.

- *[Omicron-Variante]*  
- *[Erst- und Zweitimpfung]*
