********************************************************************************
*********************************** INSTRUCTIONS *******************************
********************************************************************************

1) Move all of the included Python files to the same directory as the Python
files you are using to work on Problem Set 1.

2) Run algorithm1D.py on the list given in problem1D.py to generate a trace
for the algorithm, which can be viewed using your existing visualizer.html
file.  This will let you experiment with the one-dimensional peak-finding
algorithm you saw in lecture.

3) Run algorithmModified.py on the matrix in your existing problem.py to
generate a trace for the algorithm, which can be viewed using your existing
visualizer.html file.  Note that the algorithm will display multiple "peak
found" symbols during one run of the algorithm --- this is because there are
"peak found" symbols generated both by the one-dimensional peak-finding
algorithm (which is run multiple times) and by the modified algorithm itself.

4) Run algorithmModified.py on the matrix in counter.py to see an example
where the algorithm fails.

********************************************************************************
******************************** DIRECTORY CONTENTS ****************************
********************************************************************************

algorithm1D.py

    The Python file containing the 1D peak-finding algorithm covered in
    Lecture 1.  When this Python file is run, it loads a one-dimensional peak
    problem from a file that the user specifies, and does the following:

        (1) Tests the algorithm on the desired peak problem, and outputs
            the results.

        (2) Generates a record of the execution of the algorithm, and outputs
            the execution traces to the file trace.jsonp.  These traces can
            be examined by displaying the file visualizer.html (included with
            your original Problem Set 1 code) in a browser.

    When run with no arguments (such as when run in IDLE), algorithm1D.py
    prompts the user for a file name to read the array from, defaulting to 
    problem1D.py.  It also takes a single optional argument (the filename to
    read the list from):

        python algorithm1D.py [<filename>]

algorithmModified.py

    The Python file containing the modified version of algorithm1, known as
    algorithm5.  When this Python file is run, it loads a peak problem from
    a file that the user specifies, and does the following:

        (1) Tests all four algorithms from the problem set AND the modified
            version of algorithm1 on the desired peak problem, and outputs
            the results.

        (2) Generates a record of the execution of all five algorithms, and
            outputs both the peak problem and the execution traces to the file
            trace.jsonp.  These traces can be examined by displaying the file
            visualizer.html (included with your original Problem Set 1 code)
            in a browser.

    When run with no arguments (such as when run in IDLE), algorithmModified.py
    prompts the user for a file name to read the matrix from, defaulting to 
    problem.py.  It also takes a single optional argument (the filename to
    read the matrix from):

        python algorithmModified.py [<filename>]

problem1D.py

    Thie file contains a template for entering in a one-dimensional peak
    problem. 

counter.py

    Thie file contains the counterexample for the modified algorithm given
    in the recitation notes.
