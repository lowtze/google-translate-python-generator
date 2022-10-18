import os
import csv
from googletrans import Translator

translator = Translator()
csvName = 'input.csv'

def csvTrans():
    text = line[0]
    #print(text)
    text = translator.translate(text, dest='ja').text
    text = translator.translate(text, dest='la').text
    text = translator.translate(text, dest='zh-cn').text
    text = translator.translate(text, dest='yi').text
    text = translator.translate(text, dest='gd').text
    text = translator.translate(text, dest='hi').text
    text = translator.translate(text, dest='en').text
    #print(text)
    outputList = [line[0], text] # make them a list otherwise writerow will be unhappy
    writer.writerow(outputList) # this takes one argument, so to add multiple items, turn them into a list as above
    

with open(csvName) as f:
    with open('output.csv', 'w', newline='') as o:
        lines = csv.reader(f)
        writer = csv.writer(o)
        writer.writerow(['Input', 'Output']) # set up initial column labels
        for line in lines:
            excelTest()
        print('Done')