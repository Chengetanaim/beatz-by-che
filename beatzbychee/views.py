from django.shortcuts import render, redirect
from .forms import MessageTopicForm

# Create your views here.


def index(request):
    return render(request, 'beatzbychee/index.html')


def new_message_topic(request):
    if request.method != 'POST':
        form = MessageTopicForm()
    else:
        form = MessageTopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('beatzbychee:index')

    context = {'form': form}
    return render(request, 'beatzbychee/new_message_topic.html', context)


def my_music(request):
    return render(request, 'beatzbychee/my_music.html')


def privacy_policy(request):
    return render(request, 'beatzbychee/privacy_policy.html')


def accessibility(request):
    return render(request, 'beatzbychee/accessibility.html')

