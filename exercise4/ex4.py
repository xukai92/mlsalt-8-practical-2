import os


alphabet = []
fin = open('table4.txt', 'r')
for line in fin:
    sym = line.split(' ')[0]
    if sym.isalpha():
        alphabet.append(sym)
fin.close()

# 4a
fout, out = open('4a.txt', 'w'), ''
l = len(alphabet)
for i in range(l):
    out += '0 0 {i} {o}\n'.format(i=alphabet[i], o=alphabet[(i + 13) % 26])
out += '0 0 <space> <space>\n'
out += '0 0 . .\n'
out += '0 0 , ,\n'
out += '0'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table4.txt --osymbols=table4.txt 4a.txt 4a.fst')
os.system('fstdraw --portrait --nodesep=0.01 --height=15 --isymbols=table4.txt --osymbols=table4.txt 4a.fst 4a.dot')
os.system('dot -Tps 4a.dot > 4a.ps')

# 4b
message = 'my secret message'
fout, out = open('4b.txt', 'w'), ''
for i in range(len(message)):
    if message[i] == ' ':
        sym = '<space>'
    else:
        sym = message[i]
    out += '{s} {e} {l} {l}\n'.format(s=i, e=i+1, l=sym)
out += '17'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table4.txt --osymbols=table4.txt 4b.txt 4b.fst')
os.system('fstdraw --acceptor --vertical --portrait --fontsize=17 --nodesep=0.01 --height=10 --isymbols=table4.txt --osymbols=table4.txt 4b.fst 4b.dot')
os.system('dot -Tps 4b.dot > 4b.ps')

os.system('fstcompose 4b.fst 4a.fst 4b2.fst')
os.system('fstproject --project_output 4b2.fst 4b3.fst')
f = os.popen('printstrings.O2 --label-map=table4.txt --input=4b3.fst -n 10 -w')
fout = open('4bencode.txt', 'w')
fout.write(f.read())
fout.close()
os.system('fstdraw --acceptor --vertical --portrait --fontsize=29 --nodesep=0.01 --height=10 --isymbols=table4.txt --osymbols=table4.txt 4b3.fst 4b3.dot')
os.system('dot -Tps 4b3.dot > 4b3.ps')

os.system('fstcompose 4a.fst 4b.fst 4b4.fst')
os.system('fstproject --project_output 4b4.fst 4b5.fst')
f = os.popen('printstrings.O2 --label-map=table4.txt --input=4b5.fst -n 10 -w')
fout = open('4bdecode.txt', 'w')
fout.write(f.read())
fout.close()
os.system('fstdraw --acceptor --vertical --portrait --fontsize=29 --nodesep=0.01 --height=10 --isymbols=table4.txt --osymbols=table4.txt 4b5.fst 4b5.dot')
os.system('dot -Tps 4b5.dot > 4b5.ps')

# 4c
fout, out = open('4c.txt', 'w'), ''
l = len(alphabet)
for i in range(l):
    out += '0 0 {i} {o}\n'.format(i=alphabet[i], o=alphabet[(i + 16) % 26])
out += '0 0 <space> <space>\n'
out += '0 0 . .\n'
out += '0 0 , ,\n'
out += '0'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table4.txt --osymbols=table4.txt 4c.txt 4c.fst')
os.system('fstdraw --portrait --nodesep=0.01 --height=15 --isymbols=table4.txt --osymbols=table4.txt 4c.fst 4c.dot')
os.system('dot -Tps 4c.dot > 4c.ps')

os.system('fstunion 4a.fst 4c.fst 4c2.fst')
os.system('fstclosure 4c2.fst 4c3.fst')
os.system('fstcompose 4.encoded1.fst 4c3.fst 4c4.fst')
os.system('fstproject --project_output 4c4.fst 4c5.fst')
os.system('fstrmepsilon 4c5.fst | fstdeterminize | fstminimize - 4c6.fst')

fout, out = open('4cresult.txt', 'w'), ''
f = os.popen('fstinfo 4c5.fst | head -n 6 | tail -n 2')
out += f.read()
f = os.popen('fstinfo 4c6.fst | head -n 6 | tail -n 2')
out += f.read()
fout.write(out)
fout.close()

os.system('fstdraw --portrait --nodesep=0.01 --height=15 --isymbols=table4.txt --osymbols=table4.txt 4c6.fst 4c6.dot')
os.system('dot -Tps 4c6.dot > 4c6.ps')

# os.system('printstrings.O2 --label-map=table4.txt --input=4c4.fst -n 10 -w')

# 4d
os.system('fstcompose 4c6.fst 4.lm.fst 4d.fst')
f = os.popen('fstprint --isymbols=table4.txt --osymbols=table4.txt 4d.fst')
out = ''
for line in f:
    l = line.split('\t')
    if len(l) > 3:
        sym = l[2]
        if sym != '<space>':
            out += sym
        else:
            out += ' '
print out
# os.system('printstrings.O2 --label-map=table4.txt --input=4d.fst -n 10 -w')
