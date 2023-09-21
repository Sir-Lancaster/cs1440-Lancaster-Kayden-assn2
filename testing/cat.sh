#!/usr/bin/env bash

source testing/config.sh
source testing/functions.sh


good
echodo $PYTHON src/tt.py cat data/let3 data/num2
echodo $PYTHON src/tt.py cat data/complexity
echodo $PYTHON src/tt.py cat data/ages8 data/colors8 data/complexity data/debugging data/dup5 data/let3 data/names10 data/names8 data/num10 data/num2 data/random20 data/verbs8 data/wordcount data/words200

error
echodo $PYTHON src/tt.py cat data/let3 DOES_NOT_EXIST data/debugging
echodo $PYTHON src/tt.py cat
