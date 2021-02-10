import argparse
import re
    
def findDuplicate(sen):
        
    dict_dup = {}
    res= re.compile(r'[^\W\s]+')
    sen_1 = res.findall(sen.lower()) # reg ex is used to strip off all the punctuations 
    for word in set(sen_1): # set is used to avoid looping for duplicate entries.
        if sen_1.count(word) > 1:
            dict_dup[word] = sen_1.count(word)

    if not dict_dup:
        in_str = "\nThe sentence : " + sen + ": has " + str(len(dict_dup)) + " duplications "
    else:
        in_str = "\nThe sentence : " + sen + ": has " + str(len(dict_dup)) + " duplications :" + str(dict_dup)[1:-1]
        
    print(in_str)
     

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''This function takes a sentence or list of words as an arugument and prints the duplicate entries and number of 
    occurances of duplicate entries. ''')
    parser.add_argument('-sen', '--sentence',required=True,help='Enter a sentence or list of words')
    args = parser.parse_args()
    findDuplicate(args.sentence)


    

    
