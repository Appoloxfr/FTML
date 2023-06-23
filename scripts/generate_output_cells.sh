#!/usr/bin/env bash

# Use this scipt to run all notebooks if you are in main

# Run all notebooks to generate the output
# Also generate the HTML output

# if using poetry
 poetry env info -p &> /dev/null

if [ $? -eq 0 ]; then
    echo "Using poetry"
    poetry run jupyter nbconvert --to notebook --execute --inplace **/*.ipynb
    poetry run jupyter nbconvert --to html **/*.ipynb
else
    echo "Using conda"
    jupyter nbconvert --to notebook --execute --inplace **/*.ipynb
    jupyter nbconvert --to html **/*.ipynb
fi