import pandas as pd
from pprint import pprint
import json
df = pd.read_csv('DATAS/AmazonCats.csv', sep=";")


tree_main_cat = df['Main_Category'].drop_duplicates().dropna().tolist()
tree_sub1_cat = df['Subcategory 1'].drop_duplicates().dropna().tolist()
tree_sub2_cat = df['Subcategory 2'].drop_duplicates().dropna().tolist()
tree_sub3_cat = df['Subcategory 3'].drop_duplicates().dropna().tolist()




big_data = {}

for layer1 in tree_main_cat:
    for layer2 in tree_sub1_cat:
        match = df[(df["Main_Category"] == layer1) & (df["Subcategory 1"] == layer2)]
        
        insertion_var = match["Subcategory 2"].dropna().unique().tolist()

        if layer1 not in big_data:
            big_data[layer1] = {}
        if layer2 not in big_data[layer1]:
            big_data[layer1][layer2] = {}

        for i in insertion_var:
            big_data[layer1][layer2][i] = {}
            
            match_sub2 = match[match["Subcategory 2"] == i]

            insertion_var2 = match_sub2["Subcategory 3"].dropna().unique().tolist()

            for bns in insertion_var2:
                if i not in big_data[layer1][layer2]:
                    big_data[layer1][layer2][i] = {}
                big_data[layer1][layer2][i][bns] = []

            print("Processed", layer1, layer2, i)



with open('fetched-cats.json', 'w', encoding='utf-8') as f:
    json.dump(big_data, f, ensure_ascii=False, indent=4)



