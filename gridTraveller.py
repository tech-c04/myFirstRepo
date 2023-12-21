def gridTraveller(l, w):
    dimension = f"({l}, {w})"
    dimensions_list = {}
    if l == 1 and w == 1:
        return 1
    if l ==0 or w == 0:
        return 0
    if dimension in dimensions_list:
        return dimensions_list.get(dimension)
    
    
    # dimensions_list.append({dimension : gridTraveller(l,w)})
    # if(dimension in dimensions_list):
    #     return dimensions_list.get(dimension)
    dimensions_list[dimension] = gridTraveller(l-1,w) + gridTraveller(l,w-1)
    return dimensions_list[dimension]

print(gridTraveller(2,3))
print(gridTraveller(4,4))
print(gridTraveller(5,5))
print(gridTraveller(18,18))