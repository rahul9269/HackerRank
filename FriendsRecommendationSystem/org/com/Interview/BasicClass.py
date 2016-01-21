'''
Created on Jan 20, 2016

@author: Rahul
'''
from _heapq import heappush, heappop
class BasicClass():
    def __init__(self, textfile):
        '''Create the hashmap of users and  friends 
           O(n) to create hashmap
           O(n) space complexity
           where n is the number of unique users
        '''
        
        self.friendmap = {}
        f = open(textfile,'rb')
        lines = f.readlines()
        for line in lines:
            l = line.split('\t')
            if l[0] not in self.friendmap:
                self.friendmap[int(l[0])] = map(int,str(l[1]).split(','))
        
    def getFriends(self,userid = None):
        '''
        O(1) lookup complexity. 
        '''
        if userid in self.friendmap:
            return self.friendmap[userid]
        else:
            print "User does not exist"
            return None
    
    def areFriend(self,userid_1,userid_2):
        '''
        O(1) lookup complexity. 
        '''
        if userid_1 in self.friendmap:
            if userid_2 in self.friendmap[userid_1]:
                return True
            
        return False
            
    def haveMutualFriends(self,userid_1,userid_2):
        '''
        O(1) lookup complexity. 
        O(ab) runtime complextiy , where a is the number of friends of user1 and b in the
        number of friedsn of user2
        space complexity is O(a+b)
        '''
        list_1 = None
        list_2 = None
        if userid_1 in self.friendmap:
            list_1 = self.friendmap[userid_1]
        if userid_2 in self.friendmap:
            list_2 = self.friendmap[userid_2]
        
        if list_1 and list_2:
            commonFriends = list(set(list_1) & set(list_2))
            if len(commonFriends) > 0:
                return  True
        
        return False
    
    def getMutualFriendCount(self,userid_1,userid_2):
        '''
        O(1) lookup complexity. 
        O(ab) runtime complextiy , where a is the number of friends of user1 and b in the
        number of friedsn of user2
        space complexity is O(a+b)
        '''
        list_1 = None
        list_2 = None
        commonFriends =[]
        if userid_1 in self.friendmap:
            list_1 = self.friendmap[userid_1]
        if userid_2 in self.friendmap:
            list_2 = self.friendmap[userid_2]
        
        if list_1 and list_2:
            commonFriends = list(set(list_1) & set(list_2))
        
        return len(commonFriends)
    
    def getPotentialFriends(self,userid,count):
        '''
        used a min heap to get the top 'count' potential friends of a user.
        space complexity of min heap is O(count)
        insert into heap q and delete takes log(count) time
        printing the list in reverse order to get users with maximum count: complexity O(n)
        Overall runtime complexity is O(n)
        '''
        if userid not in self.friendmap:
            print "User does not exist"
            return  None
        minh = []
        potentialfriends = [] 
        for key,value in self.friendmap.iteritems():
            if  userid != key:
                if not self.areFriend(userid, key):
                    c = self.getMutualFriendCount(userid,key)
                    if len(minh) >= count:
                        heappop(minh)
                    heappush(minh,(c,key))
        
        for friend in minh[::-1]:
            potentialfriends.append(friend[1])   
        return potentialfriends         
                   
        
        
        
        
    