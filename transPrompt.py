from googletrans import Translator

translator = Translator()

def transPrompt():
    text = input('Please enter your translation prompt: ')
    print('You entered: ', text)
    text = translator.translate(text, dest='ja').text
    text = translator.translate(text, dest='pl').text
    text = translator.translate(text, dest='zh-cn').text
    text = translator.translate(text, dest='yi').text
    text = translator.translate(text, dest='hi').text
    text = translator.translate(text, dest='en').text
    print('Output: ', text)