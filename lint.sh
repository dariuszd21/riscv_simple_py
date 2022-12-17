#!/bin/zsh

set -x

isort src/ tests/
black src/ tests/
ruff src/ tests/

