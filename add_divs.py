import pandas as pd
import os
import json



with open('Presentation.ipynb', 'r', encoding='utf8') as f:
    doc = json.load(f)
    new_doc = doc.copy()
    # print(len(new_doc['cells']))
    for i in range(len(new_doc['cells'])):
        if sum(['###' in j for j in new_doc['cells'][i]['source']]) > 0:
            print(new_doc['cells'][i]['source'])
    #     cell = new_doc['cells'][i]
    #     cell['source'] = ['<div class="general-container">'] + cell['source'] + ['</div>']
    #     new_doc['cells'][i] = cell
    # with open('Presentation1.ipynb', 'w', encoding='utf8') as w:
    #     json.dump(new_doc, w)