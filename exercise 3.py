from math import sqrt

users2 = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
 "Ben": {"Taylor Swift": 5, "PSY": 2},
 "Clara": {"PSY": 3.5, "Whitney Houston": 4},
 "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}

def computeDeviations(self):
 # for each person in the data:
 # get their ratings
 for ratings in self.data.values():
  for (item, rating) in ratings.items():
   self.frequencies.setdefault(item, {})
   self.deviations.setdefault(item, {})
 # for each item2 & rating2 in that set of ratings:
  for (item2, rating2) in ratings.items():
    if item != item2:
     self.frequencies[item].setdefault(item2, 0)
     self.deviations[item].setdefault(item2, 0.0)
     self.frequencies[item][item2] += 1
     self.deviations[item][item2] += rating - rating2

  for (item, ratings) in self.deviations.items():
      for item2 in ratings:
        ratings[item2] /= self.frequencies[item][item2]

{'PSY': {'Taylor Swift': -2.0, 'Whitney Houston': -0.75},
 'Taylor Swift': {'PSY': 2.0, 'Whitney Houston': 1.0},
  'Whitney Houston': {'PSY': 0.75, 'Taylor Swift': -1.0}}

def slopeOneRecommendations(self, userRatings):
 recommendations = {}
 frequencies = {}
 # for every item and rating in the user's recommendations
 for (userItem, userRating) in userRatings.items():
  # for every item in our dataset that the user didn't rate
  for (diffItem, diffRatings) in self.deviations.items():
   if diffItem not in userRatings and \
   userItem in self.deviations[diffItem]:
    freq = self.frequencies[diffItem][userItem]
    recommendations.setdefault(diffItem, 0.0)
    frequencies.setdefault(diffItem, 0)
 # add to the running sum representing the numerator
 # of the formula
 recommendations[diffItem] += (diffRatings[userItem] +
 userRating) * freq
 # keep a running sum of the frequency of diffitem
 frequencies[diffItem] += freq
 recommendations = [(self.convertProductID2name(k),
 v / frequencies[k])
 for (k, v) in recommendations.items()]

 # finally sort and return
 recommendations.sort(key=lambda artistTuple: artistTuple[1],
 reverse = True)
 return recommendations

 r.slopeOneRecommendations(r.data['1'])
[('Entertaining Angels: The Dorothy Day Story (1996)', 6.375),
 ('Aiqing wansui (1994)', 5.849056603773585),
 ('Boys, Les (1997)',5.644970414201183),
 ("Someone Else's America (1995)",5.391304347826087),
 ('Santa with Muscles (1996)', 5.380952380952381),
('Great Day in Harlem, A (1994)', 5.275862068965517)]
