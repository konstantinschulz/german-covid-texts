![docs badge](https://github.com/konstantinschulz/german-covid-texts/actions/workflows/docs.yml/badge.svg)

# German Covid Texts
In this repository, you will find progress and updates for a new dataset of German texts about COVID-19.

# Documentation
The generated documentation is accessible at https://konstantinschulz.github.io/german-covid-texts/. It was built using [mdBook](https://github.com/rust-lang/mdBook) and a [workflow file](.github/workflows/docs.yml) for [GitHub Actions](https://github.com/features/actions). This project uses continuous documentation, supported by automatic validation of internal links. 

From the `docs` folder, the documentation can be 
- built and tested by running `mdbook build && mdbook test`,
- accessed at http://localhost:3000 by running `mdbook serve`.

# Roadmap
- [ ] Learn how to model Extractive Question Answering in Inception. If that fails, look for alternatives (e.g. Haystack).
- [ ] Constrain the relations tagset to a manageable amount (maybe 10 or 20?).
- [ ] Improve data preprocessing: Remove hyphenation from the input (where possible).
