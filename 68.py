from itertools import *

def seqDex(index, inner, outdex, outer) :
  return (outer[outdex],inner[index],inner[(index+1)%len(inner)])


def tryGon(inner, outer) :
  length = len(inner)
  for i in range(0,length) :
    seq = seqDex(i,inner, 0,outer)
    value = sum(seq)
    seqs = [seq]
    for j in range(1,length) :
      seq = seqDex((i+j)%length,inner, j,outer)
      if value != sum(seq) : break
      seqs.append(seq)
    if len(seqs) == length : 
      start = seqs.index(min(seqs))
      yield seqs[start:]+seqs[:start]


def collapseSeq(seq) :
  return int(''.join([''.join([str(j) for j in i]) for i in seq]))


def maxim(seq) :
  return max(seq) if seq else 0


maxim([maxim([k for k in [collapseSeq(seq) for seq in j] if k < 10**16]) for j in \
  [list(tryGon(i[:5], i[5:])) for i in permutations(range(1,11))] if j])
  
