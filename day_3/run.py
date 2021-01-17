#! /usr/bin/python3

def partOne(arr):
  yoffset = 3
  treeCount = 0
  sizeOfItem = len(arr[0]) - 1
  for xoffset in range(1, len(arr)):
    if arr[xoffset][yoffset] == '#':
      treeCount += 1
    yoffset = (yoffset + 3) % sizeOfItem
    
  return treeCount 

def partTwo(arr,yoffsetInit,xoffsetInit):
  sizeOfItem = len(arr[0]) - 1
  treeCount = 0
  yoffset = yoffsetInit
  for xoffset in range(xoffsetInit, len(arr), xoffsetInit):
    if arr[xoffset][yoffset] == '#':
        treeCount += 1
    yoffset = (yoffset + yoffsetInit) % sizeOfItem
  
  return treeCount



print('day3')
inputs = [ x for x in open('inputs.txt').readlines()]
print('partOne', partOne(inputs))
#print('test', partTwo(inputs,3,1 ))
print('partTwo', partTwo(inputs, 1,1)*partTwo(inputs, 3,1)*partTwo(inputs, 5,1)*partTwo(inputs, 7,1)*partTwo(inputs, 1,2))
