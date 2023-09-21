# CS 1440 Assignment 2: Text Tools - Project Requirements

*   Re-create the classic Unix text-processing programs in Python.
    *   These will not be perfect clones; the requirements are relaxed to meet the deadline.
*   A driver program `src/tt.py` takes its input from the command line, and chooses which tool to call on.
*   Each tool is a Python function that takes the remaining command line arguments to do its work.


## What do the Text Tools do?

*   An explanation of each tool is given in the [examples directory](./examples/).
    *   Make your program's output match these examples as closely as you can.
    *   These documents show what happens in **best case** and **worst case** scenarios.
    *   The [test scripts](../testing/README.md) offer an easy way to compare your program's output to these examples.
*   If the tool's description under the examples directory doesn't have anything to say about a certain behavior (i.e. I've left it *undefined*), you have latitude in how you approach it.
    *   Mention such situations in your Software Development Plan.
*   Don't add extra features that aren't required.
    *   Unexpected features makes grading unnecessarily difficult.
    *   You can always revisit this project and improve it later!


### Text tools do not modify files

*   I repeat: this program *does not* change files!
    *   This program prints data found in files, sometimes with a twist.
*   If you open a file in any mode besides **read-only mode** `"r"` you're doing it wrong!
    *   The default mode used by `open()` *is* read-only; don't go out of your way to change it.


### Code organization

The tools are functions which are grouped into these modules:

| Tool   | Module                                        | Description
|--------|-----------------------------------------------|--------------------------------------------------
| `cat`  | [Concatenate.py](examples/Concatenate.md#cat) | Concatenate files and print on the standard output
| `tac`  | [Concatenate.py](examples/Concatenate.md#tac) | Concatenate and print files in reverse
| `cut`  | [CutPaste.py](examples/CutPaste.md#cut)       | Remove sections from each line of files
| `paste`| [CutPaste.py](examples/CutPaste.md#paste)     | Merge lines of files
| `grep` | [Grep.py](examples/Grep.md#grep)              | Print lines of files matching a pattern
| `head` | [Partial.py](examples/Partial.md#head)        | Output the first part of files
| `tail` | [Partial.py](examples/Partial.md#tail)        | Output the last part of files
| `sort` | [Sorting.py](examples/Sorting.md#sort)        | Sort lines of text files
| `wc`   | [WordCount.py](examples/WordCount.md#wc)      | Print newline, word, and byte counts for each file


*   **Do not** rename functions or modules.
*   **Do not** change the parameter list of the provided functions.
    *   Just fill in the blanks!
*   **Do not** write your own sorting algorithm; use the one provided by Python.
*   You *may* create extra helper functions and/or module(s) of your own.
    *   This isn't a sly hint; 99% of students complete the assignment without adding extra code.


## User Interface 

### Interface Design Principles

*   A simple program called a "driver" provides a unified interface.
    *   You are already familiar with this style of UI; this is how `git` works.
*   The driver accepts *command line arguments* and *files* as input.
    *   This program **must never** call `input()`!
*   It is the **user's responsibility** to provide correct arguments.
    *   Do not assume that files are located in a particular directory.
    *   Do not assume that filenames end in `.txt`.
*   Do not try to **fix** user errors.
    *   *Reasonable* measures are taken to avoid crashes.
    *   The best thing to do is report the error with a helpful message and quit.
    *   Good error messages let the user learn how to use the program without becoming frustrated.
    *   Otherwise, let Python's default error messages through to the user.


### Driver Program `src/tt.py`

*   The driver's job is to collect the user's input and dispatch control to the appropriate function.
    *   A good driver is short and simple, leaving the hard work to the tools.
*   When the user does not provide adequate information, a helpful message is displayed and the program exits.
*   The only module that can have direct access to the argument vector, `sys.argv`
    *   This module should pass necessary information from `sys.argv` to the functions for each tool
    *   Python's list slicing ~~may~~ will come in handy for handing only the necessary information from `sys.argv` to the relevant tool


### Command-Line Interface

This program will be run from the command line like so:

```bash
$ python src/tt.py TOOL [OPTIONS] FILENAME...
```

0.  `python` invokes the Python interpreter.
    *   You may need to use `python3` instead.
1.  Next comes the name of the driver program `src/tt.py`.
    *   This may vary depending on your CWD.
2.  `TOOL` is the name of one of the text tools listed in the table above.
    *   The name of the tool must be spelled exactly as shown in the table, in **lower-case**.
    *   When this doesn't happen, a usage message is printed and the program quits.
    *   The usage messages have already been written for you; study the starter code to learn how it works.
3.  Some tools take `[OPTIONS]`; when present, these always come between `TOOL` and `FILENAME`.
    *   Note that the user does not type the brackets; these indicate an *optional* part of the command.
    *   *Options* begin with a hyphen `-`. (e.g. `-n`)
        *   Some options take an argument of their own (e.g. `-n 3`)
    *   All command line arguments are seen by the program as *strings*.
        *   If an argument should be understood as a number, you need to convert it with `int()`.
        *   **Do not use `eval()`!** (see below).
4.  Each tool must be given at least **one** (1) filename.
    *   The ellipsis means that one *or more* filenames are accepted.
5.  When a *bad filename* is given, the program lets `open()` raise an exception (i.e. crash).
    *   It is actually *very* difficult to correctly deal with bad file *without* crashing.
    *   Even if you manage to avoid all possible crashes (you won't), there is nothing left for your program to do anyway; you may as well let it crash.
    *   Any error message that you could write will be less informative than what Python naturally displays; you may as well let it crash.
6.  In all other cases of bad input, print an error message and exit *without crashing*.  These cases include:
    *   Too few arguments.
    *   A non-existent tool is named.
    *   A non-numeric argument is given where a number is expected.


### Error Messages

*   *Mimic* the classic Unix text tools.
    *   In situations where they crash, so, too should your program.
*   Use `Usage.usage()` to present consistent error messages.
    *   The messages in this file are a hint for you.
    *   When you have a question about a tool's behavior, look for an answer in `Usage.py`.
*   Some errors are best detected in the *driver*.
*   Other errors are handled by the *tool*.


#### Too few arguments given to the driver

When the driver is invoked without a `TOOL`, `Usage.usage()` is called with no arguments to output its full message:

    $ python src/tt.py
    Error: Too few arguments

    Python Text Tools Usage:
    ========================
    ...


#### Invalid arguments given to the driver

When the driver is invoked with an invalid `TOOL`, `Usage.usage()` is called with no arguments to output its full message:

    $ python src/tt.py derp
    Error: derp is not a valid subcommand

    Python Text Tools Usage:
    ========================
    ...


#### File access errors

Let `open()` raise an error when a non-existent file is named:

    $ python src/tt.py cat data/DOES_NOT_EXIST
    Traceback (most recent call last):
      File "src/tt.py", line 69, in <module>
        cat(sys.argv[2:])
      File "/home/fadein/cs1440-assn2/src/Concatenate.py", line 4, in cat
        f = open(fl, 'r');
    FileNotFoundError: [Errno 2] No such file or directory: 'data/DOES_NOT_EXIST'


Let `open()` raise an error when a directory (or another non-file object) is named:

    $ python src/tt.py cat .
    Traceback (most recent call last):
      File "src/tt.py", line 19, in <module>
        cat(sys.argv[2:])
      File "/home/fadein/cs1440-assn2/src/Concatenate.py", line 4, in cat
        f = open(fil, 'r');
    IsADirectoryError: [Errno 21] Is a directory: '.'


Let `open()` raise an error when the user does not have permission to access a file:

    $ python src/tt.py cat /dev/mem
    Traceback (most recent call last):
      File "src/tt.py", line 19, in <module>
        cat(sys.argv[2:])
      File "/home/fadein/cs1440-assn2/src/Concatenate.py", line 4, in cat
        f = open(fil, 'r');
    PermissionError: [Errno 13] Permission denied: '/dev/mem'


#### Too few or incorrect arguments given to a tool

*   Detects and report cases where too few arguments are given to a tool.
    *   At least one input file is required by all tools.
*   Call `Usage.usage()` with the `error` and `tool` keyword arguments to print an appropriate error message.
    *   For example, when `cat` is invoked without filenames, call `Usage.usage(tool='cat', error="Too few arguments")` to display this message:
    *   ```
        $ python src/tt.py cat
        Error: Too few arguments

        tt.py cat|tac FILENAME...
                Concatenate and print files in order or in reverse
        ```
*   Other usage errors should be detected and reported by the affected tool.
*   *Hint* all modules that define tool functions should `import Usage`.


## The `>` redirection operator is a feature of your shell

*   As you study the files in [examples](./examples) you will come across commands that use the `>` symbol.
    *   You should recall this from a prevoius Shell Tutor lesson.
*   In a nutshell, `>` is the shell's *redirection operator*.
    *   It causes output that would be printed to the screen to instead be *redirected* into a file.
    *   This is a feature of your shell and is *not* something that you have to write in Python.
    *   In fact, neither the redirection operator nor the following filename appear in `sys.argv`
    *   Your program doesn't know that its output is redirected!



## Don't use evil `eval()`

This project requires you to convert strings such as `"10"` into integers.  While you were taught to do this with `eval()` in CS 1400, it is time to grow up and do this the big-kid way with type constructors:

*   `int()` for integers
*   `float()` for real numbers
*   `complex()` for complex numbers

The only one that you will need for this project is `int()`.

The problem is that `eval()` is **too** powerful.  It can execute *any* Python expression, including expressions that can erase your hard drive or install malware.  Your program accepts input from users, and users should [never be trusted](https://thepythonguru.com/python-builtin-functions/eval/#evil-eval).
