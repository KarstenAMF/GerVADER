import csv
import pathlib
import random

def splitTweetsTsv():
    with open('tweets.tsv', encoding="utf-8") as tsvfile, open('tweets_positive.tsv', 'w', encoding="utf-8") as tsvout, open('tweets_negative.tsv', 'w', encoding="utf-8") as tsvneg, open('tweets_neutral.tsv', 'w', encoding="utf-8") as tsvneu:
      tsvfile = csv.reader(tsvfile, delimiter='\t')
      tsvout = csv.writer(tsvout, delimiter='\t', lineterminator='\n')
      tsvneg = csv.writer(tsvneg, delimiter='\t', lineterminator='\n')
      tsvneu = csv.writer(tsvneu, delimiter='\t', lineterminator='\n')
      for row in tsvfile:
          if row[1] == "positive":
            tsvout.writerow([row[0],row[1],row[2]])
          if row[1] == "neutral":
              tsvneu.writerow([row[0],row[1],row[2]])
          if row[1] == "negative":
              tsvneg.writerow([row[0],row[1],row[2]])

def klingerFormatterToGERVaderFormat(filename, includeNeutral):
    with open(filename, encoding="utf-8") as tsvfile, open(filename.split(".csv")[0]+".tsv", 'w', encoding="utf-8") as tsvout:
        tsvfile = csv.reader(tsvfile, delimiter='\t')
        tsvout = csv.writer(tsvout, delimiter='\t', lineterminator='\n')
        for row in tsvfile:
            rating = "neutral"
            if int(row[1]) < 3:
                rating = "negative"
            elif int(row[1]) > 3:
                rating = "positive"
            elif not includeNeutral:
                continue;

            headline = row[2]
            if not headline.endswith("!") and not headline.endswith(".") and not headline.endswith("?"):
                if headline.strip() != "":
                    headline = headline + ". "
            comment = headline.lstrip() + row[3].lstrip()


            tsvout.writerow([row[4], rating, comment, row[0]])
    print("Done")

def klingerFormatterToGERVaderFormatEntry(includeNeutral = True):
    klingerDirectory = pathlib.Path('./klinger-reviews/')

    csvPattern = "*.csv"

    for currentFile in klingerDirectory.glob(csvPattern):
        print(currentFile)
        filename = './klinger-reviews/' + currentFile.name
        todofile = './klinger-reviews/' + currentFile.name.split(".csv")[0]+".tsv"
        print(todofile)
        if pathlib.Path(todofile).is_file():
            # file exists
            print("File found")
        else:
            klingerFormatterToGERVaderFormat(filename, includeNeutral)

def tenPercentSb10k(includeNeutral = True):
    filename = "tweets.tsv"
    my_file = pathlib.Path(filename)
    if my_file.is_file():
        # file exists
        print("File found")
    else:
        print("File not found, aborting")
        return 0

    size = 0
    linenumbers = []

    with open('tweets.tsv', encoding="utf-8") as tsvfile:
        tsvfile = csv.reader(tsvfile, delimiter='\t')
        for row in tsvfile:
            if includeNeutral:
                linenumbers.append(size)
            else:
                if not row[1] == "neutral":
                    linenumbers.append(size)
            size += 1

    random.shuffle(linenumbers)

    tenpercent = int(size / 10)
    lineSet = set(linenumbers[:tenpercent])

    print(lineSet)

    currentline = 0

    neutralString = ""
    if not includeNeutral:
        neutralString = "__no_neutral"

    with open('tweets.tsv', encoding="utf-8") as tsvfile, open('./sb10k10percent/tweets_10percent4'+neutralString+'.tsv', 'w', encoding="utf-8") as tsvout:
        tsvfile = csv.reader(tsvfile, delimiter='\t')
        tsvout = csv.writer(tsvout, delimiter='\t', lineterminator='\n')
        for row in tsvfile:
            if currentline in lineSet:
                tsvout.writerow([row[0],row[1],row[2]])
            currentline += 1


if __name__ == '__main__':
    print("Welcome to GERVaders TSVHandler")
    print("Which mode do you want to use? (1 or 2)")
    print("1) unavailable")
    print("2) Split SCARE dataset")
    print("3) Build 10% of SB10k corpus including neutral tweets (tweets.tsv)")
    print("4) Build 10% of SB10k corpus without neutral tweets (tweets.tsv)")
    mode = input("==>")
    if mode.lower().strip() == "1":
        print("Mode is unsupported, go to the line of code to reactivate it")
        # splitTweetsTsv()
    elif mode.lower().strip() == "2":
        print("Include neutral? Y/N")
        neutral = input("==>")
        if neutral.lower().lstrip() == "" or neutral.lower().lstrip() == "y":
            klingerFormatterToGERVaderFormatEntry(True)
        else:
            klingerFormatterToGERVaderFormatEntry(False)
    elif mode.lower().strip() == "3":
        tenPercentSb10k()
    elif mode.lower().strip() == "4":
        tenPercentSb10k(False)
    else:
        print("No mode selected, closing GERVader")
