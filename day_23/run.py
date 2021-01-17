#! /usr/bin/python3

from linked_list import LinkedList


def solver(ll,max_value,iterations, print_limit, print_destination):
  for _ in range(iterations):
      if (_ % print_limit) == 0:
        print(f'\n-- move {_+1} --')
      value = ll.head.value
      # decrement
      value = value - 1
      if value == 0:
          value = max_value
      # extraction
      if print_destination:
        ll._print()
      ll.extract_elements()
      if print_destination:
        ll._print()
      # manipulation
      while value in ll.extracted_elements:
          value = value - 1
          if value == 0:
              value = max_value
      if print_destination:
        print(f'\ndestination: {value}')
      ll.insertExtractedElements(value)
      if print_destination:
        ll._print()
      if iterations - 1 != _:
          ll.moveHead()
          if print_destination:
            ll._print()

def partTwo():
  inputs = open('test.txt').read().strip()
  inputs = [int(x) for x in inputs]
  ll = None

  ll = LinkedList()
  for x in inputs:
      ll.push(int(x))
  for i in range(len(inputs)+1, 1000001):
      ll.push(i)
  # ll._print()

  max_value = 1000000
  iterations = 10000000
  solver(ll, max_value, iterations, 100000, False)
  # part two
  node = ll.position_map[1]
  print(f'solution : node one: {node.next.value}, node two: {node.next.next.value}. pdt: {node.next.value * node.next.next.value}')


def partOne():
  inputs = open('input.txt').read().strip()
  inputs = [int(x) for x in inputs]
  max_value = max(inputs)

  ll = LinkedList()
  for x in inputs:
      ll.push(int(x))
  # ll._print()
  iterations = 100
  solver(ll,max_value, iterations, 1, True)

  # extracting solution
  node = ll.head
  _solution =  []
  while node.value != 1:
      _solution.append(str(node.value))
      node = node.next
  assert(node.value == 1)
  node = node.next
  while node:
      _solution.append(str(node.value))
      node = node.next
  print(f'answer: {"".join(_solution)}')

partOne()
partTwo()
