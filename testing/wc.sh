#!/usr/bin/env bash

source testing/config.sh
source testing/functions.sh

echo "${_C}NOTE: The *byte count* on Windows may differ slightly from the examples${_Z}"
echo
echo "${_C}NOTE: Your formatting does not need to exactly match the documentation${_Z}"
echo


good
echodo $PYTHON src/tt.py wc data/num2
echodo $PYTHON src/tt.py wc data/words200
echodo $PYTHON src/tt.py wc data/complexity
echodo $PYTHON src/tt.py wc data/wordcount
echodo $PYTHON src/tt.py wc data/let3 data/random20 data/words200 data/dup5 data/complexity
echodo $PYTHON src/tt.py wc data/let3 data/let3 data/let3 data/let3 data/let3

error
echodo $PYTHON src/tt.py wc data/let3 data/random20 DOES_NOT_EXIST data/dup5
echodo $PYTHON src/tt.py wc
