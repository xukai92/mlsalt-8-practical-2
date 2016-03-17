import os


os.system('HIFST=/home/wjb31/src/hifst.mlsalt-cpu1.5Nov15/ucam-smt/')
os.system('export PATH=$PATH:$HIFST/bin/')
os.system('export PATH=$PATH:$HIFST/externals/openfst-1.5.0/INSTALL_DIR/bin/')

# 1a.fst - a letter in L (including space)
# 1b.fst - a single space
# 1c.fst - a capitalized word
# 1d.fst - a word containing the letter a

# 2. Using the automata in Question 1 as the building blocks, use appropriate FST operations on them to create an automaton that:
# (a) Accepts zero or more capitalized words followed by spaces.
os.system('fstconcat 1c.fst 1b.fst 2a1.fst')
os.system('fstclosure 2a1.fst 2a.fst')

# (b) Accepts a word beginning or ending in a capitalized letter.

# (c) Accepts a word that is capitalized and contains the letter a.

# (d) Accepts a word that is capitalized or does not contain an a.

# (e) Accepts a word that is capitalized or does not contain an a without using fstunion.