import random
class Classifier:

 def buckets(filename, bucketName, separator, classColumn):
    "divinding data into buckets"

    numberOfBuckets = 10
    data = {}
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        if separator != '\t':
            line = line.replace(separator, '\t')
        category = line.split()[classColumn]
        data.setdefault(category, [])
        data[category].append(line)
    buckets = []
    for i in range(numberOfBuckets):
        buckets.append([])
    for k in data.keys():
        random.shuffle(data[k])
        bNum = 0
        for item in data[k]:
            buckets[bNum].append(item)
            bNum = (bNum + 1) % numberOfBuckets

    for bNum in range(numberOfBuckets):
        f = open("%s-%02i" % (bucketName, bNum + 1), 'w')
        for item in buckets[bNum]:
            f.write(item)
        f.close()

buckets("pimaSmall.txt", 'pimaSmall',',',8)

# 10 -fold cross validation


def tenfold(bucketPrefix, dataFormat):
 results = {}
 for i in range(1, 11):
   c = Classifier(bucketPrefix, i, dataFormat)
   t = c.testBucket(bucketPrefix, i)
 for (key, value) in t.items():
   results.setdefault(key, {})
 for (ckey, cvalue) in value.items():
   results[key].setdefault(ckey, 0)
   results[key][ckey] += cvalue

 # now print results
   categories = list(results.keys())
   categories.sort()
   print( "\n Classified as: ")
   header = " "
   subheader = " +"
 for category in categories:
   header += category + " "
   subheader += "----+"
   print (header)
   print (subheader)
 total = 0.0
 correct = 0.0
 for category in categories:
   row = category + " |"
 for c2 in categories:
  if c2 in results[category]:
   count = results[category][c2]
 else:
   count = 0
   row += " %2i |" % count
   total += count
 if c2 == category:
   correct += count
 print(row)
 print(subheader)
 print("\n%5.3f percent correct" %((correct * 100) / total))
 print("total of %i instances" % total)
tenfold("mpgData", "class num num num num num comment")