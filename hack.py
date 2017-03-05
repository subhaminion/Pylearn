# #!/bin/python

# # def someArray(arr):
# # 	sum = 0
# # 	for i in arr:
# # 		sum  = sum + i

# # 	return sum

# num_array =list()
# num = raw_input()
# for i in xrange(int(num)):
# 	n = raw_input()
# 	num_array.append(int(n)) #num_array.append(n) for appending strings

# print sum(num_array)
from __future__ import print_function


# try:
#     input = raw_input
# except:
#     pass


# def main():
input = raw_input
# print (input().strip()) 
array_size = int(input().strip())
array = [int(arr_temp) for arr_temp in input().strip().split(' ')] #list comprehension it is
print(sum(array))


# if __name__ == '__main__':
#     main()
