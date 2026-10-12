def main():
	tests = int(input())
	for test in range(tests):
		a, b, c = sorted(list(map(int, input().rstrip().split())))
		print(min(c - a, b))

if __name__ == "__main__":
	main()
