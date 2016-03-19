import os


alphabet = []
fin = open('table4.txt', 'r')
for line in fin:
        sym = line.split(' ')[0]
        if sym.isalpha():
            alphabet.append(sym)
fin.close()

# 4e
fout, out = open('4e.txt', 'w'), ''
l = len(alphabet)
for i in range(l):
    out += '0 {e} {i} <eps>\n'.format(e=i+1, i=alphabet[i])
    out += '{s} 0 <eps> {o}\n'.format(s=i+l+1, o=alphabet[i])
    out += '0 0 {i} {o}\n'.format(i=alphabet[i], o=alphabet[i])
    for j in range(l):
        if alphabet[i] != alphabet[j]:
            out += '{s} {e} {i} {o}\n'.format(s=i+1, e=i+l+1,
                                              i=alphabet[j], o=alphabet[j])
out += '0 0 <space> <space>\n'
out += '0 0 . .\n'
out += '0 0 , ,\n'
out += '0'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table4.txt --osymbols=table4.txt 4e.txt 4e.fst')

os.system('fstdraw --portrait --nodesep=0.01 --height=15 --isymbols=table4.txt --osymbols=table4.txt 4e.fst 4e.dot')
os.system('dot -Tps 4e.dot > 4e.ps')

os.system('fstcompose 4.encoded2.fst 4a.fst 4e1.fst')
os.system('fstcompose 4e1.fst 4e.fst 4e2.fst')
os.system('fstproject --project_output 4e2.fst 4e3.fst')
os.system('fstrmepsilon 4e3.fst | fstdeterminize | fstminimize - 4e4.fst')
os.system('fstcompose 4e4.fst 4.lm.fst 4e5.fst')

f = os.popen('fstprint --isymbols=table4.txt --osymbols=table4.txt 4e5.fst')
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

