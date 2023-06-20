#!/usr/bin/env bash

# Use this scipt to run all notebooks if you are in main

# Run all notebooks to generate the output
# Also generate the HTML output

find . -name "*.ipynb" -print -exec jupyter nbconvert --to notebook --execute {} \; -exec jupyter nbconvert --to html {} \;