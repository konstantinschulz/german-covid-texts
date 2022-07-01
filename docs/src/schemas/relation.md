# Relations
The relation layer points to [entity](entity.md) identifiers. It marks two [Named Entities](entity.md) as connected by a [WikiData property](https://www.wikidata.org/wiki/Wikidata:List_of_properties).

Relation annotations are the last step in the topic-focused annotation pipeline: 

(1)  [Informativeness](informativeness.md) - (2) [Topics](topic.md) - **(3) [Relations](relation.md)**.  

Tags:
1. [follows](#p155)
2. [part of](#p361)
3. [country of origin](#p495)
4. [has part](#p527)
5. [start time](#p580)
6. [end time](#p582)
7. [applies to jurisdiction](#p1001)
8. [influenced by](#p737)
9. [biological variant of](#p3433)
10. [synonym](#p5973)
11. [symptoms and signs](#p780)
12. [has cause](#p828)
13. [duration](#p2047)

## Tags (Wikidata)
#### P155
##### "follows"

Description: Immediately prior item in a series of which the subject is a part, preferably use as qualifier of P179 [if the subject has replaced the preceding item, e.g. political offices, use "replaces" (P1365)]
> "Nach einem Voraufenthalt in einem Virusvariantengebiet beträgt die Quarantäne 14 Tage und kann nicht verkürzt werden ."
>> Voraufenthalt in einem Virusvariantengebiet > follows > Quarantäne

#### P361
##### "part of"

Description: Object of which the subject is a part (if this subject is already part of object A which is a part of object B, then please only make the subject part of object A). Inverse property of "has part" (P527, see also "has parts of the class" (P2670)).
>"im schwer von COVID-19 betroffen Frankreich, waren im Frühjahr 2020 vor allem der Großraum Paris sowie der Region „Grand Est" und dort vor allem die Départements Bas-Rhin und Haut- Rhin betroffen"
>> Großraum Paris > part of > Frankreich

#### P495
##### "country of origin"

Description: Country of origin of this item (creative work, food, phrase, product, etc.)
> "Weitere VOC wurden aus Brasilien (1.1.28.1) und Südafrika (501.V2) gemeldet. Zum aktuellen Zeitpunkt gibt es altersspezifische Daten nur für die Variante B.1.1.7 aus England"
>> 1.1.28.1 > country of origin > Brasilien
>> 501.V2 > country of origin > Südafrika
>> B.1.1.7 > country of origin > England

#### P527
##### "has part"

Description: Part of this subject; inverse property of "part of" (P361). See also "has parts of the class" (P2670).
> "im schwer von COVID-19 betroffen Frankreich, waren im Frühjahr 2020 vor allem der Großraum Paris sowie der Region „Grand Est" und dort vor allem die Départements Bas-Rhin und Haut- Rhin betroffen"
>> Frankreich > has part > Großraum Paris, „Grand Est", Bas-Rhin, Haut- Rhin
>> "Grand Est" > has part > Bas-Rhin, Haut- Rhin

#### P580
##### "start time"

Description: Time a time period starts
> "Zum 1. August ist außerdem die neue Einreiseverordnung in Kraft getreten."
>> Neue Einreiseverordnung > start time > 1. August

#### P582
##### "end time"

Description: Time a time period ends
> "Darüber hinaus wurden nur Fälle mit Angabe Meldedatum bis einschließlich 17.3.2020 (Datenstand minus 14 Tage, um den Zeitverzug für die Erfassung des Krankheitsverlaufs schwerer Fälle zu berücksichtigen) berücksichtigt"
>> Angabe Meldedatum > end time > 17.3.2020

#### P1001
##### "applies to jurisdiction"

Description: The item (institution, law, public office, public register...) or statement belongs to or has power over or applies to the value (a territorial jurisdiction: a country, state, municipality, ...)
> „In Deutschland muss gemäß Meldeverordnung jeder Nachweis von SARS-CoV-2 an das Gesundheitsamt gemeldet werden ."
>> Meldeverordnung > applies to jurisdiction > Deutschland

#### P737
##### "influenced by"

Description: This person, idea, etc. is informed by that other person, idea, etc., e.g. "Heidegger was influenced by Aristotle"
> "Die Warnung vor nicht notwendigen und touristischen Reisen aufgrund von COVID-19 hängt stark mit der Einstufung eines Landes als Hochrisiko- bzw. Virusvariantengebiet zusammen ."
>> Warnung > influenced by > Einstufung eines Landes als Hochrisiko- bzw. Virusvariantengebiet 

#### P3433
##### "biological variant of"

Description: A variant of a physical biological entity (e.g., gene sequence, protein sequence, epigenetic mark)
> "Eine neue SARS-CoV-2 Variante wurde im Dezember 2020 im Süden des Vereinigten Königreichs. (UK) als besorgniserregende Variante eingestuft (englische Nomenklatur: VOC: Variant of concern ). Die erste PatientInnenprobe, in der sie identifiziert werden konnte, stammte vom September 2020. Die Variante wird als VOC 202012/01, B.1.1.7 oder N501Y bezeichnet."
>> B.1.1.7 > variant of > SARS-CoV-2
>> VOC 202012/01 > variant of > SARS-CoV-2
>> N501Y > variant of > SARS-CoV-2

#### P5973
##### "synonym"

Description: Sense of another lexeme with the same meaning as this sense, in the same language
> "Die Variante wird als VOC 202012/01, B.1.1.7 oder _ N501Y bezeichnet."
>> VOC 202012/01 > synonym > B.1.1.7
>> N501Y > synonym > B.1.1.7
>> VOC 202012/01 > synonym > B.1.17
>> VOC 202012/01 > synonym > N501Y

#### P780
##### "symptoms and signs"

Description: Possible symptoms of a medical condition
> "Ausnahmen bilden hier die Anteile zur Datenvollständigkeit für Fälle mit Husten und Fieber sowie für Fälle mit Pneumonie."
>> Fälle > symptoms > Husten, Fieber, Pneumonie

#### P828
##### "has cause"

Description: Underlying cause, thing that ultimately resulted in this effect
> "Die Warnung vor nicht notwendigen und touristischen Reisen aufgrund von COVID-19 hängt stark mit der Einstufung eines Landes als Hochrisiko- bzw. Virusvariantengebiet zusammen ."
>> COVID-19 > has cause > Warnung vor nicht notwendigen und touristischen Reisen"

#### P2047
##### "duration"

Description: Length of time of an event or process
> "Nach einem Voraufenthalt in einem Virusvariantengebiet beträgt die Quarantäne 14 Tage und kann nicht verkürzt werden."
>> Quarantäne > duration > 14 Tage

## Information on Relation Tags

The Wikidata relations above constitute:

* a subset of [DocRED relations](https://drive.google.com/drive/folders/1c5-0YwnoJx8NS6CV2f-NoTHR__BdkNqw)

* additional Wikidata relations: 

"P3433": "biological variant of", "P5973": "synonym", "P780": "symptoms", "P878": "has cause", "P2047": "duration"