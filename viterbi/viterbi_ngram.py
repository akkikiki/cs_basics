# coding: utf-8
#全てのステップが終わるまで、遷移先は確定しない。

class Node:
  start_pos = 0
  word = ""
  score = 0
  prev = None
  def __init__(self, start_pos, word):
    self.start_pos = start_pos
    self.word = word

def construct_graph(sentence, ngramdic):
  graph =[[] for i in range(len(sentence) + 2)]
  #print graph
  BOS = Node(-1, "<bos>")
  EOS = Node(len(sentence) + 1 , "<eos>")
  graph[0] = [BOS]
  graph[len(sentence) + 1].append(EOS)
  
  for i in range(0, len(sentence)-1):
    for j in range(i+1, len(sentence) + 1):
      # j represents the ending character
      substr = sentence[i:j]
      #print substr
      # multiple ways to read Hiragana
      node = Node(i, substr)
      if i == 0: node.prev = graph[0][0]
      graph[j].append(node)
  #print graph
  return graph



def get_nodes_ending_with_i(graph, i):
  return graph[i]

def get_ngram_prob(n, d, ngramdic):
  
  if n in ngramdic and d in ngramdic:
    prob = 1.0 * ngramdic[n] / ngramdic[d]
    return prob
  else: return 0.00001

def get_prev_nodes(graph, node, i):
  index = i-len(node.word)
  if node.word == "<eos>": index = i-1
  return get_nodes_ending_with_i(graph, index)

def viterbi_forward(graph, sentence, i, ngram, n): # ターゲットノードのベストな遷移先を確率を用いて算出する
  nodes = get_nodes_ending_with_i(graph, i)
  cost = 0.0000000000000000000001
  shortest_prev = None
  for node in nodes:
    
    temp_node = node
    length = len(node.word)
    prev_nodes = get_prev_nodes(graph, node, i)
    shortest_prev = prev_nodes[0]
    for prev_node in prev_nodes:
      context = [node.word]
      temp = prev_node
      for j in range(1, n): # trace back the n-1 nodes
        context.insert(0, temp.word) # joins with the target node
        temp = temp.prev
    
      numer = " ".join(context)
      context.pop()
      denomi = " ".join(context)
      prob = get_ngram_prob(numer, denomi, ngram)
      #print numer +"\t"+ denomi+"\t" + str(prob)
      if cost < prob: #probより
        cost = prob
        shortest_prev = prev_node
    node.prev = shortest_prev
    node.cost = cost
  #print i, shortest_prev.word

def viterbi_backward(graph, sentence):
  current = graph[-1][0] # eos
  ret = []
  indice = len(sentence)
  while current.word != '<bos>':
    #print current.word
    ret.append(current.word)
    current = current.prev
    
  return ret
  
def viterbi(graph, sentence, ngram, n):
  for i in range(1, len(sentence)+2):
    viterbi_forward(graph, sentence, i, ngram, n)

  words = viterbi_backward(graph, sentence)
  return words
