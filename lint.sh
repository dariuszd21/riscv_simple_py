#!/usr/bin/env zsh

set -x

black src/ tests/
ruff src/ tests/

