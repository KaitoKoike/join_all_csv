import os
import glob
from tqdm import tqdm

is_header_have = False
output_file_name = "result.csv"
results = open(output_file_name,"w",encoding="shift-jis")

for file_path in tqdm(glob.glob("data/*.csv")):
    f = open(file_path,"r",encoding="shift-jis")
    texts = f.readlines()
    if is_header_have is False:
        results.writelines(texts)
        is_header_have = True
    else:
        results.writelines(texts[1:])
    
results.close()
