# Software Development Plan

## Phase 0: Requirements Analysis
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
*   [ ] List the algorithms that will be used (but don't write them yet).



### Head
* Write a function that will open a file read the specified number of lines of the file and print them to the screen, and close the file.
* A good solution will print the number of lines from a specified file. if the number of lines is not specified, then the function will print the first 10 lines. 
* Knowns:
    * I know what the head command does in the command line.
    * I can use the same function as the cat file to open and read the file. 
    * I know how to modify the cat function to ensure the file does not read more than a specified amount.
* I don't think that I will have many, if any, challenges with this particular function. 
* The output will take the form of text printed to the screen. 

### Grep
* Write a function that will open a file and look for words that match a pattern. 
* A good solution will be able to provide similar output to the grep command on the command line. It will require the name of the file to be opened and the pattern to be searched for.

### Word Count
* Write a function that will open a file, count the number of newline, word and bytes in the file.
* A good solution will be able to print the desired information to the screen without error, and will take arguments from the command line to complete the task.

* Knowns:
    * take args from the command line
    * open a file
    * parse through each line of a file. 
* Unknowns:
    * how to count newlines, or bytes of a file. 

### Sort
* write a function that, when given a list of files, sorts them in lexical order. 
* A good solution will be able to take command line arguments, sort the files given in lexical order, and close the file. 
* Knowns:
    * open a file,
    * search for a pattern
* unknowns:
    * pythons built in sorting algorithms.

### Tac
* Write a cunction that will open a file, and print the contentents to the screen in reverse. 
* A good solution will take the file and either store the contents in the memory, or will itterate through the file starting at the bottom and going to the top. 
* Knowns:
    * Opening and printing the contents of a file to the screen
* Unknowns: 
    * How to reverse the order that the lines are printed to the screen. 

### Tail
* Write a function that will open a file and only print the last part of a file.
* A good solution will take the arguments from the command line, open the file, print the end of the file, then close the file. 
* knowns:
    * Printing the contents of a file, and limiting the contents to only the first 10 lines. 
* Unknowns:
    * how to limit it to be only the last ten lines. 
* I think I can use the tac reversal algorithm to reverse the lines and then print the first 10 lines of the reversed function. 

### Cut
* Write a function that will open a file, and extract lines from the file and print them to the screen, merging the lines together.
* a good solution will take the commands from the command line argument and will print the expected results.

## Phase 1: Design
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing.

### tt.py
* all of the function calls are the same:
```
if sys.argv[1] is function_name
    call function_name and pass other sys.argv arguments to it
elif sys.argv[1] is different_function
    call different_function(sys.argv[other arguments])
    etc...
```
### Head
```
import sys

head(args, line_count)
    if line_count = 0         this will make it so that if head is called without a line specification it will print the first 10.
        line_count == 10;
    for filename in args
        file = open(filename) 
        for line in file
            print(line, end='')
            if line <= line_count in args   if statement will prevent the file from being read past the variable line_count.
                line += 1
        file.close()

need to adjust for the adding of the sys import statement:

head(args)
    if sys.argv[4] = empty space
        line_count == 10
    else 
        line_count == sys.argv[4]
```
### Grep
```
def grep(args):
    for filename in args:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    if pattern is None or pattern in line:
                        print(line, end='')
        except FileNotFoundError
            print(filename No such file or directory)
```
### Word Count
```
use the cat function as a template
wc(filename):
    for filename in args:
        file = open(filename)  # Just let open() crash if filename is invalid
        for line in file:
            newline_count += 1
        for line in file
            if line != white space
                Char_count += 1
        for line in file
            if line == whitespace
                Word_count +=1
        print("the xxx count is: ", xxxx_count) # let xxxx be the name of whatever this line is counting. There will be three print lines for the different variables.

        file.close()
```
### Sort
```
sort(files)
    Initialize an empty list called "lines"
    
    For each filename in files
        Initialize an empty list called "file_lines"
        Open the file with the given filename
        
        For each line in the opened file
            Append the line to the "file_lines" list
        
        Close the file
        
        Append "file_lines" to the "lines" list

    Sort the "lines" list alphabetically
    
    For each line in the sorted "lines" list
        Print the line to the standard output
```

### Tac
```
tac(args)
    for filename in reversed args
        file = open(filename)  # Just let open() crash if filename is invalid
        with open(filename) as file
            lines = the lines of the file
            lines of file reversed
            for line in lines
                print(lines, end = '')
            file.close()
```

### Tail
```
tail(args)
    line_count = 10  # Default line count

    if len(args) > 2 and args[0] == '-n'
        try:
            line_count = int(args[1])  # Get the line count from the command-line arguments
        except ValueError:
            print("Using default.")
        args = args[2:]  # Remove the first two command-line arguments (-n and the line count)

    for filename in args:
        lines = []  # Initialize an empty list to store the last N lines
        with open(filename) as file:
            for line in file:
                lines.append(line)  # Append each line to the list
                if len(lines) > line_count:
                    lines.pop(0)  # Remove the first line if the list exceeds N lines
        for line in lines:
            print(line, end='')

```
### Cut
```
import sys

def cut(args)
    if sys.argv[0] == '-f'
        fields = sys.argv[1].split[',']
    else
        fields = ['1']
    for filename in args
        open(filename)
        for line in file
            line.strip()
            parts = line.split(',')
            selected_fields = [parts[i - 1] for i in fields]
            print(selected_fields organized into columns)
        file.close()
    
```

## Phase 2: Implementation
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.

### Head
Implementation went well.

### Grep 
Good planning makes this go smooth.

### tt.py
So far so good, I will add the other function calls as they are designed.

### Word Count
after tinkering with it for a little while, I was able to get it to work propperly. With the pseudocode i used in the design it did not count the number of words or characters intil i implemented the len() function.

### Sort
implementation went perfectly. 

### Tac
The tac function appears to be working properly, but now the head() function is acting up. I will have to deal with that when i get to phase 3.

### Cut
I tried to get it to work several times, but ultimately had to scrap my first design and redesign another one that worked. Some things will have to be cleaned up in the testing phase. 
## Phase 3: Testing and Debugging
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 4: Deployment
*(5% of your effort)*

Deliver:

*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
