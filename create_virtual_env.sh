#!/bin/bash

OS=$(./_os_type.sh)

if [ $OS = "Unix" ]; then
    if [ hash python 2>/dev/null ]; then
        python -m venv venv
    else
        python3 -m venv venv
    fi
elif [ $OS = "Windows" ]; then
    if [ hash python 2>/dev/null ]; then
        python -m venv venv
    else
        python3 -m venv venv
    fi
fi