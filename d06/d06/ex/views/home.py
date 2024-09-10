from django.shortcuts import render

def home(request):
    context = {
        'username': request.session.get('username')
    }
    return render(request, 'ex/home.html', context) 