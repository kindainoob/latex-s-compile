import sys
import os

args = sys.argv

# 引数が1つでないならコンパイル
if len(args) != 1:
    # 引数の数を得る
    length = len(args)-1
    # 引数の数だけループ
    for num in range(length):
        # 引数の1番目から
        num += 1
        filename = args[num]

        os.system('platex ../' + filename + '.tex')
        os.system('platex ../' + filename + '.tex')
        os.system('dvipdfmx ' + filename + '.dvi')

        os.system('mv ' + filename + '.pdf ../')

os.system('rm ../*.log ../*.aux../*.dvi')
os.system('rm *.log *.aux *.dvi')
