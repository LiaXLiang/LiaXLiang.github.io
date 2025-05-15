from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from .models import ChatHistory
from .conversational_version2 import run_query
from .forms import ChatForm
import markdown

# Functionality for retrieving the query and giving responses mostly done here in this file :D

def home(request):
    chat_history = ChatHistory.objects.all().order_by('-timestamp')
    return render(request, 'home.html', {'chat_history': chat_history})

def process_query(request):
    if request.method == 'POST':
        user_query = request.POST.get('query', '').strip()
        request.session['last_query'] = user_query
        return redirect('chat_view')
    else:
        return render(request, 'home.html')

def chat_view(request):
    last_query = request.session.get('last_query', 'No query found')
    raw_response = run_query(last_query)
    formatted_response = format_response(raw_response)
    request.session['last_response'] = formatted_response

    ChatHistory.objects.create(query=last_query, response=formatted_response, timestamp=timezone.now())
    chat_history = ChatHistory.objects.all().order_by('-timestamp')


    return render(request, 'chat_view.html', {'last_query': last_query, 'last_response': formatted_response, 'chat_history': chat_history})

def format_response(raw_response):
    formatted_response = markdown.markdown(raw_response)
    return formatted_response

def clear_chat_history(request):
    ChatHistory.objects.all().delete()
    return redirect('chat_view')

