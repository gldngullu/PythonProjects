
class GeneticAlgorithm(object):
    coordinationInfo = []
    generationSize = 100
    generation = []
    bestDistanceFound = float("inf")
    bestPathFound = []

    def readingTextFile(self):
        file = open("Assignment3Berlin52.txt", "r")
        b = file.readline()
        while b != "NODE_COORD_SECTION\n":
            b = file.readline()
        b = file.readline()
        i = 0
        while b != 'EOF\n':
            b = b.split(" ")
            self.coordinationInfo.append(b)
            self.coordinationInfo[i][0] = int(self.coordinationInfo[i][0])
            self.coordinationInfo[i][1] = float(self.coordinationInfo[i][1])
            self.coordinationInfo[i][2] = float(str(self.coordinationInfo[i][2]).strip("\n"))
            i = i+1
            b = file.readline()

    def calculateDistance(self, list1, list2):
        import math
        distanceBetween = math.sqrt(((list2[1]-list1[1]) ** 2) + ((list2[2]-list1[2]) ** 2))
        return distanceBetween

    def calculateTotalDistance(self, list1):
        totalDistance = 0
        for i in range(len(self.coordinationInfo) - 1):
            city1 = self.getCoordinationInfo(list1[i])
            city2 = self.getCoordinationInfo(list1[i + 1])
            totalDistance += self.calculateDistance(city1, city2)
        return totalDistance

    def getCoordinationInfo(self, cityNumber):
        for i in range(len(self.coordinationInfo)):
            if self.coordinationInfo[i][0] == cityNumber:
                return self.coordinationInfo[i]

    def bubbleSort(self, arr, generation):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    generation[j], generation[j+1] = generation[j+1], generation[j]
        return arr

    def pickParent(self, bordersInfo):
        import random
        randnum = random.random()
        parent = self.generation[0]
        for i in range(len(bordersInfo)):
            if randnum > bordersInfo[i]:
                parent = self.generation[i]
            else:
                break
        return parent

    def crossover(self, parent1, parent2):
        import random
        isCrossover = random.random()
        if isCrossover < 1:
            # print(parent1)
            # print(parent2)
            geneNumsFromParent1 = -1
            lastIntervalStart = -1
            if len(parent1) % 2 == 0:
                geneNumsFromParent1 = (len(parent1)-2)/2
                lastIntervalStart = len(parent1)/2
            elif len(parent1) % 2 == 1:
                geneNumsFromParent1 = (len(parent1)-1)/2
                lastIntervalStart = (len(parent1)-1)/2
            geneNumsFromParent1 = random.randint(2, geneNumsFromParent1)
            intervalStart = random.randint(1, len(parent1)-3)
            lowerBound = intervalStart
            upperBound = random.randint(intervalStart+1, len(parent1)-2)
            child = [None] * len(parent1)
            numbersFromSecond = []
            for i in range(len(parent1)-1):
                if upperBound >= i >= lowerBound:
                    child[i] = parent1[i]
                else:
                    numbersFromSecond.append(parent1[i])
            orderedNumbersFromSecond = []
            for i in range(len(parent2)-1):
                for j in range(len(numbersFromSecond)):
                    if parent2[i] == numbersFromSecond[j]:
                        orderedNumbersFromSecond.append(parent2[i])
                        continue
            t = 0
            child[len(child)-1] = 1
            for i in range(len(child)):
                if child[i] is None:
                    child[i] = orderedNumbersFromSecond[t]
                    t += 1
        else:
            pickOne = random.randint(0, 1)
            if pickOne == 0:
                child = parent1
            else:
                child = parent2
        return child

    def mutation(self, child):
        import random
        randomNum = random.random()
        if randomNum <= 0.05:
            firstPick = random.randint(1, len(child)-2)
            secondPick = random.randint(1, len(child)-2)
            while secondPick == firstPick:
                secondPick = random.randint(1, len(child) - 2)
            if firstPick > secondPick:
                firstPick, secondPick = secondPick, firstPick
            numsToSwap = []
            for i in range(firstPick, secondPick):
                numsToSwap.append(child[i])
            count = len(numsToSwap)-1
            for i in range(firstPick, secondPick):
                child[i] = numsToSwap[count]
                count -= 1
        return child

    def mutationTowardsEnd(self, child):
        import random
        randomNum = random.random()
        if randomNum <= 0.5:
            for i in range(10):
                firstPick = random.randint(1, len(child)-2)
                secondPick = random.randint(1, len(child)-2)
                child[firstPick], child[secondPick] = child[secondPick], child[firstPick]
        return child

    def ga(self):
        import random
        # Initialize generation
        for i in range(self.generationSize):
            tempList = []
            tempList.append(1)
            for j in range(len(self.coordinationInfo)-1):
                tempList.append(-1)
            tempList.append(1)
            self.generation.append(tempList)
        # Create and add the shuffled part
        for k in range(self.generationSize):
            tempList = []
            for i in range(len(self.coordinationInfo)-1):
                tempList.append(i+2)
            random.shuffle(tempList)
            for i in range(len(self.coordinationInfo)-1):
                self.generation[k][i+1] = tempList[i]
        # Calculate fitnesses
        for k in range(2000):
            currentFitness = []
            for i in range(len(self.generation)):
                tempFitness = 0
                for j in range(len(self.generation[i])-1):
                    city1 = self.getCoordinationInfo(self.generation[i][j])
                    city2 = self.getCoordinationInfo(self.generation[i][j+1])
                    tempFitness += self.calculateDistance(city1, city2)
                currentFitness.append(tempFitness)
                # Sort the scores of generation and calculate probability of mating
                # _Invert scores for more logical comparison
            sumFitness = 0
            for i in range(len(currentFitness)):
                currentFitness[i] = 1/currentFitness[i]
                sumFitness += currentFitness[i]
            for i in range(len(currentFitness)):
                currentFitness[i] = currentFitness[i]/sumFitness
            currentFitness = self.bubbleSort(currentFitness, self.generation) # Liste eleman toplamları 1'e eşit şu an
            # print(currentFitness)
            bordersForProbability = []
            tempBorder = currentFitness[0]
            for i in range(len(currentFitness)-1):
                bordersForProbability.append(tempBorder)
                tempBorder += currentFitness[i+1]
            bordersForProbability.append(1)
            totalDistance = self.calculateTotalDistance(self.generation[len(self.generation)-1])
            previousBestDistance = -1
            if totalDistance < self.bestDistanceFound:
                previousBestDistance = self.bestDistanceFound
                self.bestDistanceFound = totalDistance
                self.bestPathFound = self.generation[len(self.generation)-1]
            # New Generation Creation
            newGeneration = []
            for i in range(int(len(self.generation)-(len(self.generation)/5))):
                parent1 = self.pickParent(bordersForProbability)
                parent2 = self.pickParent(bordersForProbability)
                child = self.crossover(parent1, parent2)
                if k > 500:
                    child = self.mutationTowardsEnd(child)
                else:
                    child = self.mutation(child)
                newGeneration.append(child)
            for i in range(int(len(self.generation)-(len(self.generation)/5)), len(self.generation)):
                newGeneration.append(self.generation[i])
            self.generation = newGeneration
            if self.bestDistanceFound < previousBestDistance:
                print("Generation", k)
                print(self.bestPathFound)
                print(self.bestDistanceFound)
            if self.bestDistanceFound < 9000:
                print("Solution Found!")
                break
            if k == 1999:
                print("No solution found :(")


test = GeneticAlgorithm()
test.readingTextFile()
test.ga()

