'''
Created on Jan 20, 2016

@author: Rahul
'''
from BasicClass import *

inputfile = "input.txt"

'''
Basic Data Parsing
'''
#Create a basic class Object
basic = BasicClass(inputfile)
#get Friends of a user
print "Get Friends    :",basic.getFriends(userid=1234)

#Check if two friends are friends or not
print "Are Friends    :",basic.areFriend(userid_1=4243, userid_2=7567)

#Check if user 1 and user 2 have common friends
print "Have Mutual Friends    :",basic.haveMutualFriends(userid_1=121234,userid_2=4243)

'''
Find top potential Friends
'''
#get the count of Mutual Friends of user1 and user2
print "Count of mutual friends    :",basic.getMutualFriendCount(userid_1=1234, userid_2=4243)

#get the top 'count' potential common friends
print "Top 'count' potential Friends    :",basic.getPotentialFriends(userid=1312,count=3)



'''
Top Potential Friends large data sets
=======================================


Solution 1:
We can have the data put into hive database. The idea is that the huge file can be placed in the hdfs and a hive 
external table can be created over it with the userid column indexed.
Now to get the potential friends of a particulat user, we need to generate a hiveql , which would internally
get converted to map reduce jobs distriuted across number of nodes to take advantage of paraller processing.
We can increase the number of mappers and reducers based on the number of nodes we have to gain though put.


Solution 2:
*********
Spark
*********
Say our user is user0

create a rdd of the form:
user1,[friend1,friend2,friend3,friend4...]
user2,[friend1,friend2,friend3,friend4...]
user3,[friend1,friend2,friend3,friend4...]
usern,[friend1,friend2,friend3,friend4...]

The above rdd can be created by filtering out user which are friends with the given user using rdd.filter.


use map to get below

user0,[f1,f2,f4,f5...],user1,[friend1,friend2,friend3,friend4...]
user0,[f1,f2,f4,f5...],user2,[friend1,friend2,friend3,friend4...]
user0,[f1,f2,f4,f5...].user3,[friend1,friend2,friend3,friend4...]
user0,[f1,f2,f4,f5...],usern,[friend1,friend2,friend3,friend4...]



map(lamda x : x[0],x[2],x[1].intersect(x[3])
The above statement will resturn a rdd of the form user0,user1,<intersection of friends)

map(lambda x: (x[0],x[1]),[x2])
The above statement makes the tupes (user0,usern) as the key

Use flat map to blow up the common intersect friends values

map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
The above statements get the count of the common friends with user0 and usern

map(lambda (x,y): (y,x)).sortByKey()
this would sort the values based on the mututal count.

GEt the top count from the rdd while you call a collect.

The processing is fast as the data is distributed across the cluster nodes and we also take advantage over the 
spark fast processing engine.
'''

'''
It would be cool to get my hands dirty and implement this in real :)

--------------------
How to run the scenarios
---------------------
The project contains an input.txt, please paste the data in that file
I have commented out above every line what the function does, provide your input in the finctions
as parameter and let the code do the work.



 
'''