# Displaying Partial Files (`head` and `tail`)

## head

The `head` tool prints the first lines of files.  When the file is less than or equal to 10 lines long `head` is the same as `cat`

    $ python src/tt.py head data/let3
    a
    b
    c


    $ python src/tt.py head data/names10
    Jerry
    Bailey
    Frank
    Kai
    Angela
    Mikayla
    Hazel
    Karen
    Alexa
    Isabel


For longer files, `head` prints the first 10 lines then stops:

    $ python src/tt.py head data/words200
    social
    insomniac
    implicitly
    cranky
    opponents
    clubroom
    uttering
    roughen
    easter
    dad


A limit different than 10 may be specified after the `-n` argument.  Keep in mind that command line arguments are *always* strings.  You'll need to convert this argument into a number yourself.

    $ python src/tt.py head -n 13 data/words200
    social
    insomniac
    implicitly
    cranky
    opponents
    clubroom
    uttering
    roughen
    easter
    dad
    sleighs
    honoraries
    smelt


    $ python src/tt.py head -n 3 data/complexity
         "There are two ways of constructing a software design:

                    one way is to make it so simple


When multiple files are given to the program a banner is printed to identify where the text came from.  The form of the banner must follow this pattern: `==> FILENAME <==`.  Notice that the same line number limit is applied to all files:

    $ python src/tt.py head -n 5 data/ages8 data/names8 data/words200
    ==> data/ages8 <==
    Age
    22
    36
    24
    39

    ==> data/names8 <==
    Name
    Adrianna
    Julian
    Tiffany
    Savannah

    ==> data/words200 <==
    social
    insomniac
    implicitly
    cranky
    opponents


    $ python src/tt.py head -n 3 data/complexity data/debugging
    ==> data/complexity <==
         "There are two ways of constructing a software design:

                    one way is to make it so simple

    ==> data/debugging <==
            "Everyone knows that debugging is twice as hard
                as writing a program in the first place.


### Handling Errors

This tool aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

    $ python src/tt.py head data/let3 DOES_NOT_EXIST data/complexity
    ==> data/let3 <==
    a
    b
    c

    Traceback (most recent call last):
      File "/home/fadein/assn2/src/tt.py", line 22, in <module>
        head(sys.argv[2:])
      File "/home/fadein/assn2/src/Partial.py", line 31, in head
        f = open(fil)
            ^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'


The tool must report an error when too few arguments are given; at a minimum the name of one input file is required:

    $ python src/tt.py head
    Error: Too few arguments

        tt.py head|tail [-n N] FILENAME...
            Output the first or last part of files
            -n  Number of lines to print (default N=10)


The `-n` option requires an argument.  It must be in the form of an integer.  Alert the user when this number is left off:

    $ python src/tt.py head -n
    Error: Number of lines is required

        tt.py head|tail [-n N] FILENAME...
            Output the first or last part of files
            -n  Number of lines to print (default N=10)


Alert the user when this argument *does not* appear as an integer.  Your program doesn't know that "seven" means the same thing as "7", and so errors out:

    $ python src/tt.py head -n seven
    Error: Number of lines is required

        tt.py head|tail [-n N] FILENAME...
            Output the first or last part of files
            -n  Number of lines to print (default N=10)


A negative line count does not make sense; treat this as an error:

    $ python src/tt.py head -n -7
    Error: Number of lines is required

        tt.py head|tail [-n N] FILENAME...
            Output the first or last part of files
            -n  Number of lines to print (default N=10)


Even when the `-n` option is given a valid numeric argument, one or more filenames are still required:

    $ python src/tt.py head -n 7
    Error: At least one filename is required

        tt.py head|tail [-n N] FILENAME...
            Output the first or last part of files
            -n  Number of lines to print (default N=10)



## tail

`tail`, by contrast, prints the final 10 (or N) lines of a file.  When the file is less than or equal to 10 lines long `tail` is the same as `cat`

    $ python src/tt.py tail data/let3
    a
    b
    c


For longer files, much of the content can be suppressed in this way

    $ python src/tt.py tail data/words200
    convicting
    exacerbating
    indictment
    very
    impersonated
    latching
    reconfigurations
    activates
    autobiographies
    adverbs


When multiple files are given on the command line, identify each by preceding their content with a banner.  Notice that the same limit is applied to all files:

    $ python src/tt.py tail -n 3 data/ages8 data/names8 data/words200
    ==> data/ages8 <==
    23
    29
    17

    ==> data/names8 <==
    Michael
    Marcus
    Julianna

    ==> data/words200 <==
    activates
    autobiographies
    adverbs


As with `head`, a different number of lines besides 10 is specified with the `-n` flag:

    $ python src/tt.py tail -n 4 data/words200
    reconfigurations
    activates
    autobiographies
    adverbs

    $ python src/tt.py tail -n 1 data/words200
    adverbs


Combining these tools enables you to extract a portion from the middle of a large file.  These commands use the shell's redirection operator `>` to extract words 81 - 97 from a file containing 200 words:

    $ python src/tt.py head -n 97 data/words200 > first97
    $ python src/tt.py tail -n 17 first97
    chrysanthemum
    malts
    draughts
    sterilizes
    hydrogen
    even
    pulsate
    upland
    outperforms
    subprogram
    lustiness
    handicap
    boom
    inhabiting
    improviser
    musicals
    the


Don't forget to clean up after yourself:

    $ rm first97


### Handling Errors

The program aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

    $ python src/tt.py tail data/let3 DOES_NOT_EXIST data/complexity
    ==> data/let3 <==
    a
    b
    c

    Traceback (most recent call last):
      File "/home/fadein/assn2/src/tt.py", line 24, in <module>
        tail(sys.argv[2:])
      File "/home/fadein/assn2/src/Partial.py", line 74, in tail
        f = open(fil)
            ^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'


The tool must report an error when too few arguments are given; at a minimum the name of one input file is required:

    $ python src/tt.py tail
    Error: Too few arguments

        tt.py head|tail [-n N] FILENAME...
            Output the first or last part of files
            -n  Number of lines to print (default N=10)


The `-n` option requires an argument.  It must be in the form of an integer.  Alert the user when this number is left off:

    $ python src/tt.py tail -n
    Error: Number of lines is required

        tt.py head|tail [-n N] FILENAME...
            Output the first or last part of files
            -n  Number of lines to print (default N=10)


Alert the user when this argument *does not* appear as an integer.  Your program doesn't know that "seven" means the same thing as "7", and so errors out:

    $ python src/tt.py tail -n seven
    Error: Number of lines is required

        tt.py head|tail [-n N] FILENAME...
            Output the first or last part of files
            -n  Number of lines to print (default N=10)
