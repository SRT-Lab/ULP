#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  echo 'linux detected. Try to install packages automatically ...'
  # install python-dev 
  sudo apt-get update && sudo apt install python2-dev python3-dev 
elif [[ "$OSTYPE" == "darwin"* ]]; then
  brew install python
else
  echo 'WARNING: Please manually install python'
fi


# install python3  and its requirements
python3 -V
pip install numpy
pip install pandas
pip install regex
