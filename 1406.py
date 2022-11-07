import sys

text = list(sys.stdin.readline().strip())
cursor = "#"
text.append(cursor)
M = int(sys.stdin.readline())

for i in range(M):
    cmnd_line = sys.stdin.readline().split()
    cmnd = cmnd_line[0]
    cursor_index = text.index("#")

    if cmnd == "L":
        if cursor_index == 0:
            pass
        else:
            text[cursor_index - 1], text[cursor_index] = text[cursor_index], text[cursor_index - 1]
    
    elif cmnd == "D":
        if cursor_index == len(text) - 1:
            pass
        else:
            text[cursor_index + 1], text[cursor_index] = text[cursor_index], text[cursor_index + 1]
    
    elif cmnd == "B":
        if cursor_index == 0:
            pass
        else:
            del text[cursor_index - 1]
    
    elif cmnd == "P":
        text.insert(cursor_index, cmnd_line[1])

text.remove("#")
answer = "".join(text)
print(answer)