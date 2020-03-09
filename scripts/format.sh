#!/usr/bin/env bash

poetry shell
find . -type f -name "*.py" -exec `which python` -m autopep8 --in-place {} \;

