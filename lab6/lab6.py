import matplotlib.pyplot as plt


n = int(input())
x_p = []
y_p = []
for i in range(n):
	x, y = map(int, input().split())
	x_p.append(x)
	y_p.append(y)


def check_points(point1, point2, point3):
	if (point2[0] - point1[0]) * (point3[1] - point1[1]) - (point3[0] - point1[0]) * (point2[1] - point1[1]):
		return False



for i in range(n):
	for j in range(i + 1, n):
		for k in range(j + 1, n):
			for z in range(k + 1, n):
				print('a')
				point1 = (x_p[i], y_p[i])
				point2 = (x_p[j], y_p[j])
				point3 = (x_p[k], y_p[k])
				point4 = (x_p[z], y_p[z])
				if not(check_points(point1, point2, point3) or check_points(point1, point2, point4) or check_points(point4, point2, point3)):
					d =  sorted([point1, point2, point3, point4])
					point1, point2, point3, point4 = d[0], d[1], d[3], d[2]
					x = [point1[0], point2[0]]
					y = [point1[1], point2[1]]
					plt.plot(x, y)
					x = [point2[0], point3[0]]
					y = [point2[1], point3[1]]
					plt.plot(x, y)
					x = [point3[0], point4[0]]
					y = [point3[1], point4[1]]
					plt.plot(x, y)
					x = [point4[0], point1[0]]
					y = [point4[1], point1[1]]
					plt.plot(x, y)
plt.show()
