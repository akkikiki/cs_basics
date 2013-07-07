# coding: utf-8

import sys

def rev(input_array):
  # reverse till the ith card
  n = len(input_array)
  new_array = [input_array[n-1 - i] for i in xrange(n)]
  return new_array

def cut_part(deck, begin , end):
  temp_array = deck[begin: end]
  temp_array = rev(temp_array)
  for i in xrange(end - begin):
    deck[begin + i] = temp_array[i]
  return deck

def cut(deck, p, c):
  deck = cut_part(deck, 0, p-1)
  deck = cut_part(deck, p-1, p-1+c)
  deck = cut_part(deck, 0, p-1+c)
  return deck

if __name__ == "__main__":
  argv = sys.argv
  f = open(argv[1], "r")
  case = 1
  while(1):
    first = f.readline()
    n, r = map(int, first[:-1].split())
    deck = [n - i for i in xrange(n)] # 昇順に番号を付けていく、始まりは1
    if n == 0 and r == 0: break
    for i in xrange(r):
      p, c = map(int, f.readline().split())
      print p,c
      cut(deck, p, c)
    print "case " + str(case) + " is  " + str(deck[0])
    case += 1
