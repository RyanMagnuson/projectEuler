tot = 0
first = 1
second = 1

while second <= 4000000:
	if second % 2 == 0:
		tot += second
	temp = second
	second = first + second
	first = temp

print tot

