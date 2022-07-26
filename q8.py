
def read_file_and_return_map(file_path):
 file = open('hw.txt','r')
#  data = file.read()
 dat = file.readlines()

for elem in data:
    sub, name = elem.split()
    map_[sub].add(name)
       else:
      map_[sub]= {name} 
    file.close
    return map 

map_ = read_file_and_return_map('hw.txt')
print(map_)
 
 


# data = file.readlines()
# def check():
#  map_={}
# while True:
#         if file.buffer[0] in map:

#             map_(stud[0]].add(stud[1])

#         else:

#             map_(stud[0]]={stud[1]}

# print(map_)
print(data)
