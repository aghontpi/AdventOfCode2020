#! /usr/bin/python3

def solution(arr):
	totalCount = 0
	for x in arr:
		splits = x.split(' ')
		[lBound, uBound] = splits[0].split('-')
		print(splits,lBound,uBound)
		character = splits[1][0]
		pwd = splits[2]
		count = 0
		for c in list(pwd):
			if c == character:
				count += 1
		if count >= int(lBound) and count <= int(uBound):
			totalCount += 1	
		print(x, count, totalCount)
	return totalCount		




def solution2(arr):
	totalCount = 0
	for x in arr:
		splits = x.split(' ')
		[lBound, uBound] = splits[0].split('-')
		print(splits,lBound,uBound)
		character = splits[1][0]
		pwd = splits[2]
		lchar = pwd[int(lBound)-1]
		uchar = pwd[int(uBound)-1]
		if lchar == character and uchar == character:
			continue
		if lchar == character or uchar == character:
			totalCount += 1
		print(x, totalCount)
	return totalCount		

inputs = [x.strip('\n') for x in open('input.txt','r').readlines()]
#print(solution(inputs))
print(solution2(inputs))
