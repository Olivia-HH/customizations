#!/bin/sh

#cd parent dir
cd "$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )" &> /dev/null && pwd 2> /dev/null; )"

#run the py script
sudo python3 script.py