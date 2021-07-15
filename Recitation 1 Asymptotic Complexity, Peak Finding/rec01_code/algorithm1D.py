import utils
import json
import algorithms
import peak
import trace
import sys

################################################################################
####################### Algorithm for 1D Peak Problems #########################
################################################################################

def algorithm1(problem, trace = None):
    # if it's empty, we're done 
    if problem.numRow <= 0 or problem.numCol <= 0:
        return None

    # the algorithm only works for 1D peak problems --- if the dimensions are
    # wrong, we should just give up, because whatever answer we give will not
    # be correct
    if problem.numCol != 1:
        return None

    # the recursive subproblem will involve half the number of rows
    mid = problem.numRow // 2
    
    # information about the two subproblems
    (subStartR1, subNumR1) = (0, mid)
    (subStartR2, subNumR2) = (mid + 1, problem.numRow - (mid + 1))
    
    subproblems = []
    subproblems.append((subStartR1, 0, subNumR1, 1))
    subproblems.append((subStartR2, 0, subNumR2, 1))

    # see if the center location has a better neighbor
    center = (mid, 0)
    neighbor = problem.getBetterNeighbor(center, trace)

    # this is a peak, so return it
    if neighbor == center:
        if not trace is None: trace.foundPeak(center)
        return center
   
    # otherwise, figure out which subproblem contains the neighbor, and
    # recurse in that half
    sub = problem.getSubproblemContaining(subproblems, neighbor)
    if not trace is None: trace.setProblemDimensions(sub)
    result = algorithm1(sub, trace)
    return problem.getLocationInSelf(sub, result)

################################################################################
################################ The Main Method ###############################
################################################################################

def loadProblem(file, variable = "problemList"):
    """
    Loads a 1D peak problem from a python file, and constructs a PeakProblem
    from it.
    """

    namespace = dict()
    with open(file) as handle:
        exec(handle.read(), namespace)
    matrix = convertFrom1D(namespace[variable])
    return peak.createProblem(matrix)

def convertFrom1D(list):
    """
    Convert from a list to a matrix with the appropriate dimensions
    """

    return [[x] for x in list]

def main():
    if len(sys.argv) > 1:
        problem = loadProblem(sys.argv[1])
    else:
        problem = loadProblem(utils.getOpenFilename("problem1D.py"))

    # run all algorithms, gathering the traces and printing out the results as
    # we go
    algorithmList = [("Algorithm 1", algorithm1)]

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
