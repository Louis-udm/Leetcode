# Prisoners are standing on a Cartesian coordinate system present inside a jail. 
# Each prisoner stands at a unique point with both the coordinates (x,y ) being integers. 
# Each prisoner should be at a position that forms a rectangle or square with 3 other prisonners.
# More formally, every prisoner at a coordinates pair [x,y] should have: 
# at least one prisoner standing at intger coordinates [x,ay] where ay!=y.
# at least one prisoner standing at integer coordinates [bx,y] where bx!=x.
# Unforunately, one prisoner has escaped. find the coordinates of that prisoner.
# [(1, 1), (1, 2), (2, 1), (4, 4), (4,6),(9,4),(9,6)]
# Output: (2,2)

from collections import defaultdict, Counter

def find_missing_prisoner(coordinates: list[tuple[int, int]]) -> tuple[int, int]:
    # Write your code here
    x_dict=defaultdict(int)
    y_dict=defaultdict(int)
    for x,y in coordinates:
        x_dict[x]=x_dict.get(x,0)+1
        y_dict[y]=y_dict.get(y,0)+1
    for x,c in x_dict.items():
        if c%2==1:
            x_missing=x
            break
    for y,c in y_dict.items():
        if c%2==1:
            y_missing=y
            break
    return (x_missing,y_missing)


# cerence unit test cases
print(find_missing_prisoner([(1, 1), (1, 2), (2, 1), (4, 4), (4,6),(9,4),(9,6)]))