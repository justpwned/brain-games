# brain-games

[![CI](https://github.com/justpwned/python-project-lvl1/actions/workflows/ci.yml/badge.svg)](https://github.com/justpwned/python-project-lvl1/actions/workflows/ci.yml)

Brain-games is a package that includes 5 simple CLI games written in Python. The goal of this project was to get acquainted with the process of installing, building and publishing packages in Python using tools such as [Pip](https://pip.pypa.io/en/stable/), [Poetry](https://python-poetry.org/) and [Make](https://www.gnu.org/software/make/). As well as automating the process of linting everytime code is pushed to repository using [Flake8](https://flake8.pycqa.org/en/latest/)(as a linter) and [Github Actions](https://github.com/features/actions)(as a CI utility).

## Installation

```bash
# Install Poetry
pip install poetry

# Install dependencies
make install

# Install package
make package-install
```

After successful installation you should have the following packages available as scripts in your command prompt:

- brain-even ([demo](https://asciinema.org/a/KtHWVuOJWApI3N3a5dyCw5uCm))
- brain-calc ([demo](https://asciinema.org/a/DvaF7asVXi0IrPxMgpR6auzoY))
- brain-gcd ([demo](https://asciinema.org/a/VYPUb2vopzeaXByIoUFJLsh1X))
- brain-progression ([demo](https://asciinema.org/a/utA9w9CEUNBfpO4D2ozZAHXCB))
- brain-prime ([demo](https://asciinema.org/a/gSH74Uxhfion698WnSRj22YNX))
