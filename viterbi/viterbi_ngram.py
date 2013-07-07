# coding: utf-8
#全てのステップが終わるまで、遷移先は確定しない。

class Node:
  start_pos
  word =
  score = 0
  prev = None
  def __init__(self, start_pos, word):
    self.start_pos = start_pos
    self.word = word

def construct_graph(sentence):
  graph = []
  graph.append("<bos>")
  graph.append("<eos>")
  
  for i in range(0, len(sentence)):
    for j in range(i+1, min(len(sentence), 16): #japanese words typically has less than 10 chars
      # j represents the ending character
      substr = sentence[i:j]
      graph_j = []
      if substr in ht:
        for word in ht[substr]: # multiple ways to read Hiragana
          node = Node(i, word)
          graph_j.append(node)
      if len(graph) <= j: # not searched yet
        graph.append(graph_j)
      else: graph[j] += graph_j # merging the lists
  
  return graph



def get_nodes_ending_with_i(sentence, i):
  words = []
  for j in range(i):
    words.append(sentence[j:i])
  return words

def get_ngram_prob(n, d, ngramdic):
  if n in ngramdic and d in ngramdic:
    prob = 1.0 * ngramdic[n] / ngramdic[d]
    return prob
  else: return 0.00001

def viterbi_forward(sentence, i, ngram, n, best_node, best_prob): # ターゲットノードのベストな遷移先を確率を用いて算出する
  nodes = get_nodes_ending_with_i(sentence, i)
  best_prob.append(10**9) # appending an ith element
  best_node.append(None)

  for node in nodes:
    context = [node]
    temp_node = node
    length = len(node)
    current = node
    for j in range(1, n-1): # trace back the n-1 nodes
      prev_word = get_prev_word(current, best_node, i)
      context.append(prev_word) # joins with the target node
      current =prev_word
    
    numer = " ".join(context)
    denomi = " ".join(context.pop())
    prob = get_ngram_prob(numer, denomi, ngram)
    if prob < best_prob[i]:
      best_prob[i] = prob
      best_node[i] = node # TODO 多分ここで全部の確率が無理やり挿入されているから、EOS

def viterbi_backward(best_node, sentence):
  current = best_node[-1] # eos
  print current
  ret = []
  indice = len(sentence)
  while current != '<bos>' and indice >0:
    ret.append(current)
    indice -= len(current)
    current = best_node[indice]
    
  return ret
  
def viterbi(sentence, ngram, n):
  best_node = ['<bos>']
  best_prob = [0]
  for i in range(1, len(sentence)):
    viterbi_forward(sentence, i, ngram, n, best_node, best_prob)

  words = viterbi_backward(best_node, sentence)
  return words
