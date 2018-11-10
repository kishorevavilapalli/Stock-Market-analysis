import csv
import re
import nltk
def Reading():
    all_documents = []
    with open("c:\Python27/BITCOIN.csv", "r") as csvfile:
        myfile = csv.reader(csvfile)
        for line in myfile:
            print(line[0])
            all_documents.append(line[0])
            print("_________________")

    print (len(all_documents))
    return all_documents


def cleaning(all_documents):
    for tweet in all_documents:
        # we start cleaning the data:
        tweet = re.sub(r"(?:\@|'|http?\://)\s+", "", tweet) # remove customized punctuation
        tweet = re.sub(r'[^\w\s]','', tweet)    # remove punctuation
        tweet = re.sub("\d+", "", tweet) # remove number from text
        tokens_text = nltk.word_tokenize(tweet)
        stopwords = nltk.corpus.stopwords.words('english')  # stopwords reduction
        token_text = [w for w in tokens_text if w not in stopwords]
        tokens_text = [w for w in token_text if len(w) > 2]
        print(tokens_text)

        with open("c:\Python27/cleanedbitcoin.csv", "ab") as csvfile:  # where we save file
            myfile = csv.writer(csvfile)
            myfile.writerow([tokens_text])


def main():
    all_documents = Reading()
    cleaning(all_documents)




main()