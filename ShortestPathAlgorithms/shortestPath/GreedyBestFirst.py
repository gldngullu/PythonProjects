
class GreedyBestFirst(object):
    distancesBetweenCities = [[0 for i in range(3)] for j in range(77)]
    straightLineDistances = [[0 for i in range(2)] for j in range(49)]
    # distancesBetweenCities = [[0 for i in range(3)] for j in range(5)]
    # straightLineDistances = [[0 for i in range(2)] for j in range(5)]
    startingCity = "Malaga"
    endingCity = "Valladolid"
    path = startingCity

    def readingTextFile(self):
        file = open("Assignment2SpainMap.txt", "r")
        file.readlines(13)
        b = file.readline()
        i = 0
        while b != '\n':
            b = b.split(" ")
            self.distancesBetweenCities[i] = b
            distanceValue = str(self.distancesBetweenCities[i][2]).strip("\n")
            self.distancesBetweenCities[i][2] = int(distanceValue)
            i = i+1
            b = file.readline()
        a = file.readlines(40)
        b = file.readline()
        i = 0
        while b != 'EOF':
            b = b.split(" ")
            self.straightLineDistances[i] = b
            straightLineValue = str(self.straightLineDistances[i][1]).strip("\n")
            self.straightLineDistances[i][1] = int(straightLineValue)
            i = i+1
            b = file.readline()

    def insertion_sort(self, arr):
        for i in range(len(arr)):
            cursor = arr[i]
            kek = arr[i][1]
            pos = i

            while pos > 0 and arr[pos - 1][1] > kek:
                # Swap the number down the list
                arr[pos] = arr[pos - 1]
                pos = pos - 1
            # Break and do the final swap
            arr[pos] = cursor
        return arr

    def greedyBestFirst(self):
        from anytree import Node, RenderTree
        rootNodeInfo = [self.startingCity, -1]
        root = Node(rootNodeInfo, parent=None)
        previousNode = root
        stack = []
        solutionNode = Node("No Solution")
        while True:
            # find neighbours
            neighbours = []
            parents = []
            for m in previousNode.ancestors:
                parents.append(m.name)
            for i in range(len(self.distancesBetweenCities)):
                if self.distancesBetweenCities[i][0] == self.startingCity:
                    isPresent = False
                    for j in parents:
                        if self.distancesBetweenCities[i][1] == j[0]:
                            isPresent = True
                    if isPresent:
                        continue
                    neighbours.append(self.distancesBetweenCities[i][1])
                elif self.distancesBetweenCities[i][1] == self.startingCity:
                    isPresent = False
                    for j in parents:
                        if self.distancesBetweenCities[i][0] == j[0]:
                            isPresent = True
                    if isPresent:
                        continue
                    neighbours.append(self.distancesBetweenCities[i][0])
            # find neighbour distances and sort
            neighbourDistances = [[0 for i in range(2)] for j in range(len(neighbours))]
            neighbourDistancesCount = 0
            for i in range(len(self.straightLineDistances)):
                for j in range(len(neighbours)):
                    if self.straightLineDistances[i][0] == neighbours[j]:
                        neighbourDistances[neighbourDistancesCount][0] = neighbours[j]
                        neighbourDistances[neighbourDistancesCount][1] = self.straightLineDistances[i][1]
                        neighbourDistancesCount += 1
            self.insertion_sort(neighbourDistances)
            # put them in stack
            for m in range(1, len(neighbourDistances)+1):
                stack.append(Node(neighbourDistances[len(neighbourDistances)-m], parent=previousNode))
            # create tree depending on stack
            if not stack:
                break
            closestCityNode = stack.pop()
            if closestCityNode.name[0] == self.endingCity:
                solutionNode = closestCityNode
                break
            self.startingCity = closestCityNode.name[0]
            previousNode = closestCityNode

        for pre, fill, node in RenderTree(root):
            ...
            print("%s%s" % (pre, node.name))
        solution = solutionNode.ancestors
        solutionPath = []
        for s in solution:
            solutionPath.append(s.name[0])
        solutionPath.append(solutionNode.name[0])
        print(solutionPath)


newChallenge = GreedyBestFirst()
newChallenge.readingTextFile()
newChallenge.greedyBestFirst()

