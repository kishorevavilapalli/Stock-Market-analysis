import matplotlib.pyplot as plt
import numpy as np
import csv
num_tweets = {}
with open("C:\Python27\mytweets.csv", "r") as csvfile:
       myfile = csv.reader(csvfile)
       for row in myfile:
              date = str(row[1]).split(" ")
              print date
              print date[2]
              if date[2] not in num_tweets.keys() :
                  num_tweets[date[2]] = 1
              else:
                  num_tweets[date[2]] += 1

y = num_tweets.values()
print(num_tweets)


# Data for plotting
x=[1,2,3,4,5,6,7] #days


# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='days', ylabel='number of tweets',
       title='daily number of tweets for altcoin')
ax.grid()

fig.savefig("test.png")
plt.show()