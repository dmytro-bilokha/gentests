#!/usr/local/bin/python
# -*- coding: koi8-u -*-
import locale, sys, os, random

numq = 10 # number of questions to process
numa = 8 # number of answers for each question
numt = 6 # number of test variants to generate
questions= []
answers = []
letters_t = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K')

argums = sys.argv
pz_num = argums[1]
ansdb = open("ansdb.txt", "wb")
for i in range(numq):
    try:
        qfile = open("question"+str(i)+".tex", "rb")
    except:
        print "Unable to open file question%d.tex" % i
        sys.exit(-1)
    questions.append(qfile.read())
    qfile.close()
    try:
        afile = open("answers"+str(i)+".tex", "rb")
    except:
        print "Unable to open file answers%d.tex" % i
        sys.exit(-1)
    ans = []
    for line in afile.readlines():
        ans.append(line)
    answers.append(ans)
    afile.close()
for j in range(numt):
    ques = questions[:]
    answ = [[]]*len(answers)
    for i in range(len(answers)):
        answ[i] = answers[i][:]
    outfile = open("test.tex", "wb")
    outfile.write("\\input{preamble}\n\\begin{enumerate}[\\bfseries 1.]\n")
    shifr_a = ""
    for i in range(numq):
        idx = random.randrange(len(ques))
        outfile.write("\\begin{multicols}{2}[\\item %s]\n" % ques[idx])
        was_no_true = 1
        outfile.write("\\begin{enumerate}[1)]\n")
        for k in range(numa):
            aidx = random.randrange(len(answ[idx]))
            if was_no_true and aidx == 0:
                was_no_true = 0
                shifr_a = shifr_a+str(k+1)
            outfile.write("\\item %s" % answ[idx].pop(aidx))
        outfile.write("\\end{enumerate}\n\\end{multicols}\n")
        del ques[idx]
        del answ[idx]
    outfile.write("\\end{enumerate}\n\\input{postamble}\n")
    outfile.close()
    outfile = open("shifr.tex", "wb")
    outfile.write(pz_num+letters_t[j])
    outfile.close()
    ansdb.write(pz_num+letters_t[j]+"-"+shifr_a+'\n')
    os.system('pdflatex test.tex')
    os.rename('test.pdf', 'Test-'+pz_num+letters_t[j]+'.pdf')
ansdb.close()
