
class ArtificialNeuralNetwork(object):
    import numpy as np
    trainingSet = []
    validationSet = []
    testSet = []
    lengthOfSet = 784
    hiddenNeurons = [0 for j in range(532)]
    firstWeights = []
    secondWeights = []
    outputs = [0 for j in range(10)]
    learningRate = 0.1
    outputErrorDeltas = []
    numberOfSuccess = 0
    allFirstConnectedWeights = []
    allSecondConnectedWeights = []
    accumulateFirst = np.zeros((532, 784))
    accumulateSecond = np.zeros((10, 532))

    def readFile(self):
        with open('assignment5_train.csv') as csv:
            lines = csv.readlines()
            self.trainingSet = lines[1:29400]
            self.validationSet = lines[29401:33600]
            self.testSet = lines[33601:len(lines) - 1]

    def initialize(self):
        self.initializeTrainingSet()
        self.initializeTest()
        self.initializeValidation()
        self.findConnectedWeights()

    def initializeTrainingSet(self):
        import random
        for o in range(len(self.trainingSet)):
            self.trainingSet[o] = self.trainingSet[o].split(",")
            for k in range(self.lengthOfSet+1):
                if k == self.lengthOfSet:
                    self.trainingSet[o][k].strip("\n")
                self.trainingSet[o][k] = int(self.trainingSet[o][k])
        tempIndexes = []
        for m in range(len(self.trainingSet[0])):
            for n in range(len(self.hiddenNeurons)):
                indexOfWeight = [m, n]
                tempIndexes.append(indexOfWeight)
        self.firstWeights = [[0 for x in range(3)] for y in range(len(self.hiddenNeurons) * (len(self.trainingSet[0])-1))]
        for m in range(len(self.firstWeights)):
            self.firstWeights[m][0] = random.random()-0.5  # Random weights between -0.5 0.5
            self.firstWeights[m][1] = tempIndexes[m][0]
            self.firstWeights[m][2] = tempIndexes[m][1]

        tempIndexes = []
        for m in range(len(self.hiddenNeurons)):
            for n in range(len(self.outputs)):
                indexOfWeight = [m, n]
                tempIndexes.append(indexOfWeight)
        self.secondWeights = [[0 for x in range(3)] for y in range(len(self.hiddenNeurons) * (len(self.outputs)))]
        for m in range(len(self.secondWeights)-1):
            self.secondWeights[m][0] = random.random()-0.5
            self.secondWeights[m][1] = tempIndexes[m][0]
            self.secondWeights[m][2] = tempIndexes[m][1]

    def initializeTest(self):
        import random
        for o in range(len(self.testSet)):
            self.testSet[o] = self.testSet[o].split(",")
            for k in range(self.lengthOfSet+1):
                if k == self.lengthOfSet:
                    self.testSet[o][k].strip("\n")
                self.testSet[o][k] = int(self.testSet[o][k])
        tempIndexes = []
        for m in range(len(self.testSet[0])):
            for n in range(len(self.hiddenNeurons)):
                indexOfWeight = [m, n]
                tempIndexes.append(indexOfWeight)
        self.firstWeights = [[0 for x in range(3)] for y in
                             range(len(self.hiddenNeurons) * (len(self.testSet[0]) - 1))]
        for m in range(len(self.firstWeights)):
            self.firstWeights[m][0] = random.random()-0.5
            self.firstWeights[m][1] = tempIndexes[m][0]
            self.firstWeights[m][2] = tempIndexes[m][1]

        tempIndexes = []
        for m in range(len(self.hiddenNeurons)):
            for n in range(len(self.outputs)):
                indexOfWeight = [m, n]
                tempIndexes.append(indexOfWeight)
        self.secondWeights = [[0 for x in range(3)] for y in range(len(self.hiddenNeurons) * (len(self.outputs)))]
        for m in range(len(self.secondWeights) - 1):
            self.secondWeights[m][0] = random.random()-0.5
            self.secondWeights[m][1] = tempIndexes[m][0]
            self.secondWeights[m][2] = tempIndexes[m][1]

    def initializeValidation(self):
        import random
        for o in range(len(self.validationSet)):
            self.validationSet[o] = self.validationSet[o].split(",")
            for k in range(self.lengthOfSet+1):
                if k == self.lengthOfSet:
                    self.validationSet[o][k].strip("\n")
                self.validationSet[o][k] = int(self.validationSet[o][k])
        tempIndexes = []
        for m in range(len(self.validationSet[0])):
            for n in range(len(self.hiddenNeurons)):
                indexOfWeight = [m, n]
                tempIndexes.append(indexOfWeight)
        self.firstWeights = [[0 for x in range(3)] for y in
                             range(len(self.hiddenNeurons) * (len(self.validationSet[0]) - 1))]
        for m in range(len(self.firstWeights)):
            self.firstWeights[m][0] = random.random()-0.5
            self.firstWeights[m][1] = tempIndexes[m][0]
            self.firstWeights[m][2] = tempIndexes[m][1]

        tempIndexes = []
        for m in range(len(self.hiddenNeurons)):
            for n in range(len(self.outputs)):
                indexOfWeight = [m, n]
                tempIndexes.append(indexOfWeight)
        self.secondWeights = [[0 for x in range(3)] for y in range(len(self.hiddenNeurons) * (len(self.outputs)))]
        for m in range(len(self.secondWeights) - 1):
            self.secondWeights[m][0] = random.random()-0.5
            self.secondWeights[m][1] = tempIndexes[m][0]
            self.secondWeights[m][2] = tempIndexes[m][1]

    def sigmoid(self, x):
        import numpy as np
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        import numpy as np
        a = [float(i) / max(x) for i in x]
        e_x = np.exp(a)
        return np.array(e_x) / e_x.sum(axis=0)

    def findConnectedWeights(self):
        for i in range(len(self.hiddenNeurons)):
            k = i
            tempWeights = []
            for j in range(self.lengthOfSet):
                tempWeights.append(self.firstWeights[k][0])
                k += len(self.hiddenNeurons)
            self.allFirstConnectedWeights.append(tempWeights)

        for i in range(len(self.outputs)):
            k = i
            tempWeights = []
            for j in range(len(self.hiddenNeurons)):
                tempWeights.append(self.secondWeights[k][0])
                k += len(self.outputs)
            self.allSecondConnectedWeights.append(tempWeights)

    def calculateHiddenNeuron(self, inputs, iteration):
        import numpy
        connectionWeights = self.allFirstConnectedWeights
        inputs = numpy.array(inputs)
        connectionWeights = numpy.array(connectionWeights)
        inputs = inputs.astype('float64')
        self.hiddenNeurons = connectionWeights.dot(inputs)
        result = map(self.sigmoid, self.hiddenNeurons)
        self.hiddenNeurons = list(result)

        connectionWeights = self.allSecondConnectedWeights
        self.hiddenNeurons = numpy.array(self.hiddenNeurons)
        connectionWeights = numpy.array(connectionWeights)
        self.outputs = connectionWeights.dot(self.hiddenNeurons)
        result = self.softmax(self.outputs)
        self.outputs = list(result)
        resultingNumber = self.outputs.index(max(self.outputs))
        return resultingNumber

    def updateSecondWeights(self, targetOutput , inputs):
        import numpy as np
        deltaSecondWeights = []  # Length will be 5320
        targetOutputs = [0] * len(self.outputs)
        targetOutputs[targetOutput] = 1

        delta = np.matrix(np.subtract(targetOutputs, self.outputs))
        deltaWeights = np.transpose(delta).dot(np.matrix(self.hiddenNeurons))
        deltaWeights *= self.learningRate
        self.accumulateSecond += deltaWeights

        deltaHidden = self.hiddenNeurons * (1 - self.hiddenNeurons) * np.array(np.dot(delta, np.matrix(self.allSecondConnectedWeights)))
        deltaWeights = np.transpose(deltaHidden).dot(np.matrix(inputs))
        deltaWeights *= self.learningRate
        self.accumulateFirst += deltaWeights

    def mainAlgorithm(self):
        import numpy as np
        # Read the file
        self.readFile()
        # Initialize
        self.initialize()
        # Train
        isTrainingCompleted = False
        iterationsCompleted = False
        for iterNum in range(1000):
            if iterationsCompleted:
                break
            for i in range(len(self.trainingSet)):
                if isTrainingCompleted:
                    iterationsCompleted = True
                    break
                targetOutput = self.trainingSet[i][0]
                inputs = self.trainingSet[i][1:len(self.trainingSet[i])]
                inputs = np.array(inputs)/255  # Normalize
                # Go forward
                self.calculateHiddenNeuron(inputs, i)
                # Calculate Error
                self.updateSecondWeights(targetOutput,inputs)
                # self.updateFirstWeights(inputs)
                if i % 250 == 125:
                    self.allSecondConnectedWeights += self.accumulateSecond
                    self.accumulateSecond = np.zeros((10, 532))
                elif i % 250 == 0:
                    self.allSecondConnectedWeights += self.accumulateSecond
                    self.accumulateSecond = np.zeros((10, 532))
                    self.allFirstConnectedWeights += self.accumulateFirst
                    self.accumulateFirst = np.zeros((532, 784))
                if i % 500 == 0:
                    numberOfSuccesses = 0
                    for j in range(len(self.validationSet)):
                        targetOutput = self.validationSet[j][0]
                        inputs = self.validationSet[j][1:len(self.validationSet[j])]
                        inputs = np.array(inputs)/255   # Normalize
                        # Go forward
                        result = self.calculateHiddenNeuron(inputs, targetOutput)
                        if result == targetOutput:
                            numberOfSuccesses += 1
                    print("Success rate for iteration ", iterNum, " ", i, " is " , numberOfSuccesses/len(self.validationSet))
                    if numberOfSuccesses/len(self.validationSet) > 0.76:
                        isTrainingCompleted = True
        # Test
        numberOfSuccesses = 0
        for j in range(len(self.testSet)):
            targetOutput = self.testSet[j][0]
            inputs = self.testSet[j][1:len(self.testSet[j])]
            inputs = np.array(inputs)/255  # Normalize
            # Go forward
            result = self.calculateHiddenNeuron(inputs, targetOutput)
            if result == targetOutput:
                numberOfSuccesses += 1
        print("Success rate for the algorithm is " , numberOfSuccesses / len(self.testSet))


test = ArtificialNeuralNetwork()
test.mainAlgorithm()



