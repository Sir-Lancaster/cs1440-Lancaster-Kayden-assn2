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

### Head
```
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
```

## Phase 2: Implementation
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.

### Head
Implementation went well, no errors yet. 


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
