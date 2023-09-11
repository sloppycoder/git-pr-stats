
# Welcome to your Python project

## Run code gen

```shell

ariadne-codegen --config codegen-github.toml
ariadne-codegen --config codegen-gitlab.toml

```

## Setup

The easiest way to get started is probably use [Jetpack.io devbox](https://www.jetpack.io/devbox). Install devbox first, then

```shell
devbox shell

# you should ready to go

```

The more traditional way is to install python 3.10 and [poetry](https://python-poetry.org/), then

```shell

# create virtualenv
poetry shell
# install dependencies
poetry install

```

## Develop the code for the stack

```shell

# run unit tests
pytest

```
