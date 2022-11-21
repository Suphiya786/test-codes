def convertToBase3(n):
	if (n== 0):
		return
	x = n % 3
	n//= 3
	if (x < 0):
		n += 1
	convertToBase3(n)
	if (x < 0):
		print(x + (3 * -1), end = "")
	else:
		print(x, end = "")

def convert(num):
	print(end = "")
	if (num != 0):
		convertToBase3(num)
	else:
		print("0", end = "")
		
if __name__ == '__main__':
	num = int(input())
	convert(num)

