# coding: utf-8
import sys, os, codecs
from viterbi_ngram import *


def load_ngram(f):
  fopen = codecs.open(f, "r", "utf-8")
  dic = {}
  for line in fopen:
    word, prob = line[:-1].split("\t")
    dic[word] = float(prob)
  
  return dic

if __name__ == "__main__":
  f = "ngrams.txt"
  path = os.path.dirname(os.path.abspath(__file__))
  ngram_dic = load_ngram(path + "/" + f)
  sentence = u"今日はいい天気だな"
  graph = construct_graph(sentence, ngram_dic)
  sep = viterbi(graph, sentence, ngram_dic, 2)
  sep.pop(0) #eos, popped
  for e in sep:
    print e
