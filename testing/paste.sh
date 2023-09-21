#!/usr/bin/env bash

source testing/config.sh
source testing/functions.sh


good
echodo $PYTHON src/tt.py paste data/let3 data/num2
echodo $PYTHON src/tt.py paste data/num2 data/let3
echodo $PYTHON src/tt.py paste data/num2 data/let3 data/words5
echodo $PYTHON src/tt.py paste data/num2 data/words5 data/let3
echodo $PYTHON src/tt.py paste data/num10
echodo $PYTHON src/tt.py paste data/names8 data/ages8 data/colors8 data/verbs8

error
echodo $PYTHON src/tt.py paste data/let3 DOES_NOT_EXIST data/num2
echodo $PYTHON src/tt.py paste
