import vaderSentimentGER as GERVADER
import pathlib
import datetime

def sentimentOneRun():
    print("\nWhich file do you want to work with")
    do_translate = input("Hit enter if you want to read tweets.tsv, otherwise type the name\n ==>")
    filename = "tweets.tsv"
    if do_translate.lower().lstrip() == "":
        print("No input, working with tweets.tsv")
    else:
        print("Trying to open the specified file")
        filename = do_translate.lower().lstrip()

    my_file = pathlib.Path(filename)
    if my_file.is_file():
        # file exists
        print("File found")
    else:
        print("File not found, aborting")
        return 0

    do_translate = input("Creating output directory. Do you want to set a custom name? \nY/N: ")
    directoryname = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    if do_translate.lower().strip() == "y":
        directoryname = input("Name:")
        if directoryname.strip() == "":
            directoryname = str(datetime.datetime.now()).split('.')[0]


    pathlib.Path('./results/mode_All/'+directoryname).mkdir(exist_ok=True)

    print("GERVader in this Mode will analyze all sentences and rate them +,0,-")
    print("Therefore you will see 3 output files")
    print("Analyzing ALL statements")
    GERVADER.sentimentAll(filename, directoryname)


def sentimentSplitter():
    print("\nWhich file do you want to work with")
    do_translate = input("Hit enter if you want to read tweets.tsv, otherwise type the name\n ==>")
    filename = "tweets.tsv"
    if do_translate.lower().lstrip() == "":
        print("No input, working with tweets.tsv")
    else:
        print("Trying to open the specified file")
        filename = do_translate.lower().lstrip()

    my_file = pathlib.Path(filename)
    if my_file.is_file():
        # file exists
        print("File found")
    else:
        print("File not found, aborting")
        return 0

    do_translate = input("Creating output directory. Do you want to set a custom name? \nY/N: ")
    directoryname = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    if do_translate.lower().strip() == "y":
        directoryname = input("Name:")
        if directoryname.strip() == "":
            directoryname = str(datetime.datetime.now()).split('.')[0]


    pathlib.Path('./results/'+directoryname).mkdir(exist_ok=True)
    pathlib.Path('./results/'+directoryname+"/"+"positive").mkdir(exist_ok=True)
    pathlib.Path('./results/'+directoryname+"/"+"negative").mkdir(exist_ok=True)
    pathlib.Path('./results/'+directoryname+"/"+"neutral").mkdir(exist_ok=True)

    print("GERVader works by first checking for the positive, then negative, and then neutral data")
    print("Therefore you will see 3 different directories and results")

    print("\nAnalyzing POSITIVE statements")
    GERVADER.entry(filename, directoryname, "positive")
    print("Analyzing NEUTRAL statements")
    GERVADER.entry(filename, directoryname, "neutral")
    print("Analyzing NEGATIVE statements")
    GERVADER.entry(filename, directoryname, "negative")

if __name__ == '__main__':
    print("Welcome to GERVader")
    print("Which mode do you want to use? (1 or 2)")
    print("1) Split analysis into 3 steps. Analyze all positive statements, analyze all neutral statements, analzye all negative statements")
    print("2) Analyze all input in one step. For detailed correctness calculation, use 1)")
    mode = input("==>")
    if mode.lower().strip() == "1":
        sentimentSplitter()
    elif mode.lower().strip() == "2":
        sentimentOneRun()
    else:
        print("No mode selected, closing GERVader")
