# file = open('demo.txt', 'r')                                                      
# data = file.read()
# data = file.readlines()
# file.close()
# print(data)




file = open('demo.txt', 'w')
file.write('This is a demo file')
file.writelines(['This is demo files','This is a demo file2'])
file.close()
