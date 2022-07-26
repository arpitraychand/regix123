try:
    print(5/0)
except ZeroDivisionError:
    print('you cant divide bt zero')
except:
    print('you cant divide by string')
