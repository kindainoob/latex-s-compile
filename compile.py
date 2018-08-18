import sys
import os


args = sys.argv
length = len(args)-1
for num in range(length):
    num += 1

    filename = args[num]

    os.system('platex ../' + filename + '.tex')
    os.system('platex ../' + filename + '.tex')
    os.system('dvipdfmx ' + filename + '.dvi')

    os.system('mv ' + filename + '.pdf ../')

os.system('rm ../*.log ../*.aux../*.dvi')
os.system('rm *.log *.aux *.dvi')
