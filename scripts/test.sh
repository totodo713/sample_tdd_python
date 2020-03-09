#!/usr/bin/env bash

export PATH=`poetry env info --path`/bin:$PATH
`which python` -m pytest --cov=sample_tdd --cov-report=html --html=reports/test/results.html --self-contained-html
