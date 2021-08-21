def hasSingleCycle(array):
    # Write your code here.
    numElementsVisited = 0
    currentIdx= 0
    visitedNodes = {}
    while numElementsVisited < len(array):
    	if numElementsVisited > 0 and currentIdx == 0:
    		return False
    	numElementsVisited += 1
    	currentIdx = getNextIdx(currentIdx, array[currentIdx], len(array))
        if numElementsVisited != 6 and currentIdx in visitedNodes:
            return False
        else:
            visitedNodes[currentIdx] = True

	return True
		
def getNextIdx(currentIndex, value, maxLength):
	currentIndex = (currentIndex + value) % maxLength
	return currentIndex


