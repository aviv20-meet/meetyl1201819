import random
# def first_last(ls):
# 	new_ls = []
# 	new_ls.append(ls[0])
# 	new_ls.append(ls[-1])
# 	return new_ls
# print(first_last([5, 10, 15, 20, 25]))


# def under_five(ls):
# 	new_ls = []
# 	num = int(input("Enter a number: "))
# 	for i in ls:
# 		if i < num:
# 			new_ls.append(i)
# 	return new_ls
# print(under_five( [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))


def in_common(a,b):
	ls = []
	for i in a:
		for j in b:
			if (i == j ):
				ls.append(i)
	return ls
a = random.sample(range(1,50), 10)
b  = random.sample(range(1,50), 10)
print(b)
print(a)
print(in_common(a,b))


def is_prime(a):
	print(a)
	if (a%2) == 0:
		return False
	for i in range(2,a):
		if a//i == type(int):
			return True
	return 'ass'
print(is_prime(13))