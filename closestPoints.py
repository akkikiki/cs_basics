# -*- coding: utf-8 -*- 
# Assuming that input points are described as tuples
# what happens if the found pairs are not unique?
import math

def distance(a, b):
  # this returs d^2
  # quality raised by expanding to multiple dimension
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def compute_closest_pairs(input_list):
  if len(input_list) < 2: return 10 ** 9
  delta = 10 ** 9
  for i in xrange(len(input_list)):
    for j in xrange(i + 1, len(input_list)):
      dist = distance(input_list[i], input_list[j])
      if dist < delta: delta = dist
  return delta

def closestPoints(X, Y):
  # (x, y) is the given pair
  # Assuming the given lists are already sorted
  # dividing by a vertical line (x-axis)
  n = len(X)
  if n <= 3: return compute_closest_pairs(X) # return a pair of points and delta
  x_median = n/2
  
  # creating X_l and X_r
  X_l = []
  X_r = []
  Y_l = []
  Y_r = []
  for point in X:
    if point[0] <= X[x_median][0]: X_l.append(point)
    else: X_r.append(point)
  
  if X == X_l or X == X_r: # duplicate points check, otherwise causes error for case duplicates >= 4
    X_l = X[:x_median]
    X_r = X[x_median:]
  
  for point in Y:
    if point in X_l:
      Y_l.append(point)
    else:
      Y_r.append(point)

  delta = 10 ** 9
  
  delta_l = closestPoints(X_l, Y_l)
  delta_r = closestPoints(X_r, Y_r)
  delta = min(delta_l, delta_r)
  ## computing the cross border pairs
  # find all points which are within |delta| from x_median
  Y_d = []
  for point in Y:
    if abs(X[x_median][0] - point[0]) ** 2 < delta:
      Y_d.append(point)
  # δを直接更新していく方が良い
  #delta_d = 10 ** 9
  Y_d_len = len(Y_d)
  for i in xrange(Y_d_len):
    for j in xrange(i+1, Y_d_len):
      temp_dis = distance(Y_d[i], Y_d[j])
      if temp_dis < delta:
        delta = temp_dis 
   
  #if delta_d < delta: delta = delta_d
  return delta

def main(P):
  X = sorted(P, key = lambda x:x[0]) # sorted monotonically by x
  Y = sorted(P, key = lambda x:x[1]) # sorted monotonically by y

  return math.sqrt(closestPoints(X, Y)) # sqrtには時間がかかるため一回のみに抑えている。

def test(P, answer):
  if main(P) == answer:
    print True
  else: print False

if __name__ == "__main__":
  # list of points as input
  # test cases
  P1 = [(0, 0), (1, 1), (2,2), (3,3), (4,4), (5, 5), (6, 6), (7,7), (8, 8), (9, 9)] # multiple minimum distance pairs
  P2 = [(1,1), (1,1)]
  P3 = [(1,1), (1,1), (1,1), (1,1)]
  P4 = [(1,0), (1,3), (1,4), (1,8)]
  P5 = [(-2,-3), (-1, -1), (-1,1), (2,2)] # for pairs with negative and positive points
  P6 = [(-2,4), (-1, -1), (0,-2), (2, -20)] # unsorted input for y, absolute function is working or not
  P7 = [(3,4), (-1, -1), (1,1), (-2, -20)] # unsorted input for x
  
  
  test(P1, math.sqrt(2))
  test(P2, 0)
  test(P3, 0)
  test(P4, 1)
  test(P5, 2)
  test(P6, math.sqrt(2))
  test(P7, 2 * math.sqrt(2))
