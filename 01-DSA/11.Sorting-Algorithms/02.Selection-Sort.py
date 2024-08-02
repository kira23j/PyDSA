def SelectionSort(customList):
    for i in range(len(customList)):
        min_index=i
        for j in range(i+1,len(customList)):
          if customList[min_index]>customList[j]:
              min_index=j
        customList[i],customList[min_index]=customList[min_index],customList[i]
    print(customList)

items=[2,4,5,6,7,8,1,3]
SelectionSort(items)
# time complexity o(n^2)
# space complexty o(1)
