import os


# 1a.fst - a letter in L (including space)
# 1b.fst - a single space
# 1c.fst - a capitalized word
# 1d.fst - a word containing the letter a

# 2. Using the automata in Question 1 as the building blocks, use appropriate FST operations on them to create an automaton that:
out = ''

# (a) Accepts zero or more capitalized words followed by spaces.
os.system('fstconcat 1c.fst 1b.fst 2a1.fst')
os.system('fstclosure 2a1.fst 2a2.fst')
os.system('fstrmepsilon 2a2.fst | fstdeterminize | fstminimize - 2a.fst')

out += '2.(a) before\n'
f = os.popen('fstinfo 2a2.fst | head -n 6 | tail -n 2')
out += f.read()
out += '2.(a) after\n'
f = os.popen('fstinfo 2a.fst | head -n 6 | tail -n 2')
out += f.read()

os.system('fstdraw --acceptor --portrait --nodesep=0.01 --ranksep=1.0 --height=15 --isymbols=table1.txt --osymbols=table1.txt 2a.fst 2a.dot')
os.system('dot -Tps 2a.dot > 2a.ps')

# (b) Accepts a word beginning or ending in a capitalized letter.
os.system('fstreverse 1c.fst 2b1.fst')
os.system('fstunion 1c.fst 2b1.fst 2b2.fst')
os.system('fstrmepsilon 2b2.fst | fstdeterminize | fstminimize - 2b.fst')

out += '2.(b) before\n'
f = os.popen('fstinfo 2b2.fst | head -n 6 | tail -n 2')
out += f.read()
out += '2.(b) after\n'
f = os.popen('fstinfo 2b.fst | head -n 6 | tail -n 2')
out += f.read()

os.system('fstdraw --acceptor --portrait --nodesep=0.01 --height=13 --ranksep=1.0 --isymbols=table1.txt --osymbols=table1.txt 2b.fst 2b.dot')
os.system('dot -Tps 2b.dot > 2b.ps')

# (c) Accepts a word that is capitalized and contains the letter a.
os.system('fstintersect 1c.fst 1d.fst 2c1.fst')
os.system('fstrmepsilon 2c1.fst | fstdeterminize | fstminimize - 2c.fst')

out += '2.(c) before\n'
f = os.popen('fstinfo 2c1.fst | head -n 6 | tail -n 2')
out += f.read()
out += '2.(c) after\n'
f = os.popen('fstinfo 2c.fst | head -n 6 | tail -n 2')
out += f.read()

os.system('fstdraw --acceptor --portrait --nodesep=0.01 --ranksep=1.0 --height=17 --isymbols=table1.txt --osymbols=table1.txt 2c.fst 2c.dot')
os.system('dot -Tps 2c.dot > 2c.ps')

# (d) Accepts a word that is capitalized or does not contain an a.
os.system('fstdifference 1a.fst 1b.fst 2d1.fst')
os.system('fstclosure 2d1.fst 2d2.fst')
os.system('fstconcat 2d1.fst 2d2.fst 2d3.fst')      # all word
os.system('fstdifference 2d3.fst 1d.fst 2d4.fst')
os.system('fstunion 1c.fst 2d4.fst 2d5.fst')
os.system('fstrmepsilon 2d5.fst | fstdeterminize | fstminimize - 2d.fst')

out += '2.(d) before\n'
f = os.popen('fstinfo 2d5.fst | head -n 6 | tail -n 2')
out += f.read()
out += '2.(d) after\n'
f = os.popen('fstinfo 2d.fst | head -n 6 | tail -n 2')
out += f.read()

os.system('fstdraw --acceptor --portrait --nodesep=0.01 --ranksep=1.0 --height=15 --isymbols=table1.txt --osymbols=table1.txt 2d.fst 2d.dot')
os.system('dot -Tps 2d.dot > 2d.ps')

# (e) Accepts a word that is capitalized or does not contain an a without using fstunion.
os.system('fstarcsort --sort_type=ilabel 1c.fst 2e1.fst')
os.system('fstdifference 2d3.fst 2e1.fst 2e2.fst')
os.system('fstintersect 2e2.fst 1d.fst 2e3.fst')
os.system('fstrmepsilon 2e3.fst | fstdeterminize | fstminimize - 2e.fst')

out += '2.(e) before\n'
f = os.popen('fstinfo 2e3.fst | head -n 6 | tail -n 2')
out += f.read()
out += '2.(e) after\n'
f = os.popen('fstinfo 2e.fst | head -n 6 | tail -n 2')
out += f.read()

os.system('fstdraw --acceptor --portrait --nodesep=0.01 --ranksep=1.0 --height=15 --isymbols=table1.txt --osymbols=table1.txt 2e.fst 2e.dot')
os.system('dot -Tps 2e.dot > 2e.ps')

f_out = open('2.txt', 'w')
f_out.write(out)
f_out.close()
