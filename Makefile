.PHONY : clean
clean :
	rm -f pdftest.pdf pdftest.log pdftest.aux *.png

pdftest.pdf : pdftest testtext.txt ph20_set3_1a1_mk1.png ph20_set3_1a2_mk1.png ph20_set3_2_1a1.png ph20_set3_2_1a2.png ph20_set3_2_1a3.png ph20_set3_2_2a1.png ph20_set3_2_3a1.png ph20_set3_2a1.png ph20_set3_2a2.png ph20_set3_2a3.png ph20_set3_2a4.png ph20_set3_3a1.png ph20_set3_4a1.png ph20_set3_5a1.png ph20_set3_5a2.png ph20_set3_5a3.png ph20_set3_5a4.png ph20_set3_5a5.png ph20_set3_5a6.png  
	pdflatex pdftest

ph20_set3_1a1_mk1.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 1 $@

ph20_set3_1a2_mk1.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 2 $@

ph20_set3_2_1a1.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.1 300 15 $@

ph20_set3_2_1a2.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.1 300 16 $@

ph20_set3_2_1a3.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.1 300 17 $@

ph20_set3_2_2a1.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.1 300 18 $@

ph20_set3_2_3a1.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.1 300 19 $@

ph20_set3_2a1.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 3 $@

ph20_set3_2a2.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 4 $@

ph20_set3_2a3.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 5 $@

ph20_set3_2a4.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 6 $@

ph20_set3_3a1.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 7 $@

ph20_set3_4a1.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 8 $@

ph20_set3_5a1.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 9 $@

ph20_set3_5a2.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 10 $@

ph20_set3_5a3.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 11 $@

ph20_set3_5a4.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 12 $@

ph20_set3_5a5.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 13 $@

ph20_set3_5a6.png : Ph20set3mk1.py
	python2 Ph20set3mk1.py 1 0 0.01 3000 14 $@

