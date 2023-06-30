from django.shortcuts import render
from django.http import HttpResponse
import collections.abc
collections.Hashable = collections.abc.Hashable
# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chat')

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

chatterbotCorpusTrainer.train("chatterbot.corpus.english")

def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse("This is the specific url")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
