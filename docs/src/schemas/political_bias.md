# Political Bias
The political bias layer points to [segment](segment.md) identifiers. It marks single segments as belonging to one of the 5 classes described in this paper: 

Aksenov, D., Bourgonje, P., Zaczynska, K., Ostendorff, M., Moreno-Schneider, J., & Rehm, G. (2021). Fine-grained Classification of Political Bias in German News: A Data Set and Initial Experiments. Proceedings of the 5th Workshop on Online Abuse and Harms (WOAH 2021), 121–131. https://doi.org/10.18653/v1/2021.woah-1.13

The classes are:
- far-left
- center-left
- center
- center-right
- far-right

The classes can be collapsed into a binary setup for detection of hyperpartisanship: `far-left` and `far-right` are hyperpartisan, the others are non-hyperpartisan.