#!/usr/bin/env zsh

set -x

ruff format --check src/ tests/
ruff src/ tests/

