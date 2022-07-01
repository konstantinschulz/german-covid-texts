# Political Bias
The political bias layer points to [token](token.md) identifiers. It marks spans of tokens as belonging to one of the 5 classes described in this paper: 

Aksenov, D., Bourgonje, P., Zaczynska, K., Ostendorff, M., Moreno-Schneider, J., & Rehm, G. (2021). Fine-grained Classification of Political Bias in German News: A Data Set and Initial Experiments. Proceedings of the 5th Workshop on Online Abuse and Harms (WOAH 2021), 121–131. https://doi.org/10.18653/v1/2021.woah-1.13

The token span is always equal to the length of the whole tweet.

## Classes
- far-left
- center-left
- center
- center-right
- far-right

## Binary Model
The classes can be collapsed into a binary setup for detection of hyperpartisanship: `far-left` and `far-right` are hyperpartisan, the others are non-hyperpartisan.

## Definitions
### Hyperpartisan (Far-Left or Far-Right)
- the utterance includes violence/ threatening
- it includes conspiracy theories and fake news (Aksenov et al., 2021)
- Using slurs: “Slurs are lexical items that convey negative attitudes or heavy emotional connotations towards a social group (Hess, 2019), typically centered around race, nationality, religion, gender, or sexual orientation (Bianchi, 2014). As one of their functions, slurs derograte targeted groups or individuals, and they specifically call up one or more descriptive attributes of the targeted group” (Ruppenhofer, Siegel & Struß 2020)
- it includes hate speech. According to de Gibert et al. (2018), hate speech is commonly defined as “a) a deliberate attack, b) directed towards a specific group of people, and c) motivated by actual or perceived aspects that form the group’s identity.”

### Far-Left
Left-wing politics is generally understood as striving for social equality. The freedom of the community is above that of the individual. Opinion researcher Elisabeth Noelle-Neumann discovered that people not only associate left-wing values with equality, but also with justice, formlessness, warmth, closeness, spontaneity, the international and cosmopolitan and the informal address.
#### Examples
`Nochmal für alle Impfschwurbler : Niemand hat behauptet , dass die Impfung immun gegen Corona macht .`
### Center
The center label is used for politically neutral or balanced cases. It is also the default label for unpolitical statements.
### Center-Right
#### Examples
`geht es beim impfen nur ums impfen oder darum Antikörper zu produzieren ? ohne Antikörper Test wissen wir das doch nicht !`
### Far-Right
The political right assumes human inequality and advocates a hierarchy with traditional values and norms. Individual freedom is more important than social equality. With right-wing values, according to Elisabeth Noelle-Neumann, people associate distance, authority, discipline, regulated manners, the national and the formal address in addition to emphasizing differences.
#### Examples
`Aber in meiner Umgebung häufen sich derzeit Fälle ausschließlich bei Geimpften !`

`Ich verleugne Corona nicht und bin generell kein Impfgegner , jedoch eine Impfpflicht lehne ich ab .`

`50 % meiner Bekannten die sich Impfen lassen haben und vorher kein Leiden hatten sind jetzt zum Teil Arbeitsunfähig und Krank .`
