#!/usr/bin/env bash

pip install --user poetry
poetry --version
poetry config virtualenvs.in-project true --local
poetry install --no-root
