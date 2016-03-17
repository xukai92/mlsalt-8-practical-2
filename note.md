HIFST=/home/wjb31/src/hifst.mlsalt-cpu1.5Nov15/ucam-smt/
export PATH=$PATH:$HIFST/bin/
export PATH=$PATH:$HIFST/externals/openfst-1.5.0/INSTALL_DIR/bin/
fstcompile --isymbols=isyms.txt --osymbols=osyms.txt eg1.txt eg1.fst
fstprint --isymbols=isyms.txt --osymbols=osyms.txt eg1.fst
fstdraw --isymbols=isyms.txt --osymbols=osyms.txt eg1.fst eg1.dot
dot -Tps eg1.dot > eg1.ps
fstinfo eg1.fst
printstrings.O2 --label-map=isyms.txt --input=eg1.fst -n 10 -w
printstrings.O2 --label-map=osyms.txt --input=eg1o.fst -n 10 -w 2> /dev/null
fstcompile --isymbols=isyms.txt --osymbols=isyms.txt input.txt input.fst
fstcompile --isymbols=isyms.txt --osymbols=osyms.txt model.txt model.fst
fstarcsort --sort_type=olabel input.fst input_sorted.fst
fstarcsort --sort_type=ilabel model.fst model_sorted.fst
fstcompose input_sorted.fst model_sorted.fst comp.fst
fstproject --project_output comp.fst result.fst
fstrmepsilon result.fst | fstdeterminize | fstminimize - result2.fst
printstrings.O2 --label-map=osyms.txt --input=result2.fst -n 10 -w 2> /dev/null
fstconcat
fstunion
fstcompose
fstintersect
fstdifference
fstrmepsilon
fstdeterminize
fstminimize
fstshortestdistance
fstshortestpath
fstprune
fstproject
fstarcsort
fsttopsort
fstreverse
fstinvert
fstclosure
fstpush
fstrelabel
fstreplace
