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

### Paste
* write a function that will open a file or multiple files, and will print them to the screen. 
* a good solution will take the columns of data print them to the screen seperating the columns with ','

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
head(args)
    Default line count

    if '-n' in args
        n_index = args.index(-n)
        if n_index + 1 < len(args)
            line_count_str = args[n_index + 1]
            if line_count_str isdigit
                line_count = int(line_count_str)
                args.pop(n_index)   Remove the '-n' option
                args.pop(n_index)   Remove the line count
            else:
                print("Invalid usage of the -n option. Line count must be an integer. Using the default line count of 10.")
                args.remove('-n')   Remove the '-n' option if the line count is not valid
        else:
            print("Invalid usage of the -n option. Line count is missing. Using the default line count of 10.")
            args.remove(-n)   Remove the '-n' option if no line count is provided

    for filename in args
        with open(filename) as file
            lines_read = 0
            for line in file
                print(line, end='')
                lines_read += 1
                if lines_read >= line_count
                    break   Stop reading after reaching the specified line count

```
### Grep
```
def grep(args):
initialize some variables
    pattern = args[0]
    option = None
    filenames = []

    if args[0] in ['-f', '-v']
        option = args[0]
        pattern = args[1]
        filenames = args[2:]
    else
        filenames = args[1:]

    for filename in filenames
        with open(filename, 'r') as file 
            for line in file
                line = line.strip()
                if option == '-f'
                    if pattern in line:
                        print(line)
                elif option == '-v'
                    if pattern not in line
                        print(line)
                else
                    if pattern in line
                        print(line)
```
### Word Count
```
use the cat function as a template
wc(filename):

    for filename in files:
        newline_count = 0
        char_count = 0
        word_count = 0
        with open(filename) as file:
            for line in file:
                newline_count += 1
                char_count += len(line)
                word_count += len(line.split())

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
cut(args)
    if args[0] == '-f'
        fields = args[1].split(',')
    else
        fields = ['1']
    for filename in args[2:]
        file = open(filename)
        for line in file
            line = line.strip()
            parts = line.split(',')
            
             Ensure that the indices in 'fields' are valid
            selected_fields = []
            for field_index in map(int, fields)
                if 1 <= field_index <= len(parts)
                    selected_fields.append(parts[field_index - 1])
                else:
                    selected_fields.append('')   Add an empty field for out-of-range indices
            
            print(','.join(selected_fields))
        file.close()
```
### Paste
```
paste(args)
     Initialize an empty list to store the lines from each file
    lines = []

     Read lines from each file and append them to the 'lines' list
    for file_path in args
        with open(file_path, 'r') as current_file
            current_lines = current_file.readlines()
            lines.append(current_lines)

    Determine the maximum number of lines among all files
    max_lines = max(len(lines[i]) for i in range(len(lines)))

    Pad shorter files with empty lines if necessary
    for i in range(len(lines))
        while len(lines[i]) < max_lines
            lines[i].append('\n')

    Paste the lines together with a tab delimiter and print the result
    for i in range(max_lines)
        combined_line = \tab.join(lines[j][i].rstrip('\n') for j in range(len(lines)))
        print(combined_line)

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
### Paste
I did not have as hard of a time with paste as I did with cut for some reason. With paste I didn't have to worry too much about some of the - options and just had to worry about making sure that the files were opened, or redirected correctly. Overall paste was one of my smoother ones. 
## Phase 3: Testing and Debugging
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

* For the test cases, I simply ran the command below. I ran each command from the ~/cs1440-assn2 directory. 
```
$ ./testing/FUNCTION_NAME.sh
```
* On the grep function when I would call it without the -f or -v option it would simply not print anything. The remedy was to put in some if statements to redefine the pattern variable so that it would know which of the args it was supposed to define as a pattern. after adding those statements it works fine. 
* on most, if not all, of the testing errors, the problem was that I had not created conditions for the -n, -f,... options and simply had to rewrite those statements so that they would run. 
* on cut I had not implemented anything so that if the line count index was larger than one of the files it would pad it with empty lines. 

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
        * The CutPaste.py file might be hard to understand. 
        *   Are there parts of your program which you aren't quite sure how/why they work?
            * the for statement on line 36 in the CutPaste.py can be hard for me to understand. 
        *   If a bug is reported in a few months, how long would it take you to find the cause?
            * Because everything is in modules I don't think it would take more than a few hours. Maybe a work day. 
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
            * I hope so.
        *   ...yourself in six month's time?
            * I should be able to make sense of it. ordered chaos and all that. 
    *   How easy will it be to add a new feature to this program in a year?
        * It sould not take more than a little while to add a new function. 
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
            * As long as it is run on the same version of python it should work. 
        *   ...the operating system?
            * there should be no problem with that.
        *   ...to the next version of Python?
            * Maybe not. It would depend on what changes are made to the next version. 
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
