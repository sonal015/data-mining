class Classifier:
 def __init__( self, bucketPrefix, testBucketNumber, dataFormat,k ):
  """ a classifier will be built from files with the bucketPrefix
  excluding the file with textBucketNumber"""

  self.medianAndDeviation = []
  self.format = dataFormat.strip().split('\t')
  self.data = []
  self.k = k
  for i in range(1, 11):
   if i != testBucketNumber:
    filename = "%s-%02i" % (bucketPrefix, i)
    f = open(filename)
    lines = f.readlines()
    f.close()
    for line in lines:
     fields = line.strip().split('\t')
     ignore = []
     vector = []
     for j in range(len(fields)):

      if self.format[j] == 'num':
       vector.append(float(fields[j]))
      elif self.format[j] == 'comment':
       ignore.append(fields[j])
      elif self.format[j] == 'class':
       classification = fields[j]
     self.data.append((classification, vector, ignore))
   self.rawData = copy.deepcopy(self.data)
   self.vlen = len(self.data[0][1])
  for i in range(self.vlen):
   self.normalizeColumn(i)

 def testBucket(self, bucketPrefix, bucketNumber):
        """Evaluate the classifier with data from the file
        bucketPrefix-bucketNumber"""
        filename = "%s-%02i" % (bucketPrefix, bucketNumber)
        f = open(filename)
        lines = f.readlines()
        totals = {}
        f.close()
        for line in lines:
            data = line.strip().split('\t')
            vector = []
            classInColumn = -1
            for i in range(len(self.format)):
                  if self.format[i] == 'num':
                      vector.append(float(data[i]))
                  elif self.format[i] == 'class':
                      classInColumn = i
            theRealClass = data[classInColumn]
            classifiedAs = self.classify(vector)
            totals.setdefault(theRealClass, {})
            totals[theRealClass].setdefault(classifiedAs, 0)
            totals[theRealClass][classifiedAs] += 1
        return totals

def knn(self, itemVector):
 """returns the predicted class of itemVector using k
 Nearest Neighbors"""
 # changed from min to heapq.nsmallest to get the
 # k closest neighbors
 neighbors = heapq.nsmallest(self.k,
 [(self.manhattan(itemVector, item[1]), item)
 for item in self.data])
 # each neighbor gets a vote
 results = {}
 for neighbor in neighbors:
  theClass = neighbor[1][0]
  results.setdefault(theClass, 0)
  results[theClass] += 1
  resultList = sorted([(i[1], i[0]) for i in results.items()],
  reverse=True)
 #get all the classes that have the maximum votes
  maxVotes = resultList[0][0]
  possibleAnswers = [i[1] for i in resultList if i[0] == maxVotes]
 # randomly select one of the classes that received the max votes
  answer = random.choice(possibleAnswers)
 return( answer)