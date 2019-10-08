# loop

# for loop
# find the min
# place in the front

integerList = [9,4,18,3,8,66,9,11]

def insert(list,src,dest):
    # src: the index of which to be inserted
    # dest: the index of where to insert in
    a = list[src]
    for i in range(src-1,dest-1,-1):
        list[i+1] = list[i]
    list[dest] = a
    return list


def insertionSort(list):
    for i in range(0,len(list)):
        for j in range(0,i):
            if list[i]<list[j]:
                list = insert(list,i,j)
            
    return list
