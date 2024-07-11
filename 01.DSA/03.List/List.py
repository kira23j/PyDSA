# list in python
Places_to_visit=["lalibela","axum","fasiledes"]

# accessing list
for i in range(len(Places_to_visit)):
    Places_to_visit[i]=Places_to_visit[i]+"," 
    print(Places_to_visit[i])
  
# list operations  
empty=[]
for i in empty:
    print("empty list")
    
empty.insert(0,1)
print(empty)
empty.append(2)
list_two=[3,4,5]
empty.extend(list_two)
print(empty)

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print("search index for 3 is:-",searchinList(empty,3))
print("search index for 7 is:-",searchinList(empty,7))

# list n string
all_english="the quick brown fox jumps over the lazy dog"
delimiter=' '
a=all_english.split(delimiter)
print(a)
# join back together
b=delimiter.join(a)
print(b)


