from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index_view(request):
    return render(request, 'dictionary/index.html')

def word_view(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    context ={
        'meaning':meaning['Noun'][0],
        'synonyms':synonyms,
        'antonyms':antonyms,
    }
    return render(request, 'dictionary/word.html', context)