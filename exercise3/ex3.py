import os


# zero
zero = ['0']
zerosym = ['zero']

fout, out = open('zero.txt', 'w'), ''
for d, s in zip(zero, zerosym):
    out += '0 1 {d} {s}\n'.format(d=d, s=s)
out += '1'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table3.txt --osymbols=table3.txt zero.txt zero.fst')
os.system('fstdraw --isymbols=table3.txt --osymbols=table3.txt zero.fst zero.dot')
os.system('dot -Tps zero.dot > zero.ps')

# one29
one29 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
one29sym = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

fout, out = open('one29.txt', 'w'), ''
for d, s in zip(one29, one29sym):
    out += '0 1 {d} {s}\n'.format(d=d, s=s)
out += '1'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table3.txt --osymbols=table3.txt one29.txt one29.fst')
os.system('fstdraw --isymbols=table3.txt --osymbols=table3.txt one29.fst one29.dot')
os.system('dot -Tps one29.dot > one29.ps')

# ten219
ten219 = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
ten219sym = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

fout, out = open('ten219.txt', 'w'), ''
for d, s in zip(ten219, ten219sym):
    out += '0 1 {d} {s}\n'.format(d=d[1], s=s)
out += '1'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table3.txt --osymbols=table3.txt ten219.txt ten219.fst')
os.system('fstdraw --isymbols=table3.txt --osymbols=table3.txt ten219.fst ten219.dot')
os.system('dot -Tps ten219.dot > ten219.ps')

# twenty290
twenty290 = ['20', '30', '40', '50', '60', '70', '80', '90']
twenty290sym = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

fout, out = open('twenty290.txt', 'w'), ''
for d, s in zip(twenty290, twenty290sym):
    out += '0 1 {d} {s}\n'.format(d=d[0], s=s)
out += '1'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table3.txt --osymbols=table3.txt twenty290.txt twenty290.fst')
os.system('fstdraw --isymbols=table3.txt --osymbols=table3.txt twenty290.fst twenty290.dot')
os.system('dot -Tps twenty290.dot > twenty290.ps')

# hundred
fout, out = open('hundred.txt', 'w'), ''
out += '0 1 <eps> hundred\n'
out += '1'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table3.txt --osymbols=table3.txt hundred.txt hundred.fst')
os.system('fstdraw --isymbols=table3.txt --osymbols=table3.txt hundred.fst hundred.dot')
os.system('dot -Tps hundred.dot > hundred.ps')

# thousand
fout, out = open('thousand.txt', 'w'), ''
out += '0 1 <eps> thousand\n'
out += '1'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table3.txt --osymbols=table3.txt thousand.txt thousand.fst')
os.system('fstdraw --isymbols=table3.txt --osymbols=table3.txt thousand.fst thousand.dot')
os.system('dot -Tps thousand.dot > thousand.ps')

# 0eps
fout, out = open('0eps.txt', 'w'), ''
out += '0 1 0 <eps>\n'
out += '1'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table3.txt --osymbols=table3.txt 0eps.txt 0eps.fst')
os.system('fstdraw --isymbols=table3.txt --osymbols=table3.txt 0eps.fst 0eps.dot')
os.system('dot -Tps 0eps.dot > 0eps.ps')

# 0s
os.system('fstconcat 0eps.fst 0eps.fst 20s.fst')
for i in range(3):
    os.system('fstconcat 0eps.fst {i}0s.fst {j}0s.fst'.format(i=i+2, j=i+3))
for i in range(4):
    os.system('fstrmepsilon {i}0s.fst | fstdeterminize | fstminimize - {i}0s.fst'.format(i=i+2))
    os.system('fstdraw --isymbols=table3.txt --osymbols=table3.txt {i}0s.fst {i}0s.dot'.format(i=i+2))
    os.system('dot -Tps {i}0s.dot > {i}0s.ps'.format(i=i+2))

# 1eps
fout, out = open('1eps.txt', 'w'), ''
out += '0 1 1 <eps>\n'
out += '1'
fout.write(out)
fout.close()

os.system('fstcompile --isymbols=table3.txt --osymbols=table3.txt 1eps.txt 1eps.fst')
os.system('fstdraw --isymbols=table3.txt --osymbols=table3.txt 1eps.fst 1eps.dot')
os.system('dot -Tps 1eps.dot > 1eps.ps')

# 2digits
os.system('fstunion 0eps.fst one29.fst zeroeps29.fst')
os.system('fstconcat twenty290.fst zeroeps29.fst twenty290f.fst')
os.system('fstconcat 1eps.fst ten219.fst ten219f.fst')
os.system('fstconcat zero.fst one29.fst zero29f.fst')
os.system('fstunion twenty290f.fst ten219f.fst 2digits.fst')
os.system('fstunion 2digits.fst zero29f.fst 2digits.fst')

os.system('fstrmepsilon 2digits.fst | fstdeterminize | fstminimize - 2digits.fst')
os.system('fstdraw --portrait --nodesep=0.01 --height=20 --isymbols=table3.txt --osymbols=table3.txt 2digits.fst 2digits.dot')
os.system('dot -Tps 2digits.dot > 2digits.ps')


# 3digits
os.system('fstconcat 0eps.fst 2digits.fst zeroeps2digits.fst')
os.system('fstconcat one29.fst hundred.fst one29hundred.fst')
os.system('fstconcat one29hundred.fst 2digits.fst one29hundred2digits.fst')
os.system('fstunion zeroeps2digits.fst one29hundred2digits.fst 3digits.fst')

os.system('fstrmepsilon 3digits.fst | fstdeterminize | fstminimize - 3digits.fst')
os.system('fstdraw --portrait --nodesep=0.01 --height=20 --isymbols=table3.txt --osymbols=table3.txt 3digits.fst 3digits.dot')
os.system('dot -Tps 3digits.dot > 3digits.ps')

# 5digits
os.system('fstconcat 2digits.fst thousand.fst 2digitsthousand.fst')
os.system('fstunion 3digits.fst 30s.fst 3digitsor30s.fst')
os.system('fstconcat 2digitsthousand.fst 3digitsor30s.fst 5digits.fst')
os.system('fstunion 5digits.fst 50s.fst 5digits.fst')

os.system('fstrmepsilon 5digits.fst | fstdeterminize | fstminimize - 5digits.fst')
os.system('fstdraw --portrait --nodesep=0.01 --height=10 --isymbols=table3.txt --osymbols=table3.txt 5digits.fst 5digits.dot')
os.system('dot -Tps 5digits.dot > 5digits.ps')

