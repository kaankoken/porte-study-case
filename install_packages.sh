#!/bin/

_pip=""
if [ hash pip 2>/dev/null ]; then
    _pip=pip
else
    _pip=pip3
fi

$_pip install --upgrade pip
$_pip install -r requirements.txt