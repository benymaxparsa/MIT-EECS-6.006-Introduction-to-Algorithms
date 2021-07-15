import utils
import json
import algorithms
import algorithm1D
import peak
import trace
import sys

################################################################################
######################## Algorithm for 2D Peak Problems ########################
################################################################################

def algorithm5(problem, trace = None):
    # if it's empty, we're done 
    if problem.numRow <= 0 or problem.numCol <= 0:
        return None

    # the recursive subproblem will involve half the number of columns
    mid = problem.numCol // 2

    # information about the two subproblems
    (subStartC1, subNumC1) = (0, mid)
    (subStartC2, subNumC2) = (mid + 1, problem.numCol - (mid + 1))

    subproblems = []
    subproblems.append((0, subStartC1, problem.numRow, subNumC1))
    subproblems.append((0, subStartC2, problem.numRow, subNumC2))

    # find a 1D peak of the dividing column
    divider = problem.getSubproblem((0, mid, problem.numRow, 1))
    if not trace is None: trace.setProblemDimensions(divider)
    dividerPeak = algorithm1D.algorithm1(divider, trace)
    dividerPeak = problem.getLocationInSelf(divider, dividerPeak)
    if not trace is None: trace.setProblemDimensions(problem)

    # see if the peak we found on the dividing line has a better neighbor
    # (which cannot be on the dividing line, because we know that this
    # location is a peak on the dividing line)
    neighbor = problem.getBetterNeighbor(dividerPeak, trace)

    # this is a peak, so return it
    if neighbor == dividerPeak:
        if not trace is None: trace.foundPeak(dividerPeak)
        return dividerPeak
   
    # otherwise, figure out which subproblem contains the neighbor, and
    # recurse in that half
    sub = problem.getSubproblemContaining(subproblems, neighbor)
    if not trace is None: trace.setProblemDimensions(sub)
    result = algorithm5(sub, trace)
    return problem.getLocationInSelf(sub, result)

################################################################################
################################ The Main Method ###############################
################################################################################

def loadProblem(file = "problem.py", variable = "problemMatrix"):
    """
    Loads a matrix from a python file, and constructs a PeakProblem from it.
    """

    namespace = dict()
    with open(file) as handle:
        exec(handle.read(), namespace)
    return peak.createProblem(namespace[variable])

def main():
    if len(sys.argv) > 1:
        problem = loadProblem(sys.argv[1])
    else:
        problem = loadProblem(utils.getOpenFilename("problem.py"))

    # run all algorithms, gathering the traces and printing out the results as
    # we go
    algorithmList = [("Algorithm 1", algorithms.algorithm1),
                     ("Algorithm 2", algorithms.algorithm2),
                     ("Algorithm 3", algorithms.algorithm3),
                     ("Algorithm 4", algorithms.algorithm4),
                     ("Algorithm 5", algorithm5)]

    steps = []
    
    for (name, function) in algorithmList:
        tracer = trace.TraceRecord()
        peak = function(problem, trace = tracer)
        steps.append(tracer.sequence)
        
        status = "is NOT a peak (INCORRECT!)"
        if problem.isPeak(peak):
            status = "is a peak"

        print(name + " : " + str(peak) + " => " + status)

    # write the trace out to a file
    with open("trace.jsonp", "w") as traceFile:
        traceFile.write("parse(")

        json.dump({
            "input" : problem.array,
            "steps" : steps
        }, traceFile)

        traceFile.write(")")

if __name__ == "__main__":
    main()
