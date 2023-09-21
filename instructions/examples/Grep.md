# Pattern Search (`grep`)

Find all shades of Blue in our list of colors.  Notice that the pattern may occur anywhere in a line of text:

    $ python src/tt.py grep Blue data/colors8
    Royal Blue
    Midnight Blue
    Dodger Blue

Words containing double 'o's; 200 lines trimmed down to 4!

    $ python src/tt.py grep oo data/words200
    clubroom
    boom
    flooding
    burglarproofed


The search pattern is case-sensitive; lowercase 'blue' is not present in the list of color names, hence no results are printed *(notice that the prompt reappears immediately with no output in between)*

    $ python src/tt.py grep blue data/colors8
    $


When multiple file names are given on the command line, the name of the file is displayed before the matching line, separated by a colons `:`.  You must replicate this format: `filename:line`.

Find all lines containing lowercase letter 'a' across many files:

    $ python src/tt.py grep a data/ages8 data/colors8 data/let3
    data/colors8:Favorite Color
    data/colors8:Royal Blue
    data/colors8:Light Salmon
    data/colors8:DarkSea Green
    data/colors8:Dark Goldenrod
    data/let3:a


The `-v` argument prints lines that *don't* have a match.  As before, when multiple filenames are given as arguments, their names are printed before the non-matches.

Find all lines *not* containing lowercase `'a'` across many files:

    $ python src/tt.py grep -v a data/ages8 data/colors8 data/let3
    data/ages8:Age
    data/ages8:22
    data/ages8:36
    data/ages8:24
    data/ages8:39
    data/ages8:26
    data/ages8:23
    data/ages8:29
    data/ages8:17
    data/colors8:Midnight Blue
    data/colors8:Antique White
    data/colors8:Dodger Blue
    data/colors8:Snow
    data/let3:b
    data/let3:c


Styles of locomotion containing the substring 'rch'

    $ python src/tt.py grep rch data/verbs8
    march
    lurch


And the rest...

    $ python src/tt.py grep -v rch data/verbs8
    Locomotion Style
    crawl
    traipse
    push
    trot
    slink
    wriggle



## Handling Errors
The program aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

    $ python src/tt.py grep a data/let3 DOES_NOT_EXIST data/complexity
    data/let3:a
    Traceback (most recent call last):
      File "/home/fadein/assn2/src/tt.py", line 29, in <module>
        grep(sys.argv[2:])
      File "/home/fadein/assn2/src/Grep.py", line 31, in grep
        f = open(fil)
            ^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'


The program aborts with a usage message when no search term is provided:

    $ python src/tt.py grep
    Error: Please provide a pattern and at least one filename

        tt.py grep [-v] PATTERN FILENAME...
            Print lines of files matching PATTERN
            -v  Invert matching; print lines which DO NOT match PATTERN


The program also exits with an error message when no filenames are given:

    $ python src/tt.py grep pattern
    Error: Please provide a pattern and at least one filename

        tt.py grep [-v] PATTERN FILENAME...
            Print lines of files matching PATTERN
            -v  Invert matching; print lines which DO NOT match PATTERN


The `-v` argument must **not** be treated as a search pattern:

    $ python src/tt.py grep -v
    Error: Please provide a pattern and at least one filename

        tt.py grep [-v] PATTERN FILENAME...
            Print lines of files matching PATTERN
            -v  Invert matching; print lines which DO NOT match PATTERN


Under all circumstances both `PATTERN` and `FILENAME...` are required; even when there is a `-v` on the command line, two more arguments are needed:

    $ python src/tt.py grep -v data/let3
    Error: Please provide a pattern and at least one filename

        tt.py grep [-v] PATTERN FILENAME...
            Print lines of files matching PATTERN
            -v  Invert matching; print lines which DO NOT match PATTERN

