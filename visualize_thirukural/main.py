import json
import os
import wordcloud
import matplotlib.pyplot as py
import sys


def read_corpus(file_name):
	with open(file_name,"r") as file_object:
		json_object = json.loads(file_object.read())
		for value in json_object:
			chapters = json_object['chapters']
	print type(chapters)
	corpus=""
	for text in chapters:
		corpus +="".join(text)
	print corpus
	sample="Hello Boss"
	wc = wordcloud.WordCloud(font_path="/home/selva/Downloads/TAMUni-Tamil195.ttf",scale=500).generate(corpus)
	py.imshow(wc.recolor())
	py.show()


if __name__ == '__main__':
	BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
	read_corpus(BASE_DIR + "/resources/data.json")
