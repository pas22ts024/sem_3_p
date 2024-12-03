import random
import time


def insertonsortwithbinnsearh(arr):
	k = 0
	for i in range(1, len(arr)):
		cur = arr[i]
		lo = 0
		hi = i
		if lo == hi:
			lo += 1
		else:
			while lo < hi:
				mid = (lo + hi) // 2
				if cur < arr[mid]:
					hi = mid
				else:
					lo = mid + 1
		j = i
		while j > lo and j > 0:
			arr[j] = arr[j - 1]
			j -= 1
			k += 1
		k += 1
		arr[lo] = cur
	return k


def zamer(n):
	a = []
	for i in range(n):
		a.append(i + 1)
	t1 = time.time()
	k1 = insertonsortwithbinnsearh(a)
	t1 = time.time() - t1
	a = []
	for i in range(n):
		a.append(random.randint(1, n * 10))
	t2 = time.time()
	k2 = insertonsortwithbinnsearh(a)
	t2 = time.time() - t2
	a = []
	for i in range(n):
		a.append(i + 1)
	a = a[::-1]
	t3 = time.time()
	k3 = insertonsortwithbinnsearh(a)
	t3 = time.time() - t3
	return int(t1 * 1000), k1, int(t2 * 1000), k2, int(t3 * 1000), k3


a = []
try:
	n = int(input())
	if n > 0:
		for i in range(n):
			a.append(random.randint(1, 100))
		print(*a)
		insertonsortwithbinnsearh(a)
		print(*a)
	else:
		print("n отрицательное")
except:
	print("Введено неверное значение")
try:
	n1 = int(input())
	n2 = int(input())
	n3 = int(input())
	t1, k1, t4, k4, t7, k7 = zamer(n1)
	t2, k2, t5, k5, t8, k8 = zamer(n2)
	t3, k3, t6, k6, t9, k9 = zamer(n3)
	print(" " * 13, "{n1:^15}    {n2:^15}    {n3:^15}".format(n1 = n1, n2 = n2, n3 = n3))
	print(" " * 13, "время перестановки время перестановки время перестановки")
	print("Упорядоченный", "{t1:^5}{k1:^14}{t2:^5}{k2:^14}{t3:^5}{k3:^14}".format(t1 = t1, k1 = k1, t2 = t2, k2 = k2, t3 = t3, k3 = k3))
	print("Список")
	print("Случайный    ", "{t4:^5}{k4:^14}{t5:^5}{k5:^14}{t6:^5}{k6:^14}".format(t4 = t4, k4 = k4, t5 = t5, k5 = k5, t6 = t6, k6 = k6))
	print("Список")
	print("Упорядоченный", "{t7:^5}{k7:^14}{t8:^5}{k8:^14}{t9:^5}{k9:^14}".format(t7 = t7, k7 = k7, t8 = t8, k8 = k8, t9 = t9, k9 = k9))
	print("в обратном")
	print("порядке")
except:
	print("Одна или несколько размерностей введены неверно")
