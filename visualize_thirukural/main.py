import json
import os
import wordcloud
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as py

def read_corpus(file_name):
    with open(file_name, "r") as file_object:
        json_object = json.loads(file_object.read())
    chapters = json_object['chapters']
    corpus=""
    for text in chapters:
        corpus +="".join(text)
    wc = wordcloud.WordCloud().generate(corpus)
    py.imshow(wc.recolor())
    py.show()


if __name__ == '__main__':
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    read_corpus(BASE_DIR + "/resources/data.json")
