
def find_parents(ancestors, node):
    #parents list
    parents = []
    #loop through ancestors
    for i in ancestors:
        #if second entry set is the node
        if i[1] == node:
            #append first entry to parent list
            parents.append(i[0])
     #if length of parent list is zero
    if len(parents) == 0:
        #return none
        return None
    else:
        #return parent list
        return parents



def earliest_ancestor(ancestors, starting_node):
    #grab parents
    parents = find_parents(ancestors,starting_node)
    
    #var for grand parents
    next_gen = []
   
    #if parents are none
    if parents is None:
        #retrun -1
        return -1
    
    #if length of parents is 1 and has parents
    first_parent = find_parents(ancestors, parents[0])
    if len(parents) == 1 and first_parent is not None:
        #set parents to its parents
        parents = first_parent
        
    
    # for each parent
    for i in parents: 
        #add parents to grand parents list
        if find_parents(ancestors, i) is not None:
            next_gen += find_parents(ancestors, i)
    
    #if after searching for parents the list is none next gen is parents
    if len(next_gen) == 0:
        next_gen = parents  
    
    #if at this point the list is still only two skip the loop and move to return logic
    if len(next_gen) != 2:
        #while grand parents is > 1
        while len(next_gen) > 1:
            #new parents var
            new_parents = []
            # for each grand parent
            for i in next_gen:
                #grab parent 
                par = find_parents(ancestors, i)
                #if parents is not None
                if par is not None: 
                    # append parents to new parents
                    new_parents += par
            #grand parents = new parents
            next_gen = new_parents

    #if len granparents is 1
    if len(next_gen) == 1: 
        #return gran parents
        return next_gen[0]
    #if grandparents 0 < grandparents 1
    if next_gen[0] < next_gen[1]:
        #return gp 0
        return next_gen[0]
    else:
        #return gp 1
        return next_gen[1]
    


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors,3))