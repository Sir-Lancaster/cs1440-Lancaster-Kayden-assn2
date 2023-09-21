# CS 1440 Assignment 2: Text Tools

*   [Instructions](./instructions/README.md)
    *   [How to Submit this Assignment](./instructions/How_To_Submit.md)
    *   [Troubleshooting](./instructions/Troubleshooting.md)
*   [Project Requirements](./instructions/Requirements.md)
    *   [Output Examples](./instructions/examples)
    *   [Testing Scripts](./testing/README.md)

*Note: you may replace text in this file with your own notes.  For example, when seeking help from TAs or tutors replace this text with a description of your problem and push it to GitLab.*


## Get the starter code

*   Clone this repository and use it as a basis for your work.
    *   Run each of these commands one-at-a-time, without the `$` (that represents your shell's prompt).
    *   Replace `USERNAME` with your GitLab username, `LAST` and `FIRST` with your names as used on Canvas.

```bash
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn2 cs1440-assn2
$ cd cs1440-assn2
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn2.git
$ git push -u origin --all
```


## Overview

A client has sought DuckieCorp's services to process a large quantity of textual data.  Specifically, the data is in the form of a Comma Separated Values (CSV) file which is far too large to load as a spreadsheet in an application such as LibreOffice Calc or Microsoft Excel.

I explained to the client that it would be easier for them to install Linux and use its built-in text processing tools for this job.  Fortunately for our bottom line (and your job security), this client is adamant that installing Linux is out of the question.  Instead, DuckieCorp will recreate the classic suite of Unix *text processing tools* in Python.

I made a start at this project, but only got as far as creating a general outline and finishing the `usage()` routine before my other responsibilities at DuckieCorp became too great.  I will leave this project to you, my favorite intern, to complete.  If you do good work I am confident that this small job will turn into a standing contract.



## Running the starter code

All tools are invoked through the `src/tt.py` driver program, like this:

```bash
$ python src/tt.py TOOL [OPTIONS] FILE ...
```

If that gives you `Command not found`, try it with `python3` instead.

*   Not all tools take `OPTIONS`
*   All tools **do** take one or more `FILE`s
*   Study the [output examples](./instructions/examples) to see what each tool's output will look like
    *   Lines beginning with `$` represent what is typed into the shell
        *   When you run the same command, omit the `$`
    *   Your program's output should *essentially* match the examples, which cover both *good* and *bad* program behavior
    *   Extra leading or trailing white space is generally permissible, *except* where its presence changes the meaning of the output
    *   **Windows users** the numbers displayed by the *Word Count* tool may differ slightly from the examples
