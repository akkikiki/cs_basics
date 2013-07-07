# coding: utf-8

from viterbi_ngram import *

def load_ngram(f):
  fopen = open(f, "r")
  dic = {}
  for line in fopen:
    word, prob = line[:-1].split("\t")
    dic[word] = float(prob)
  
  return dic

if __name__ == "__main__":
  f = "ngrams.txt"
  ngram_dic = load_ngram(f)
  sentence = u"今日はいい天気だな"
  sep = viterbi(sentence, ngram_dic, 2)
  for e in sep:
    print e
