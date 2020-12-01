import os.path as osp

import pandas as pd

# By default, reading the following files and producing a coding analysis
# Accepts the codings in valid_codings, if detecting other codings, will print warning messages
script_dir = osp.dirname(__file__)
conservative_pth = osp.join(script_dir, '..', 'data', 'annotations', 'Conservative.xlsx')
politics_pth = osp.join(script_dir, '..', 'data', 'annotations', 'Politics.xlsx')
valid_codings = {'E', 'C', 'PC', 'PA'}

df_c = pd.read_excel(conservative_pth)
df_p = pd.read_excel(politics_pth)
counter_c = {}
counter_p = {}
sum_c = sum_p = 0

for i, row in df_c.iterrows():
    coding = row['Coding']
    if coding not in valid_codings:
        if not (type(coding) is float):
            print(f'warning from df_c, row {i}', coding)
    else:
        sum_c += 1
        if coding not in counter_c:
            counter_c[coding] = 1
        else:
            counter_c[coding] += 1

for i, row in df_p.iterrows():
    coding = row['Coding']
    if coding not in valid_codings:
        if not (type(coding) is float):
            print(f'warning from df_p, row {i}', coding)
    else:
        sum_p += 1
        if coding not in counter_p:
            counter_p[coding] = 1
        else:
            counter_p[coding] += 1

print('In conservative')
for k in counter_c.keys():
    print(f'{k}: {counter_c[k] / sum_c}')

print()

print('In politics')
for k in counter_p.keys():
    print(f'{k}: {counter_p[k] / sum_p}')
