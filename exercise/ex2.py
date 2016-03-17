import os


# 1a.fst - a letter in L (including space)
# 1b.fst - a single space
# 1c.fst - a capitalized word
# 1d.fst - a word containing the letter a

# 2. Using the automata in Question 1 as the building blocks, use appropriate FST operations on them to create an automaton that:
# (a) Accepts zero or more capitalized words followed by spaces.
os.system('fstconcat 1c.fst 1b.fst 2a1.fst')
os.system('fstclosure 2a1.fst 2a.fst')

os.system('fstdraw --acceptor --portrait --nodesep=0.01 --height=15 --isymbols=table1.txt --osymbols=table1.txt 2a.fst 2a.dot')
os.system('dot -Tps 2a.dot > 2a.ps')

# (b) Accepts a word beginning or ending in a capitalized letter.
os.system('fstreverse 1c.fst 2b1.fst')
os.system('fstunion 1c.fst 2b1.fst 2b2.fst')
os.system('fstrmepsilon 2b2.fst | fstdeterminize | fstminimize - 2b.fst')

# (c) Accepts a word that is capitalized and contains the letter a.

# (d) Accepts a word that is capitalized or does not contain an a.

# (e) Accepts a word that is capitalized or does not contain an a without using fstunion.
