
def bubblesort(CustomList):
    for i in range(len(CustomList)-1):
        for j in range(len(CustomList)-i-1):
            if CustomList[j]>CustomList[j+1]:
                CustomList[j],CustomList[j+1]=CustomList[j+1],CustomList[j]
    print(CustomList)
items=[2,1,3,4,5,9,7]
bubblesort(items)
# time complexity of o(n^2)
# space complexity of o(1)