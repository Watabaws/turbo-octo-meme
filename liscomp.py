def union(a, b):
    return [x for x in a+b] #add the lists and iterate through everything in that

print union([1,2,3], [2,5,6])

def intersection(a, b):
   return [x for x in a if x in b] #go through a and only return the items also in b

print intersection([1,2,3,4,7], [4,7,8])

def set_diff(u, a):
    return [x for x in u if x not in a] #go through u and only return the items not in a

print set_diff([1,2,3,4,5,6,7,8], [1,3,5,7])


def sym_diff(a, b):
    avoid = intersection(a,b) #Make a list of all the items in BOTH the lists
    return [x for x in a+b if x not in avoid] #go through both lists, and return the items that wouldn't be in the intersection

print sym_diff([1,2,3,4,5,6,7,8], [1,3,5,7,10,12,14])

def cartes_prod(a,b):
    return [[x,y] for x in a for y in b] #Go through a then go through b and return the ordered pair (this is a nested for loop!!)

print cartes_prod([1,2], ["red", "white"])
