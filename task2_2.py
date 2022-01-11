task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for el in task_list:
    if el.isdigit():
        new_list.extend(
            ['"', el.zfill(2), '"'])
    elif el[1:].isdigit() and el[0] == "-" or el[0] == "+":
        new_list.extend(
            ['"', el.zfill(3), '"'])
    else:
        new_list.append(el)
str_answer = []
dub_sing = False

for i in range(len(new_list)):
    str_answer.append(new_list[i])
    if new_list[i] == '"' and not dub_sing:
        dub_sing = True
    elif new_list[i] == '"' and dub_sing:
        str_answer.append(" ")
        dub_sing = False
    elif new_list[i] != '"' and i + 1 != len(new_list) and not dub_sing:
        str_answer.append(" ")
print("".join(str_answer))
