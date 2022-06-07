#!/bin/bash

OS="`uname`"

case "$OSTYPE" in
  solaris*) OS="Unix" ;;
  darwin*)  OS="Unix" ;; 
  linux*)   OS="Unix" ;;
  msys*)    OS="Windows" ;;
  cygwin*)  OS="Windows" ;;
  *)        OS="unknown: $OSTYPE" ;;
esac

echo $OS
