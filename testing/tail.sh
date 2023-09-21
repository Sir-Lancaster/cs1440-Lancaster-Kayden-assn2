#!/usr/bin/env bash

source testing/config.sh
source testing/functions.sh


good
echodo $PYTHON src/tt.py tail data/let3
echodo $PYTHON src/tt.py tail data/words200
echodo $PYTHON src/tt.py tail -n 3 data/ages8 data/names8 data/words200
echodo $PYTHON src/tt.py tail -n 4 data/words200
echodo $PYTHON src/tt.py tail -n 1 data/words200
echodo "$PYTHON src/tt.py head -n 97 data/words200 > first97"
echodo $PYTHON src/tt.py tail -n 17 first97
echodo rm first97

error
echodo $PYTHON src/tt.py tail data/let3 DOES_NOT_EXIST data/complexity
echodo $PYTHON src/tt.py tail
echodo $PYTHON src/tt.py tail -n
echodo $PYTHON src/tt.py tail -n seven
