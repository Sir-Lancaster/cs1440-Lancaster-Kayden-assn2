# CS 1440 Assignment 2: Text Tools - Test Scripts

Automated testing is an important aspect of software development, and I want to help you rigorously test your project.  Inside this directory, you'll find shell scripts that will streamline the testing process for your Text Tools.

To validate your work, match your program's output against the [Output Examples](../instructions/examples).

## **Heads Up!**

*   Execute these scripts from the root directory of the project.
*   Don't rename `src/tt.py`, or the scripts won't function!

Since we all use various operating systems here at DuckieCorp, the Python 3 command might differ.

These testing scripts are configured to auto-detect the appropriate Python interpreter for your system. It's usually works! If you encounter issues, modify [config.sh](./config.sh) with the Python command you typically use in the shell.


## Running The Scripts

**Important** These scripts *must* be run from the project's root directory, like this:

```
$ testing/cat.sh
  ___              _                                   _    
 / __|___  ___  __| |  __ ___ _ __  _ __  __ _ _ _  __| |___
| (_ / _ \/ _ \/ _` | / _/ _ \ '  \| '  \/ _` | ' \/ _` (_-<
 \___\___/\___/\__,_| \__\___/_|_|_|_|_|_\__,_|_||_\__,_/__/

TEST$ python src/tt.py cat data/let3 data/num2
a
b
c
1
2

TEST$ python src/tt.py cat data/complexity
     "There are two ways of constructing a software design:

... Skipped many lines...
```


Before you write the code for a tool, the test scripts will produce output like this:

```
$ testing/cat.sh
  ___              _                                   _
 / __|___  ___  __| |  __ ___ _ __  _ __  __ _ _ _  __| |___
| (_ / _ \/ _ \/ _` | / _/ _ \ '  \| '  \/ _` | ' \/ _` (_-<
 \___\___/\___/\__,_| \__\___/_|_|_|_|_|_\__,_|_||_\__,_/__/

TEST$ python src/tt.py cat data/let3 data/num2
TODO: Determine which tool the user has invoked by examining sys.argv
TODO: Use if/elif/else to select which function to call
TODO: Call the requested tool, passing remaining arguments from sys.argv
TODO: Call usage() and exit when bad input is provided

TEST$ python src/tt.py cat data/complexity
TODO: Determine which tool the user has invoked by examining sys.argv
TODO: Use if/elif/else to select which function to call
TODO: Call the requested tool, passing remaining arguments from sys.argv
TODO: Call usage() and exit when bad input is provided
```

As you progress through the project, more and more of the test scripts will create output that matches my examples.  You'll know you are done when everything looks the same!


## Understanding Shell Syntax

Understanding how these scripts work is not part of this assignment.  But in case you are curious...

*   `#!/usr/bin/env bash`
    *   This is called the *shebang line*
    *   It tells the OS how to execute this text file
        *   In this case, the OS runs this file with the Bash interpreter
    *   `#` introduces a comment, just like in Python
        *   Once `bash` takes over the execution of this file, the shebang line is treated as an ordinary comment 
*   `source scripts/python.conf`
    *   Execute `scripts/python.conf` in context of the current script to declare functions and initialize variables
    *   `source` is Bash's version of `import`
*   `PYTHON=''`
    *   Declare a new variable and assign the empty string to it
    *   Just like Python, the assignment operator in Bash is `=`
    *   Unlike Python, white space *cannot* surround the `=` operator!
        *   For example, this is wrong: `PYTHON = python3`
    *   It is common for the names of Bash variables to be written in *UPPER_CASE*
*   `$PYTHON`
    *   Access the value stored in the `PYTHON` variable
    *   `$` *expands* a variable into its value
    *   Otherwise, `PYTHON` is treated as the string `"PYTHON"` instead of being replaced with the name of your computer's Python interpreter
    *   Do not use `$` when *assigning* a value to a variable!
        *   For example, this is wrong: `$PYTHON=python3`
*   `echodo $PYTHON src/tt.py ...`
    *   Call a function named `echodo` that prints a command right before running it
