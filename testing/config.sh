# Hard-code the Python command that works on your system EX: `python3`
# IMPORTANT: Do not put any whitespace around the '='
PYTHON=''

if [[ -z $PYTHON ]] && which python &>/dev/null && [[ $(python -V 2>&1) = "Python 3"* ]]; then
    PYTHON=python
elif [[ -z $PYTHON ]] && which python3 &>/dev/null && [[ $(python3 -V 2>&1) = "Python 3"* ]]; then
    PYTHON=python3
elif [[ -z $PYTHON ]]; then
    cat <<ERROR
I could not find a working Python 3 interpreter on your computer.

If you know which command to use, open scripts/python.conf and assign it to
the variable PYTHON.

Contact erik.falor@usu.edu if you need help
ERROR
    exit 1
fi
