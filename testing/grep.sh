#!/usr/bin/env bash

source testing/config.sh
source testing/functions.sh


good
echodo $PYTHON src/tt.py grep Blue data/colors8
echodo $PYTHON src/tt.py grep oo data/words200
echodo $PYTHON src/tt.py grep blue data/colors8
echodo $PYTHON src/tt.py grep a data/ages8 data/colors8 data/let3
echodo $PYTHON src/tt.py grep -v a data/ages8 data/colors8 data/let3
echodo $PYTHON src/tt.py grep rch data/verbs8
echodo $PYTHON src/tt.py grep -v rch data/verbs8

error
echodo $PYTHON src/tt.py grep a data/let3 DOES_NOT_EXIST data/complexity
echodo $PYTHON src/tt.py grep
echodo $PYTHON src/tt.py grep pattern
echodo $PYTHON src/tt.py grep -v
echodo $PYTHON src/tt.py grep -v data/let3
