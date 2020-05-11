import pickle

# open a file, where you stored the pickled data
file = open('classes.pkl', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

print('Showing the pickled data:')

cnt = 0
for item in data:
    print('The data ', cnt, ' is : ', item)
    cnt += 1

##Batch 2
# get_input = int(input("Please give the number of inputs: "))
# data=[]
#
# counter=0
# for i in range(get_input):
#     raw_data = input('enter data for '+str(i)+':')
#     counter +=1
#     data.append(raw_data)
#
#
# print(data)

##Batch 3
import nltk
from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# import pickle
# import numpy as np
#
# from keras.models import load_model
# model = load_model('chatbot_model.h5')
# import json
# import random
# intents = json.loads(open('intents.json').read())
# words = pickle.load(open('words.pkl','rb'))
# classes = pickle.load(open('classes.pkl','rb'))
# bag = [0]*len(words)
#
# print(model)
#
# def clean_up_sentence(sentence):
#     # tokenize the pattern - split words into array
#     sentence_words = nltk.word_tokenize(sentence)
#     # stem each word - create short form for word
#     sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
#     print(sentence_words)
#     return sentence_words
#
# print('\nThis is sentence:::::')
#
# def bow(sentence, words, show_details=True):
#     # tokenize the pattern
#     sentence_words = clean_up_sentence(sentence)
#     # bag of words - matrix of N words, vocabulary matrix
#     bag = [0]*len(words)
#     print('\nThis is bag:::::')
#     print(bag)
#     for s in sentence_words:
#         for i,w in enumerate(words):
#             if w == s:
#                 # assign 1 if current word is in the vocabulary position
#                 bag[i] = 1
#                 if show_details:
#                     print ("\nfound in bag: %s" % w)
#     print(np.array(bag))
#     return(np.array(bag))
#
# p=bow("Hello how are you doing today",words)
#
# res = model.predict(np.array([p]))[0]
# print(res)
#
# results = [[i,r] for i,r in enumerate(res) if r>0.25]
# # sort by strength of probability
# results.sort(key=lambda x: x[1], reverse=True)
# return_list = []
# for r in results:
#     return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
# print(return_list)