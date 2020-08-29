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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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

#test graph
# map_graph={0:{'n':1, 's':2}, 1:{'s':'?'}, 2:{'n':0, 'w': 1}}

#referance only:
# print(player.current_room.id)
# print(player.current_room.get_exits())
# player.travel('n')

#function to invert a direction
def invert_direction(direction):
    verts= {'n':'s', 's': 'n', 'e':'w', 'w':'e'}
    return verts[direction]

#function to grab a direction to travel
def grab_move(room):
    poles = map_graph[room]
    if 's' in poles and poles['s'] == '?':
        return 's'
    if 'e' in poles and poles['e'] == '?':
        return 'e'
    if 'w' in poles and poles['w'] == '?':
        return 'w'
    if 'n' in poles and poles['n'] == '?':
        return 'n'

#function to return path to closest '?'
def find_closest_unknown(starting):
    exists= False
    for i in map_graph:
        if '?' in map_graph[i].values():
            exists = True
    if exists == False:
        return None    
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
    


#function to revert paths of room numbers to path of directions
def num_to_direction(path):
    #new path var = []
    new_path = []
    #loop through path
    #for i in  length  of path -1
    for i in range(len(path) -1):
        #directory = map_graph[i]
        directiory = map_graph[path[i]]
        #for pole, num in directory
        for x, y in directiory.items():
            if y == path[i + 1]:
                new_path.append(x)
    #return new path
    return new_path             

#function to check if a '?' exists in map_graph
def unexplored_exists():
    exists = False
    for i in map_graph:
        if '?' in map_graph[i].values():
            exists = True
    return exists  

#function to check if '?' exists i a given room
def unexplored_exits_room(room):
    exists = False
    if '?' in map_graph[room].values():
        exists = True
    return exists

#set up inital/starting room in our map_graph
initial_exits = player.current_room.get_exits()
initial_room = player.current_room.id
initial_directions = {}
for i in initial_exits:
    initial_directions[i] = '?'
map_graph[initial_room] = initial_directions


#var for preveous room
prev_room = None
#var to track if rooms are unexplored if true still have '?'
unexplored = True

# begin traversal aka main loop
while len(map_graph) < len(room_graph) and unexplored is True:
    #set our break case unexplored = False when no '?'
    unexplored = unexplored_exists()
    
    #grab exits to current room
    exits = player.current_room.get_exits()

    #check if room is in our map graph
    #if its not in our graph
    if player.current_room.id not in map_graph: 
        #create a new entry in map graph
        #create a new directories dict to be the entry of the room
        directoties = {}
        #fill directories with the rooms exits as keys and '?' as values
        for i in exits:
            directoties[i] = '?'
        #set prev room to the inverse of the direction we travled in directories
        last_move = traversal_path[-1]
        last_move_inverse = invert_direction(last_move)
        directoties[last_move_inverse] = prev_room
        #add room to map_graph with directories as values
        map_graph[player.current_room.id] = directoties
        #update prev rooms exits to current room number
        last_room = map_graph[prev_room]
        last_room[last_move] = player.current_room.id
    else:
        if len(traversal_path) > 0:
            last_move = traversal_path[-1]
            last_visited_room = map_graph[prev_room]
            if last_visited_room[last_move] == '?':
                last_visited_room[last_move] = player.current_room.id

    
    #find a direction to move
    #next room var
    next_room = ''
    
    
    room_unexplored = unexplored_exits_room(player.current_room.id)
    # if this is our first room just set next room
    if len(traversal_path) == 0:
        #find '?' room set next room var
        next_room = grab_move(player.current_room.id)
    #if this room only has one exit
    # if len(exits) == 1 and len(traversal_path) == 0:
    elif room_unexplored == False:
        #find path to closest room with '?'
        move_path = find_closest_unknown([player.current_room.id])
        if move_path != None:
            move_directions = num_to_direction(move_path)
            #move through path updating prev room and traversal path
            for i in move_directions:
                traversal_path.append(i)
                prev_room = player.current_room.id
                player.travel(i)
            
            #find '?' room set next room var
            next_room = grab_move(player.current_room.id)
    else:
        #find '?' room set next room var
        next_room = grab_move(player.current_room.id)

    #append traversal_path with direction
    if next_room is not None and next_room is not '':
        traversal_path.append(next_room)
        #set prev room to current room
        prev_room = player.current_room.id
        #move to next room
        player.travel(next_room)
    
    # print(next_room)
    # print(player.current_room.id)
    # print(traversal_path)
    # print(map_graph)
    
    # print(len(map_graph))





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
