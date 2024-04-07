from pprint import pprint
import re

import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

sp = []
for i in (contacts_list):
    sp.append(" ".join(i[:3]).split())
for i in range(0, 10):
    sp[i][3:] = contacts_list[i][3:]
for i in range(1, 10):
    for j in range(5, 6):
         st = ''
         st += sp[i][j]
         pattern = r"(\+7|8)\s*[\(\s]*(\d{3})[\)\s-]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*[\(\s]*([д\s]*[о\s]*[б\s]\.)*[\.\s]*([\d\s]*)[\s\)]*"
         substitute = r"+7(\2)\3-\4-\5 \6\7"
         result = re.sub(pattern, substitute, st)
         sp[i][j] = result

for i in range(10):
    if len(sp[i]) < 7:
        sp[i].append(' ')

contact_dic = {}

new_contacts_list =[]
for elem in sp:
    if f'{elem[0]} {elem[1]}' in contact_dic.keys():
        if len((contact_dic[f'{elem[0]} {elem[1]}'])[2]) == 0:
            (contact_dic[f'{elem[0]} {elem[1]}'])[2] = elem[2]

        if len((contact_dic[f'{elem[0]} {elem[1]}'])[3]) == 0:
            (contact_dic[f'{elem[0]} {elem[1]}'])[3] = elem[3]

        if len((contact_dic[f'{elem[0]} {elem[1]}'])[4]) == 0:
            (contact_dic[f'{elem[0]} {elem[1]}'])[4] = elem[4]

        if len((contact_dic[f'{elem[0]} {elem[1]}'])[5]) == 0:
            (contact_dic[f'{elem[0]} {elem[1]}'])[5] = elem[5]

        if len((contact_dic[f'{elem[0]} {elem[1]}'])[6]) == 0:
            (contact_dic[f'{elem[0]} {elem[1]}'])[6] = elem[6]

    else:
        contact_dic[f'{elem[0]} {elem[1]}'] = elem

for val in contact_dic.items():
    new_contacts_list.append(val[1])
pprint(new_contacts_list)

pprint(sp)


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)