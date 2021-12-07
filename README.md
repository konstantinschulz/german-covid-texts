![docs badge](https://github.com/konstantinschulz/german-covid-texts/actions/workflows/docs.yml/badge.svg)

# Documentation
The generated documentation is accessible at https://konstantinschulz.github.io/german-covid-texts/. It was built using [mdBook](https://github.com/rust-lang/mdBook) and a [workflow file](.github/workflows/docs.yml) for [GitHub Actions](https://github.com/features/actions). This project uses continuous documentation, supported by automatic validation of internal links. 

From the `docs` folder, the documentation can be 
- built and tested by running `mdbook build && mdbook test`,
- accessed at http://localhost:3000 by running `mdbook serve`.
