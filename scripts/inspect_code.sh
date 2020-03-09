#!/usr/bin/env bash

export PATH=`poetry env info --path`/bin:$PATH
`which python` -m flake8
