import random

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")
        # Create friendships
        # Generate ALL possible friendships
        # Avoid duplicate friendships 
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # user_id == user_id_2 cannot happen
                # if friendship between user_id and user_id_2 already exists
                #   dont add friendship between user_id_2 and user_id
                possible_friendships.append( (user_id, friend_id) )
            
        # Randomly select X friendships
        # the formula for X is  num_users * avg_friendships  // 2 
        # shuffle the array and pick X elements from the front of it
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        #make a queue
        queue = Queue()
        #add userid to q
        queue.enqueue(user_id)
        #while q is not empty
        while queue.size() > 0:
            #pop value from q
            poped = queue.dequeue()
            #if the poped value is not in visited
            if poped not in visited:
                #grab friends of poped value
                friends = self.friendships[poped]
                #if poped value is equal to userid
                if poped == user_id:
                    #visited[poped] = [userid]
                    visited[poped] = [user_id]
                
                else:
                    #if userid in friends
                    if user_id in friends:
                        #visited[poped]= [userid, poped]
                        visited[poped] = [user_id, poped]
                    else:
                        #found bool false
                        found = False
                        #while found is false
                        for i in friends:
                            if i in visited and found is False:
                                visited[poped] = visited[i] + [poped]
                                found = True
                #for each value in friends
                for i in friends:
                    #add value to q
                    queue.enqueue(i)  
                            
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    cg = SocialGraph()
    num_users = 1000
    ave_friends = 5
    cg.populate_graph(num_users, ave_friends)
    connections = cg.get_all_social_paths(1)
    print(f"{(len(connections)/num_users) * 100}%")
    con_leng = 0
    
    for i in connections:
        con_leng += len(connections[i])
    print(f"{con_leng/len(connections)}")
