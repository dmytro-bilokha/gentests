# GenTests

In the repository I put two simple python scripts with the example of they
work.  This scripts were used to generate paper tests to check student's
knowledge level.

## Using Scripts
### General Information

The software is intended to generate tests variants from the latex files
given with questions and answers. The script just mixes questions and
answers in random way to create different variants of same questions.
Variants differ by the order of questions in the test and by the order of
answers in the question. The test variant has assigned identify letter.
Each question in test contains one right and some wrong answers.  For
example, the first question in the variant 'A' has the right answer under
the 4th variant.  But, the same question in the 'B'-test is 8th with the
right answer under the 6th variant.  The goal of such mixing is to prevent
easy answers sharing by students.

Provided two scripts:

1. `gentests.py` is used to generate tests. It takes data from latex files with
hard-coded names and puts answers to the file named `ansdb.txt`

2. `checktest.py` is used to check the test. It reads right answers from `ansdb.txt`
and takes numbers of student's answers from command line argument. On checking
script shows the number of right answers.

Both scripts are situated in
[/scripts](https://github.com/dmytro-bilokha/gentests/tree/master/scripts/).

### Data Preparation

To generate tests one should prepare and put in the working directory such files:

 * `preamble.tex` - file with heading part of the test;

 * `postamble.tex` - file with ending of the test;

 * `question0.tex`, `question1.tex`, etc. - files with test questions. Each
 file contains one question;

 * `answers0.tex`, `answers1.tex`, etc. - files with answers. Each file
 contains all answers on corresponding question (i.e. 0-0, 1-1...). The
 right answer must be the first in the answers file. Quantity of answer
 variants must be equal for all questions.

All this files and scripts should be putted in the working directory.
Examples of input files are included in
[/input-files-example](https://github.com/dmytro-bilokha/gentests/tree/master/input-files-example/).
Also, it may be needed to edit constants in the scripts sources. In the
`gentests.py`:

 * `numq` number of questions to process (default is 10);
 * `numa` number of answers for each question (default is 8);
 * `numt` number of test variants to generate (default is 6).

In the `checktest.py`:

 * `numq` number of questions in the test (default is 10).

### Tests Generation

To generate tests just execute `./gentests.py N` in the working directory,
where `N` is number of test bunch. If everything is OK, pdf-files with
tests and answers file (`ansdb.txt`) will be generated.  Examples of
generated tests are included in
[/output-files-example](https://github.com/dmytro-bilokha/gentests/tree/master/output-files-example/).

### Test Checking

To check test results run `./checktest.py NV-12345678`, where:

 * `N` is number of the test bunch to check;
 * `V` is variant of the test, i.e. 'A', 'B', 'C', etc.
 * `12345678` are numbers of answers choosed by the student. In this example student choosed
the answer '1' for the first question, the answer variant number '2' for the second question
 and so on.

Script will compare answers numbers with data from file `ansdb.txt` and print how many questions
were answered right.

## Requirements

 * Python interpreter, because scripts are written in Python language. It
 may be needed to edit first line of scripts to set correct path to
 interpreter executable. Script contains `/usr/local/bin/python` which is
 default for FreeBSD.

 * TeX Live or another TeX installation with `pdflatex` tool. Pdflatex is
used to create output pdf-files from input latex files.
