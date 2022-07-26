# Relations
The relation layer points to [entity](entity.md) identifiers. It marks two [Named Entities](entity.md) as connected by a [WikiData property](https://www.wikidata.org/wiki/Wikidata:List_of_properties).

## Tags:
A. Time
1. [follows](#p155) (P155)
2. [point in time](#p585) (P585) 
3. [duration](#p2047) (P2047)
4. [start time](#p580) (P580)
5. [end time](#p582) (P582)

B. Causal
  
6. [has cause](#p828) (P828)  
7. [has contributing factor](#p1479) (P1479)

C. Covid-Related  

8. [biological variant of](#p3433) (P3433)  
9. [symptoms and signs](#p780) (P780)  

D. Location  

10. [location](#p276) (P276) 
11. [start point](#p1427) (P1427)  

E. Other

12. [synonym](#p5973) (P5973) 
13. [part of](#p361) (P361)  
------
## Tags (Wikidata)

### A. Time
#### 1. [follows](#p155) (P155)  

Immediately prior item in a series of which the subject is a part. Not to be confused with "has cause", which is a causal relation, we use "follow" as a temporal expression of consecutive events. Inverse propery of "followed by".
> "Nach einem Voraufenthalt in einem Virusvariantengebiet beträgt die Quarantäne 14 Tage und kann nicht verkürzt werden ."
>> Voraufenthalt in einem Virusvariantengebiet > follows > Quarantäne  
> "In der letzten Änderung des Impfschemas gibt es ja nun die FN 5, die in diesem Fall [keine Auffrischungsimpfung] mehr empfiehlt (wenn  die [Infektion] [3 Monate nach] [2. Impfung] erfolgt.)."

keine Auffrischungsimpfung > has cause > Infektion

[2.Impfung]MEASURE > start point > [3 Monate]DURATION  
[Infektion] > follows > [3 Monate]

#### 2. [point in time](#p585) (P585) 

Time and date something took place, existed or a statement was true. Related properties "start time" and "end time" should be preferred if also possible.

>In Kooperation mit dem @X macht unsere [ImpfenHilftTour] den nächsten Halt in Halle an der Saale am [22. und am 23.  März 2022] !  Dort warten ab 11 Uhr unsere mehrsprachigen Wertebotschafter:innen auf dich und beantworten deine Fragen zur  Coronaschutzimpfung!  ImpfenHilft""
>>ImpfenHilftTour > point in time > 22. und 23. März 2022

#### 3. [duration](#p2047) (P2047)

Description: Length of time of an event or process
> "Nach einem Voraufenthalt in einem Virusvariantengebiet beträgt die Quarantäne 14 Tage und kann nicht verkürzt werden."
>> Quarantäne > duration > 14 Tage

#### 4. [start time](#p580) (P580)

Description: Time a time period starts
> "Zum 1. August ist außerdem die neue Einreiseverordnung in Kraft getreten."
>> Neue Einreiseverordnung > start time > 1. August

#### 5. [end time](#p582) (P582)

Description: Time a time period ends
> "Darüber hinaus wurden nur Fälle mit Angabe Meldedatum bis einschließlich 17.3.2020 (Datenstand minus 14 Tage, um den Zeitverzug für die Erfassung des Krankheitsverlaufs schwerer Fälle zu berücksichtigen) berücksichtigt"
>> Angabe Meldedatum > end time > 17.3.2020

## B. Causal
#### 6. [has cause](#p828) (P828)  

Underlying cause, thing that ultimately resulted in this effect. If possible, prefer, the narrower relation "symptoms and signs". 


#### 7. [has contributing factor](#p1479) (P1479)

Thing that significantly influenced the effect, but did not directly cause it.

What is the difference between a "cause" and a "contributing factor"? In public health, law, social and natural science, the difference is that an effect would not have happened but for a cause, whereas it would have still happened but for a contributing factor. In other words, if you take away a contributing factor, the effect still would have happened. However if you took away a cause, the effect would not have happened.

Here is a test for assigning something as a cause or a contributing factor:

If the thing were removed, would that have prevented the effect?

    (1) Yes: the thing is a cause
    (2) No, but it significantly influenced the effect: the thing is a contributing factor

(taken from: https://www.wikidata.org/wiki/Help:Modeling_causes)

Example: 
> "Die [Warnung vor nicht notwendigen und touristischen Reisen] **aufgrund von**  [COVID-19] **hängt stark** mit der [Einstufung eines Landes als Hochrisiko- bzw. Virusvariantengebiet] **zusammen** ."
>> Warnung vor nicht notwendigen und touristischen Reisen > has cause > COVID-19
>> Einstufung eines Landes als Hochrisiko- bzw. Virusvariantengebiet > has contributing factor > Warnung

## C. Covid-Related
#### 8. [biological variant of](#p3433) (P3433) 

A variant of a physical biological entity (e.g., gene sequence, protein sequence, epigenetic mark)
> "Eine neue SARS-CoV-2 Variante wurde im Dezember 2020 im Süden des Vereinigten Königreichs. (UK) als besorgniserregende Variante eingestuft (englische Nomenklatur: VOC: Variant of concern ). Die erste PatientInnenprobe, in der sie identifiziert werden konnte, stammte vom September 2020. Die Variante wird als VOC 202012/01, B.1.1.7 oder N501Y bezeichnet."
>> B.1.1.7 > biological variant of > SARS-CoV-2
>> VOC 202012/01 > biological variant of > SARS-CoV-2
>> N501Y > biological variant of > SARS-CoV-2

>> *Pattern: DESEASE > biological variant of > DESEASE*

#### 9. [symptoms and signs](#p780) (P780)  

Description: Possible symptoms of a medical condition
> "Ausnahmen bilden hier die Anteile zur Datenvollständigkeit für Fälle mit Husten und Fieber sowie für Fälle mit Pneumonie."
>> Fälle > symptoms and signs > Husten, Fieber, Pneumonie

>> *Pattern: DESEASE > symptoms and signs > SYMPTOM*

## D. Local

### 12. [location](#p276) (P276)

Location of the object, structure or event. Summarizes all locations of an administrative entity (P131) and geograohical entities (P706).
> "Weitere VOC wurden aus Brasilien (1.1.28.1) und Südafrika (501.V2) gemeldet. Zum aktuellen Zeitpunkt gibt es altersspezifische Daten nur für die Variante B.1.1.7 aus England"
>> 1.1.28.1 > location > Brasilien
>> 501.V2 > location > Südafrika
>> B.1.1.7 > location > England
 Wege entstanden und hat sich vom Tier auf den Menschen übertragen."

#### 13. [start point](#p1427) (P1427)

Specification of "location" (P276), and exact match to [fromLocation](https://schema.org/fromLocation) property from schema.org. Expresses the original location of the object or the agent before an action.


## E. Other

#### 10. [synonym](#p5973) (P5973) 

Sense of another lexeme with the same meaning as this sense, in the same language. 
> "Die Variante wird als VOC 202012/01, B.1.1.7 oder _ N501Y bezeichnet."
>> VOC 202012/01 > synonym > B.1.1.7
>> N501Y > synonym > B.1.1.7
>> VOC 202012/01 > synonym > B.1.17
>> VOC 202012/01 > synonym > N501Y

#### 11. [part of](#p361) (P361)

Object of which the subject is a part (if this subject is already part of object A which is a part of object B, then please only make the subject part of object A). Inverse property of "has part" (P527, see also "has parts of the class" (P2670)).
>"im schwer von COVID-19 betroffen Frankreich, waren im Frühjahr 2020 vor allem der Großraum Paris sowie der Region „Grand Est" und dort vor allem die Départements Bas-Rhin und Haut- Rhin betroffen"
>> Großraum Paris > part of > Frankreich


## Information on Relation Tags

The Wikidata relations above constitute:

* a subset of [DocRED relations](https://drive.google.com/drive/folders/1c5-0YwnoJx8NS6CV2f-NoTHR__BdkNqw)

* additional Wikidata relations: 

"P3433": "biological variant of", "P5973": "synonym", "P780": "symptoms", "P878": "has cause", "P2047": "duration"