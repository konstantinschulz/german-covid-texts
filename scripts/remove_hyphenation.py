# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import duden
import spacy
import treetaggerwrapper
import fire

#https://pypi.org/project/treetaggerwrapper/

def remove_hyphenation(file_dir, out_dir, tagger="treetagger"):
    """ 
    Removes unnecessary hyphenation from already tokenized text.
        
    Parameters
    ----------
    
    file_dir: str
        Directory to input files.
    out_dir: str
        Directory to input files.
    tagger (optional): str
        Tagger for lemmatization.
        Default is 'treetagger', other possible value is 'spacy'.
        
    Returns
    -------
    None.    
    """
    files = [f for f in listdir(file_dir) if isfile(join(file_dir, f))]
    if tagger == "treetagger":
        for f in files:
            print(f)
            tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
            with open(file_dir + f, "r", encoding="utf8") as inp, open(out_dir + "hyph_" + f, "w", encoding="utf8") as out:
               lines = inp.read()
               lines = lines.split(" ")
               index = 0
               text_tokenized = []
               skip_next = False
               for word in lines:
                   if word.endswith("-"): 
                       next_word = lines[index+1]
                       word_rm = word[:-1]
                       #print(word_rm, next_word)
                       tags = tagger.tag_text(word_rm + next_word)
                       lemmatize = treetaggerwrapper.make_tags(tags)
                       lemma = lemmatize[0][2]
                       #print(lemma)
                       if next_word[0].islower() and duden.search(lemma) != []:
                           word = word_rm + next_word
                           #print(word)
                           text_tokenized.append(word)
                           skip_next = True
                       else:
                           if skip_next:
                               skip_next = False
                               index += 1
                               continue
                           text_tokenized.append(word)
                   else:
                       if skip_next:
                           skip_next = False
                           index += 1
                           continue
                       text_tokenized.append(word)
                   index += 1
               out.write(" ".join(text_tokenized))
    elif tagger == "spacy":
        nlp = spacy.load('de_core_news_lg')
        for f in files:
            print(f)
            with open(file_dir + f, "r", encoding="utf8") as inp, open(out_dir + "hyph_" + f, "w", encoding="utf8") as out:
               lines = inp.read()
               lines = lines.split(" ")
               index = 0
               text_tokenized = []
               skip_next = False
               for word in lines:
                   if word.endswith("-"): 
                       next_word = lines[index+1]
                       word_rm = word[:-1]
                       #print(word_rm, next_word)
                       lemmatize = nlp(word_rm + next_word)
                       lemma = [x.lemma_ for x in lemmatize][0]
                       if next_word[0].islower() and duden.search(lemma) != []:
                           word = word_rm + next_word
                           #print(word)
                           text_tokenized.append(word)
                           skip_next = True
                       else:
                           if skip_next:
                               skip_next = False
                               index += 1
                               continue
                           text_tokenized.append(word)
                   else:
                       if skip_next:
                           skip_next = False
                           index += 1
                           continue
                       text_tokenized.append(word)
                   index += 1
               out.write(" ".join(text_tokenized))
    else:
        print("Possible values for 'tagger' are currently only 'spacy' or 'treetagger' (default).")

if __name__=='__main__':       
    
    fire.Fire() 
#    remove_hyphenation("C:/Users/melin/Desktop/panqura/test_sample/", "C:/Users/melin/Desktop/panqura/test_output/")