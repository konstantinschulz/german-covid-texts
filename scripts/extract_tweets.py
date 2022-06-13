# Creates csv files with extracted tweets+metadata in /data/sources/meta/twitter_csv/ and txt-files for annotations in /data/sources/plain_text/twitter/
import os
import os.path
import twint
import pandas as pd
import glob
# basic cleaning with tweet-preprocessor -> excludes German Umlaute
#import preprocessor as p
import re
from pathlib import Path

"""set root dir for script"""
SCRIPT_ROOT = os.path.dirname(__file__)
print("ROOT ", SCRIPT_ROOT)
p = Path(SCRIPT_ROOT)
ROOT = str(p.parent)
print("ROOT: ", ROOT)


def extract_tweets(list_tags, period):
    """use twint pkg to extract tweets and metadata based on search-queries (tag) and between time periods, write each query output in one csv-file"""
    tweet_dir = ROOT + "/data/sources/meta/twitter_csv/"
    for tag in list_tags:
        for i1, i2 in period:
            print(tag)
            #twint extraction
            c = twint.Config()
            c.Search = tag
            c.Lang = "de"
            c.Limit = 100
            startdate = i1
            c.Since = startdate
            c.Until = i2
            c.Store_csv = True 
            files_path = tweet_dir + f"temp/queried_tweets_{tag}_{startdate}.csv"
            c.Output = files_path
            twint.run.Search(c)
            #open csv in df and write in query
            try:
                df = pd.read_csv(files_path, encoding="utf-8-sig")
                df['query'] = tag
                df.to_csv(files_path)
            except:
                print(files_path , 'not found')

    return tweet_dir
        
def merge_csv_files(tweet_dir):
    """merge all csv tables in /temp into one csv file"""
    os.chdir(tweet_dir+"temp/")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv(tweet_dir+"/twitter_meta_notproc.csv", index=False, encoding='utf-8-sig')
    combined_path = tweet_dir + "/twitter_meta_notproc.csv"
    return combined_path



def remove_emojis(data):
    """for preproc remove emojis and other imgs from string"""
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)


def preproc_tweets(df_comb):
    """filter duplicates, short tweets and preprocess tweet strings"""
    # rm duplicates
    orig_rows = df_comb.shape[0]
    df_comb.drop_duplicates(inplace=True, subset="tweet")
    new_rows = df_comb.shape[0]
    print("excluded", orig_rows - new_rows, "duplicate tweets. Old num rows: ", orig_rows, "New num rows: ", new_rows)
    
    # exclude posts with less than 10 tokens
    print("num of rows: ", df_comb.shape[0])
    df_comb['length_tweet'] = df_comb['tweet'].apply(lambda x: len(x.split()))
    cond = df_comb['length_tweet'] > 20
    df_sm = df_comb[cond]
    print("num of rows wc > 10: ", df_comb.shape[0])
    df_sm = df_comb[['id', 'tweet']]
    df_sm = df_sm.rename(columns={'tweet': 'tweet_text'})

    df_sm['tweet_text'] = df_sm['tweet_text'].apply(lambda x:  re.sub(r'https?://[^ ]+', '', x)) #rm urls
    df_sm['tweet_text'] = df_sm['tweet_text'].apply(lambda x:  re.sub(r'@[^ ]+', '@XXX', x)) #replace usernames with XX
    df_sm['tweet_text'] = df_sm['tweet_text'].apply(lambda x:  re.sub(r'(#)([^ ]+)', r'\1 \2', x)) #include ' ' after hashtags
    #df_sm['tweet_text'] = df_sm['tweet_text'].apply(lambda x:  re.sub(r'([A-Za-z])\1{2,}', r'\1', x)) # normalization of character repetition 
    df_sm['tweet_text'] = df_sm['tweet_text'].apply(lambda x:  remove_emojis(x))

    df_sm.to_csv(ROOT +"/data/sources/twitter_csv/twitter_meta.csv", index=False, encoding='utf-8-sig')
    return df_sm


def write_to_txt(df_sm):
    """write each row with "tweet_text" from csv file into a .txt file, use 'id' for filename"""
    dirpath = ROOT + "/data/sources/plain_text/twitter/"
    list_id = df_sm['id'].tolist()
    print(len(list_id))
    list_tweets = df_sm['tweet_text'].tolist()
    for i, t in zip(list_id, list_tweets):  
        if str(i).isdecimal():      
            with open(dirpath + 'tweet_' + str(i) + ".txt", "w", encoding='utf-8-sig') as f:
                f.write(t)


if __name__ == "__main__":

    list_tags = ["corona", "coronavirus", "covid", "covid-19", "SARSCoV2" "impfung", "impfstoff", "boosterimpfung", "auffrischungsimpfung", "impfreaktionen", "nebenwirkungen", "longcovid",  "pandemie", "quarantäne", "isolierung", "coronabeschränkungen", "rki", "bzga"]
    period = [("2021-11-01", "2021-12-01"), ("2021-12-02", "2022-01-01"), ("2022-01-02", "2022-02-01"), ("2022-02-02", "2022-03-01"), ("2022-03-02", "2022-04-01")]
    #list_tags = ["corona", "SARSCoV2", "impfung"]
    #period = [("2021-11-01", "2021-12-01"), ("2021-12-02", "2022-01-01")]
    tweet_dir = extract_tweets(list_tags,period)
    combined_path = merge_csv_files(tweet_dir)

    combined_path = ROOT + "/data/sources/twitter_csv/twitter_meta_notproc.csv"
    df_comb = pd.read_csv(combined_path, encoding="utf-8-sig")
#    debugging 
#    print_plot(0, df_comb)
    
    preproc_tweets(df_comb)

    df_sm_clean = pd.read_csv(ROOT + "/data/sources/twitter_csv/twitter_meta.csv", encoding="utf-8-sig")
    write_to_txt(df_sm_clean)






 



