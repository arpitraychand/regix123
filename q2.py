
n = input('how many test cases')
n = int(n)
# for i in range(n):
#     op = input('enter the operation')
#     op_list = op.split()
#     print(op_list)
#     if op_list[0] == 'add':
#         num = map(int,op_list[1:])
#         for j in num:
#         print(total = total + j)
            
#     elif op_list[0] =='mul':
#         num = map(int, op_list)
#         for j in num:
#             num = num * j

for i in range(n):
    op = input('enter the operation')
    op_list = op.split()
    print(op_list)
    if op_list[0] == 'add':
        total = 0
        for num in op_list[1:]:
            total = total + int(num)
            print(total)
    elif op_list[0] == 'mul':
        sum = 0
        for num in op_list[1:]:
            sum = sum * int(num)
        print(sum)



