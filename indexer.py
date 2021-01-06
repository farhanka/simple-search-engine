from pathlib import Path
import re
import sys
import math
from tqdm import tqdm
import json




def get_text(text, tag):

    get = re.search(f'<{tag}>(.*?)</{tag}>', text)
    return get.group(1)

def index(hashs, words):
     for word in words:
            if word in hashs:
                hashs[word] += 1
            else:
                hashs[word] = 1

def calculate_idf():
    idf = {}
    for term in tf:
        total_doc = 0
        for doc_id in df:
            if term in df[doc_id]:
                total_doc += 1
        try:
            idf_doc = math.log2(len(df)/total_doc)
        except:
            idf_doc = 0
        idf[term] = idf_doc
    return idf


BASE_DIR = Path(__file__).resolve().parent
IN_DIR = BASE_DIR / 'download/'

df, tf = {}, {}
total_file = 0

print("Processing Data...")
for path in IN_DIR.glob('**/cleaned/*.html'):        #uncomment ini untuk baca dari dokumen yang sudah dibersihkan
# for path in IN_DIR.glob('**/scrapped/*.html'):     #uncomment ini untuk baca dari dokumen original
    with open(path.resolve(), 'r', encoding='utf-8') as file:
        df[path.name] = {}
        text = file.read()
        try:
            terms = get_text(text, 'title') + ' ' + get_text(text, 'top') + ' ' + \
                get_text(text, 'middle') + ' ' + get_text(text, 'bottom')
            words = terms.split()
        except:
            print()

        index(df[path.name], words)
        index(tf, words)
        total_file += 1

inverted_index = {}
idf = calculate_idf()
with open(BASE_DIR / 'words_score.txt', 'w', encoding='utf-8') as file:
    for term, term_freq in tqdm(tf.items()):
        file.write(term + ' ')
        for doc_id in df.keys():
            doc_tf = 0
            total_term = 0
            if term in df[doc_id]:
                doc_tf = df[doc_id][term]
            total_term += sum(df[doc_id].values())
            term_frequency = doc_tf / total_term
            w = term_frequency * idf[term]

            if term in inverted_index:
                inverted_index[term][doc_id] = w
            else:
                inverted_index[term] = {}
                inverted_index[term][doc_id] = w
                
            if w > 0:
                file.write(f'%s:%.3f ' % (doc_id, w))
        file.write('\n')