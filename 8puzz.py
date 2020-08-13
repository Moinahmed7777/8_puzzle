# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 02:09:52 2020

@author: Necro
*Astar need valid check and optimization

"""


import sys
if sys.platform == "win32":
    import psutil
    print("psutil", psutil.Process().memory_info().rss)
else:
    # Note: if you execute Python from cygwin,
    # the sys.platform is "cygwin"
    # the grading system's sys.platform is "linux2"
    import resource
    print("resource", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    

import time

#import resource


 
import math
from heapq import heappush, heappop,heapify

#### SKELETON CODE ####

## The Class that Represents the Puzzle

class PuzzleState(object):

    """docstring for PuzzleState"""

    def __init__(self, config, n, parent=None, action="Initial", cost=0):

        if n*n != len(config) or n < 2:

            raise Exception("the length of config is not correct!")

        self.n = n

        self.cost = cost

        self.parent = parent

        self.action = action

        self.dimension = n

        self.config = config

        self.children = []

        for i, item in enumerate(self.config):

            if item == 0:

                self.blank_row = i // self.n

                self.blank_col = i % self.n

                break

    def display(self):

        for i in range(self.n):

            line = []

            offset = i * self.n

            for j in range(self.n):

                line.append(self.config[offset + j])

            print(line)

    def move_left(self):

        if self.blank_col == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):

        if self.blank_col == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):

        if self.blank_row == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):

        if self.blank_row == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):

        """expand the node"""

        # add child nodes in order of UDLR

        if len(self.children) == 0:

            up_child = self.move_up()

            if up_child is not None:

                self.children.append(up_child)

            down_child = self.move_down()

            if down_child is not None:

                self.children.append(down_child)

            left_child = self.move_left()

            if left_child is not None:

                self.children.append(left_child)

            right_child = self.move_right()

            if right_child is not None:

                self.children.append(right_child)

        return self.children

# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
###########################################
# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None

     
  
###########################################
class Queue: 
    
    def __init__(self): 
        self.front = self.rear = None
        self.Q_dict= {}
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def EnQueue(self, item): 
        temp = Node(item) 
        self.Q_dict[temp.data.config] = 1  
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def DeQueue(self): 
          
        if self.isEmpty(): 
            return
        
        temp = self.front
        self.Q_dict.pop(temp.data.config)
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
            
    
###########################################
class Stack: 
      
     
    def __init__(self): 
        self.head = None
        self.S_dict= {}
    
    def isempty(self): 
        if self.head == None: 
            return True
        else: 
            return False
      
    
    def push(self,data): 
          
        if self.head == None: 
            self.head=Node(data)
            self.S_dict[self.head.data.config] = 1
              
        else: 
            newnode = Node(data) 
            self.S_dict[newnode.data.config] = 1
            #print(self.S_dict)
            newnode.next = self.head 
            self.head = newnode 
      
     
    def pop(self): 
          
        if self.isempty(): 
            return None
              
        else: 
             
            
            poppednode = self.head 
            #print(self.S_dict)
            self.S_dict.pop(poppednode.data.config)
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data 
      
     
    def peek(self): 
          
        if self.isempty(): 
            return None
              
        else: 
            return self.head.data 
      
    



    
            
            
            
            
            
            
            
###########################################            
def writeOutput():

    ### Student Code Goes here
    pass
def bfs_search(initial_state):

    """BFS search"""

    
    q = Queue() 
    q.EnQueue(initial_state)
    
    Explored_set=set()
    
    
    while not q.isEmpty():
        
        state=q.front.data
        Explored_set.add(state.config)
        q.DeQueue()
        
        if test_goal(state):
            print("Suc")
            
            calculate_total_cost(state,initial_state)
            
            break
        
        
        
        for neighbor in state.expand():   
            
            if test2(neighbor,q.Q_dict,Explored_set):
               q.EnQueue(neighbor)
        
        
    


def dfs_search(initial_state):

    
    s= Stack()
    s.push(initial_state)
    Explored_set=set()
    
    
    while not s.isempty():
        
        state=s.head.data
        Explored_set.add(state.config)
        
        s.pop()
        
        if test_goal(state):
            print("Suc")
            
            calculate_total_cost(state,initial_state)
            
            break
        
        
        
        for neighbor in state.expand()[::-1]:   
            
            if test2(neighbor,s.S_dict,Explored_set):
                
                s.push(neighbor)
               
def printheap(heap):
    for i,j,k in heap:
        print(i,j,k.config)              
        
    
def A_star_search(initial_state):

    """A * search"""
    

     
    h_dict={}
    heap=[]
    count = 0
    count2=0
     
    heappush(heap,((calculate_manhattan_dist(initial_state.config)+initial_state.cost),count,initial_state))
    Explored_set=set()
    
    while not len(heap)== 0:
        
        
        state = heappop(heap)[2]
        h_dict[state.config]=1
        Explored_set.add(state.config)
        
        
        if test_goal(state):
            print("Suc")
            
            calculate_total_cost(state,initial_state)
            
            break
        
        
        for neighbor in state.expand():   
            
            if test2(neighbor,h_dict,Explored_set):
                
                count=count+1
               
                
                fn = calculate_manhattan_dist(neighbor.config)+(neighbor.cost)
                
                heappush(heap,(fn,count,neighbor))
        
        h_dict.pop(state.config)
        count2 = count2+1 
        
        
               
        
        

def calculate_total_cost(state,initial_state):

    
    cost_d=1
    n =None
    l=[]
    dict3 = {initial_state.config: 1}
    n=state.parent
    a=state.action
    while True :
        if n.config in dict3:
            l.insert(0,a)
            break
        
        l.insert(0,a)
        cost_d=cost_d+1
        a=n.action
        n=n.parent
        
        
    print(l)
    print(cost_d)

def calculate_manhattan_dist(initial_state):

    
    initial_config = initial_state
    manDict = 0
    for i,item in enumerate(initial_config):
        if item == 0:
            continue
        prev_row,prev_col = int(i/ 3) , i % 3
        goal_row,goal_col = int(item /3),item % 3
        manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return manDict

def test_goal(puzzle_state):

    
    dict2 = {(0,1,2,3,4,5,6,7,8): 1}
    
    #if puzzle_state.config in dict2:
    if puzzle_state.config in dict2:
        return True
    else:
        return False
            
           
def test2(N,Dict,E):
    
    if Dict.get(N.config) != None or N.config in E:
        
        return False
    return True
    
    
# Main Function that reads in Input and Runs corresponding Algorithm

def main():
    
    

    sm = sys.argv[1].lower()

    begin_state = sys.argv[2].split(",")

    begin_state = tuple(map(int, begin_state))

    size = int(math.sqrt(len(begin_state)))

    hard_state = PuzzleState(begin_state, size)

    if sm == "bfs":

        bfs_search(hard_state)

    elif sm == "dfs":

        dfs_search(hard_state)

    elif sm == "ast":

        A_star_search(hard_state)

    else:

        print("Enter valid command arguments !")

if __name__ == '__main__':

    main()