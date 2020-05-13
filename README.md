# GerVADER

GerVADER is a German adaptation of the sentiment classification tool VADER. VADER is a lexicon and rule-based approach in classifying sentences into positive, negative or neutral statements and puts a focus on social media texts.

GerVADER copied the process for the German language and comes with its own lexicon and edited rules for the German language. Just like VADER it is free to use.

For more information on **VADER** please check:
> Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

and [GitHub - VADER](https://github.com/cjhutto/vaderSentiment).

## Paper

For more information on **GerVADER**, please check the paper linked here: http://ceur-ws.org/Vol-2454/paper_14.pdf. As part of the LWDA2019 Proceedings: http://ceur-ws.org/Vol-2454/.

Check out the **LWDA2019 presentation**: https://pages.cms.hu-berlin.de/ipa/lwda-pdf/GerVader-eng.ver-1.pdf

### Citation

For your future works, please cite GerVADER as follows.

> Karsten Michael Tymann, Matthias Lutz, Patrick Palsbröker and Carsten Gips: GerVADER - A German adaptation of the VADER sentiment analysis tool for social media texts. In Proceedings of the Conference "Lernen, Wissen, Daten, Analysen" (LWDA 2019), Berlin, Germany, September 30 - October 2, 2019.

## LICENSE

GerVADER is free under MIT-License.

## About GerVADER

Since GerVADER is an adaptation of VADER, most of the algorithm used for sentiment analysis has been kept the same. For greater details please refer to the GerVADER paper.

#### Lexicon

The lexicon has been collected by the author and rated by individuals. The lexicon is for the most parts based on SentiWS.

> R. Remus, U. Quasthoff & G. Heyer: SentiWS - a Publicly Available German-language Resource for Sentiment Analysis.
In: Proceedings of the 7th International Language Ressources and Evaluation (LREC'10), pp. 1168-1171, 2010

**For using GerVADER or just the lexicon make sure to cite [SentiWS](http://wortschatz.uni-leipzig.de/de/download) and accept their license. Moreover the ratings of the lexicon are part of GerVADER, so make sure to quote GerVADER**.

The *GERVaderLexicon_noexpansion* is GERVaders crowd-rated lexicon of german words. The *GERVaderLexicon* has been expanded with the grammatical forms as well as with emoticons and english phrases taken from the *VADER* lexicon. 

More details on the lexicon can be found in GerVADERs paper.

#### Heuristics

VADER has 5 heuristics that can impact the rating of a sentence. These heuristics have either been changed manually by the author for the German language or have been kept the same.

#### Classification

To find out more about GerVADER and its classification scores, please check the paper.

## Requirements
- Python 3.7

## How To Use

### Corpus format

GerVADER accepts tsv (tab-seperated) files without a header line in the given form:

| 1st        | 2nd           | 3rd  |
| ------------- |:-------------:| -----:|
| ID    | Label (positive or negative or neutral) | Sentence |

The file should end on .tsv.

### GerVADER GERvaderModule.py

    python GERvaderModule.py

The module **GERvaderModule** is the entry point for using GerVADER. It comes in 2 modes:

#### Modes

1. Split analysis into 3 steps. Analyze all positive statements, analyze all neutral statements, analzye all negative statements
  - Results in *results/foldername*
  - Sentences need label: positive, negative, neutral
  - Useful for calculating classification scores of GerVADER (e.g. Precision, Recall, F1)
  - example file: *example_corpus.tsv*
2. Analyze all input in one step. For detailed correctness calculation, use 1)
  - Results in *results/mode_All/foldername*
  - Sentences can have any label: unknown, positive, ...
  - Useful for production use when you would not know whether a sentence is positive, negative or neutral.
  - example file: *example_corpus_no_labels.tsv*

The first mode allows to classify all statements and calculate how accurate GerVADER classifies the input. It splits the data accordingly into folders, therefore allowing you to check how the tool rated every label.

The second mode is useful for classifying the statements without needing to know whether GerVADER classified a statement correctly. Therefore it can be used without labels for production use.

The module will guide you through in how to use it on execution.

### tsvhandler.py

Allows to process .csv files into a GerVADER compatible .tsv format.

#### Modes

##### 2) Split SCARE dataset

Convers files from the folder klinger-reviews/ into a .tsv format. .tsv files that already exist are skipped. Can crash on some files, therefore only a certain amonut of lines are interated. Then you have to reexecute until all files are created.

##### 3) Build 10% of SB10k corpus including neutral tweets (tweets.tsv)

Takes a random amount of 10% of the SB10k corpus including neutral tweets and generating a new .tsv.

##### 4) Build 10% of SB10k corpus without neutral tweets (tweets.tsv)

Just like 3) but neutral tweets are skipped.

### vaderSentimentGER

vaderSentimentGER is the actual VADER script transformed into a German adaptation. Moreover some utility functions have been added in order to allow for an easier classification of corpora.

## Corpora

In the paper multiple corpora are mentioned and used for the benchmark.

### SB10k

SB10k is a German twitter corpus used for evaluating GerVADER (more details check the paper). Because of legal reasons, the tweets can not be published with GerVADER.

For the tweet ids used in the benchmark, please email me or come back later to the repository.

Cite SB10k as follows:

>Cieliebak, Mark and Deriu, Jan and Egger, Dominic and Uzdilli, Fatih: A Twitter
Corpus and Benchmark Resources for German Sentiment Analysis. Social NLP @
EACL. https://doi.org/10.18653/v1/W17-1106

### SCARE

SCARE is a corpus containing app reviews for different app categories (more details check the paper). It is used for evaluating GerVADERs performance.

Which categories were used for the benchmark can be read in the paper. For legal reasons the SCARE corpus can not be published in the repository.

For more information on SCARE and the corpus please check the following resources:

>Mario Sänger, Ulf Leser, Steffen Kemmerer, Peter Adolphs, and Roman Klinger. SCARE -- The Sentiment Corpus of App Reviews with Fine-grained Annotations in German. In Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16), Portorož, Slovenia, May 2016. European Language Resources Association (ELRA)

[Link to SCARE corpus](http://www.romanklinger.de/scare/)

## Results

As can be seen from the papers results, GerVADER underperforms compared to VADER. I suggest to only use GerVADER for benchmarking and not for real business applications.
The *GERVaderLexicon_noexpansion.txt* is however useful for a crowd-rated source of german sentiment words. For usage, please read the *Lexicon* chapter above.
