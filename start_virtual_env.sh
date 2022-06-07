#!/bin/bash

OS=$(./_os_type.sh)

if [ $OS = "Unix" ]; then
  source ./venv/bin/activate
elif [ $OS = "Windows" ]; then
  venv\Scripts\Activate.ps1
fi