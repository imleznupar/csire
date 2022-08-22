import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from tqdm import tqdm
import re
from word2number import w2n
import nltk
nltk.download('punkt')
from nltk.tag.stanford import StanfordNERTagger

def main(df):
    print("======Extracting Casualty Information...======")


    PATH_TO_JAR='stanford-ner-2020-11-17/stanford-ner.jar'
    PATH_TO_MODEL = 'stanford-ner-2020-11-17/ner-model.ser'
    tagger = StanfordNERTagger(model_filename=PATH_TO_MODEL,path_to_jar=PATH_TO_JAR, encoding='utf-8')
    df.reset_index(drop=True, inplace=True)

    def ner(df):
        df['tokenize'] = df['text'].apply(lambda x: nltk.word_tokenize(x))
        df['ner'] = tagger.tag_sents( df['tokenize'] )
        df['dead'] = np.empty((len(df), 0)).tolist()
        df['injured'] = np.empty((len(df), 0)).tolist()
        df['missing'] = np.empty((len(df), 0)).tolist()

        for i in tqdm(range((df.shape[0]))):
            for j in df.loc[i,'ner']:
                if(j[1]=="DEAD"):
                    df.loc[i,'dead'].append(j[0])
                elif(j[1]=="INJURED"):
                    df.loc[i,'injured'].append(j[0])
                elif(j[1]=="MISSING"):
                    df.loc[i,'missing'].append(j[0])

            
        return df

    def extract_number(lst):
        if not lst:
            return 0

        phrase = lst.replace(',','')
        try:
            x = w2n.word_to_num(phrase)
            return x
        except:
            pass
        
        x = re.findall(r'\b([0-9]*[.]?[0-9]+)*(k| k| thousand| thousands)\b',phrase)
        for jt in x:
            num = float(jt[0])*1000
            try:
                return int(num)
            except:
                pass
        
        x = re.findall(r'\b([0-9]*[.]?[0-9]+)*(m| m| million| millions)\b',phrase)
        for jt in x:
            num = float(jt[0])*1000000
            try:
                return int(num)
            except:
                pass
        
        x = re.findall(r'\d+(?:\.\d+)?',phrase)
        for jt in x:
            try:
                return int(jt)
            except:
                pass
        return 0

    def maxi(lst):
        maxi = 0
        if not lst:
            return maxi
        
        for i in lst:
            tmp = extract_number(i)
            if(tmp>maxi):
                maxi = tmp
                
        return maxi

    df = ner(df)

    df['dead_number'] = 0
    df['injured_number'] = 0
    df['missing_number'] = 0

    df['dead_number'] = df['dead'].apply(lambda x: maxi(x))
    df['injured_number'] = df['injured'].apply(lambda x: maxi(x))
    df['missing_number'] = df['missing'].apply(lambda x: maxi(x))

    return df