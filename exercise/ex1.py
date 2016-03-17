import os


# read L
L = []
f_in = open('table1.txt', 'r')
for line in f_in:
    L.append(line.split(' ')[0])
f_in.close()


# (a) Accepts a letter in L (including space).
f_out, out = open('1a.txt', 'w'), ''
for s in L:
    if s != '<eps>':
        out += '0 1 {s} {s}\n'.format(s=s)
out += '1'
f_out.write(out)
f_out.close()

os.system('fstcompile --isymbols=table1.txt --osymbols=table1.txt 1a.txt 1a.fst')
os.system('fstdraw --acceptor --portrait --nodesep=0.01 --height=10 --isymbols=table1.txt --osymbols=table1.txt 1a.fst 1a.dot')
os.system('dot -Tps 1a.dot > 1a.ps')

# (b) Accepts a single space.
f_out, out = open('1b.txt', 'w'), ''
out += '0 1 <space> <space>\n'
out += '1'
f_out.write(out)
f_out.close()

os.system('fstcompile --isymbols=table1.txt --osymbols=table1.txt 1b.txt 1b.fst')
os.system('fstdraw --acceptor --portrait --isymbols=table1.txt --osymbols=table1.txt 1b.fst 1b.dot')
os.system('dot -Tps 1b.dot > 1b.ps')

# (c) Accepts a capitalized word (where a word is a string of letters in L excluding space and a capitalized word has its initial letter uppercase and remaining letters lowercase).
f_out, out = open('1c.txt', 'w'), ''
for s in L:
    if s != '<eps>' and s != '<space>':
        if s.islower():
            out += '1 1 {s} {s}\n'.format(s=s)
        else:
            out += '0 1 {s} {s}\n'.format(s=s)
out += '1'
f_out.write(out)
f_out.close()

os.system('fstcompile --isymbols=table1.txt --osymbols=table1.txt 1c.txt 1c.fst')
os.system('fstdraw --acceptor --portrait --nodesep=0.01 --height=15 --isymbols=table1.txt --osymbols=table1.txt 1c.fst 1c.dot')
os.system('dot -Tps 1c.dot > 1c.ps')

# (d) Accepts a word containing the letter a.
f_out, out = open('1d.txt', 'w'), ''
for s in L:
    if s != '<eps>' and s != '<space>':
        if s != 'a':
        out += '1 1 {s} {s}\n'.format(s=s)
out += '0 1 a a\n'
out += '1'
f_out.write(out)
f_out.close()

os.system('fstcompile --isymbols=table1.txt --osymbols=table1.txt 1d.txt 1d.fst')
os.system('fstdraw --acceptor --portrait --nodesep=0.01 --height=20 --isymbols=table1.txt --osymbols=table1.txt 1d.fst 1d.dot')
os.system('dot -Tps 1d.dot > 1d.ps')
