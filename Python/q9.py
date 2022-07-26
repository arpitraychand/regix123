# from asyncore import read


# def max_of_a_world(file_path):
#     file = open(file_path, 'r')
#     data = read()


def frequency(file_path):
    file = open(file_path,'r')
    data = file.read()
    data = data.split()
    map_ = {} 
    for elem in data: 
        if elem in map_:
            map_[elem] +=1
        else:
            map_[elem] = 1
    return map_

map_= frequency('hitler.txt')
print(map_)

