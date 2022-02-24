# Political Bias
The political bias layer points to [segment](segment.md) identifiers. It marks single segments as belonging to one of the 5 classes described in this paper: 

Aksenov, D., Bourgonje, P., Zaczynska, K., Ostendorff, M., Moreno-Schneider, J., & Rehm, G. (2021). Fine-grained Classification of Political Bias in German News: A Data Set and Initial Experiments. Proceedings of the 5th Workshop on Online Abuse and Harms (WOAH 2021), 121–131. https://doi.org/10.18653/v1/2021.woah-1.13

## Classes
- far-left
- center-left
- center
- center-right
- far-right

## Binary Model
The classes can be collapsed into a binary setup for detection of hyperpartisanship: `far-left` and `far-right` are hyperpartisan, the others are non-hyperpartisan.

## Definitions
### Far-Left
Left-wing politics is generally understood as striving for social equality. The freedom of the community is above that of the individual. Opinion researcher Elisabeth Noelle-Neumann discovered that people not only associate left-wing values with equality, but also with justice, formlessness, warmth, closeness, spontaneity, the international and cosmopolitan and the informal address.
#### Examples
`Nochmal für alle Impfschwurbler : Niemand hat behauptet , dass die Impfung immun gegen Corona macht .`
### Center
The center label is used for politically neutral or balanced cases. It is also the default label for completely unpolitical statements.
### Far-Right
The political right assumes human inequality and advocates a hierarchy with traditional values and norms. Individual freedom is more important than social equality. With right-wing values, according to Elisabeth Noelle-Neumann, people associate distance, authority, discipline, regulated manners, the national and the formal address in addition to emphasizing differences.
#### Examples
`Aber in meiner Umgebung häufen sich derzeit Fälle ausschließlich bei Geimpften !`

`Ich verleugne Corona nicht und bin generell kein Impfgegner , jedoch eine Impfpflicht lehne ich ab .`

`50 % meiner Bekannten die sich Impfen lassen haben und vorher kein Leiden hatten sind jetzt zum Teil Arbeitsunfähig und Krank .`
