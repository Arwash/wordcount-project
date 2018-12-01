from django.http import HttpResponse

from django.shortcuts import render

import operator

def homepage(request):
    return render(request, 'home.html', {'instrument':'Always Piano'})

def piano(request):
    return HttpResponse('Hello Piaist Arwa!')


""" The split() method identify the spaces in a text to identify the words in it.

To count the most occuring word in the text. First we loop through each item/word in the wordlist, them we make a dictionary of keys/value, where each word is a key and its value is its count number. Whenever a word occour again we increment the value of the word. Below is the process """

def count(request):
    
    fulltext= request.GET['fulltext']
    
    wordList = fulltext.split()
    
    wordDictionary = {}
    
    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1 
              
        else:
            wordDictionary[word] = 1
            
    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordList), 'sortedWords':sortedWords}) 

def about (request):
    return render (request, 'about.html')