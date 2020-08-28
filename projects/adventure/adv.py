from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#traversal graph
map_graph = {}

#map_graph={0:{'n':1, 's':2}, 1:{'s':0}, 2:{'n':0, 'w': '?'}}

#referance only:
# print(player.current_room.id)
# print(player.current_room.get_exits())
# player.travel('n')

#function to invert a direction
def invert_direction(direction):
    verts= {'n':'s', 's': 'n', 'e':'w', 'w':'e'}
    return verts[direction]

#function to grab a direction to travel
def grab_pole(room):
    poles = map_graph[room]
    if poles['n'] == '?':
        return 'n'
    if poles['w'] == '?':
        return 'w'
    if poles['e'] == '?':
        return 'e'
    if poles['s'] == '?':
        return 's'

#function to return path to closest '?'
def find_closest_unknown(starting):
    #create a queue
    q = Queue()
    #add starting to the q must be a list
    q.enqueue(starting)
    #found var = false
    found = False
    #while found is false
    while found is False:
        #pop from the q
        poped = q.dequeue()
        #directory = map_graph[pop[-1]]
        directory = map_graph[poped[-1]]
        #loop throug directory
        for i in directory:
            #if '?' exists
            if directory[i] == '?':
                #found = true
                found = True
                #return poped value
                return poped
            #else
            else:
                #copy poped value
                new_path = list(poped)
                #append copy with directory[i]
                new_path.append(directory[i])
                #add coppy to the q
                q.enqueue(new_path)
    
# print(find_closest_unknown([1]))

#function to revert paths of room numbers to path of directions
def num_to_pole(path):
    #new path var = []
    #loop through path
         
    pass

#var for next room to travel
#var for last room
#var to track if rooms are unexplored if true still have '?'

#while length of map graph is less than 500 and unexplored is true
    #break case:
    #if length of map graph is greater than 0
        # loop through map graph and all entries 
            # if '?' dosent exist unexplores is false

    
    #grab exits for current room


    #check to see if room exists in our graph:
    #the first time we visit a room we need to update map_graph:
    #if current room not in map graph
        #create a directions dict to be the value of the room 
        
        #directions = {}
        #for each value in exits
            #directions[i] = '?'
        
        #if this is not the first room we are in from the begining then update room numbers to directions as needed
        #if length of traversal_path is not 0
            #last move  = traversal_path[-1]
            #find inverse of move to add last visited room number to this directions dict
            #directions[inverse] = last room
            
            #update last rooms dict
            #to update = map_graph[last_room]
            #to update[last_move] = current room
        
        #add current room to map graph as key
        #map_graph[current] = directions 
    
    #find a direction to move
    #if length of exits is 1
        #call function to return path to closest '?'
        #move through the path
        #find a '?' and set  a next room var
    #else
        #find a '?' and set next room var
    
    #append traversal path with next room
    #move to next room


#what we need (brain storm):
#traversal graph to track rooms weve been to and log exits and there room numbers as traveled
#A bfs function that returns a path back to a room with an unsearched exit
#function to return opposite of direction traveled might not be needed
# main algorithm that loops us through rooms until traversal graph has all rooms and no unsearched rooms
    #in this loop we will need to:
    # add room to traversal graphc(dict) if doesnt alrady exist
    # add a dict that tracks the rooms exits as keys and room numbers as values 
        # for each room in traversal_graph if dosent exist
    #choose a direction and move 
    #update current room number to exit of prior room
    #add direction traveled to traversal_path
    # check exits of current room
    # if no exits use function to find nearest room with a unexplored exit
        #move to that room
    # ..... loop not nessisarily in order above
    #vars we might need:
    #current room id
    #prev room id


#################################
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
