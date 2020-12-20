import sys
str1 =""

try:
    file_name = sys.argv[1]
except IndexError:
    print('Usage: {0} TEXTFILE'.format(file_name))
    sys.exit(1)

with open(file_name, 'r') as f:
    # 集合型にすることで重複が消える（順序は保証されない）
    # .rstrip()することで、一番最後の行に改行を入れる必要がなくなる
    unique_texts = {line.rstrip() for line in f}

for i in unique_texts:
    str1 += i+"\n"

with open(file_name, 'w') as f:
    f.writelines(str1)


