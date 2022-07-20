n = input("enter the string")
n = n.lower()
map_ = {}
# for i in n:
#     if i in map_: 
#         map_[i]+=1
#     else:
#         map_[i] =1
# print(map_)
    


for i in n:
    if i in map_: 
        map_[i]+=1
    else:
       map_[i] =1
print(map_)
    

    
   

