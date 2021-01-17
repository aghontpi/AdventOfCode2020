def solution(arr):
	for i in range(0, len(arr)):
		for j in range(i, len(arr)):
			for k in range(i, len(arr)):
				if int(arr[i]) + int(arr[j]) + int(arr[k]) == 2020:
					print(int(arr[i]) * int(arr[j]) * int(arr[k]))
	




inputs = open('input1.txt','r').readlines()
processedInput = list(map(lambda x: x.strip('\n'),inputs))

solution(processedInput)
