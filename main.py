# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
with open('random_int.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
processed_lines = []
for line in lines:
    new_line = []
    for word in line.split():
        if word in reserved_words:
            new_line.append(word)
        else:
            new_line.append(word.upper())
    processed_lines.append(' '.join(new_line) + '\n')
with open('random_int_converted.py', 'w', encoding='utf-8') as f:
    f.writelines(processed_lines)
