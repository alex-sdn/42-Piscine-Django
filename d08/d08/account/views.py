from django.shortcuts import render
# from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
# from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm

from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token


def loginview(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                'success': True,
                'username': username
            })
        else:
            return JsonResponse({
                'success': False,
                'error': 'Invalid credentials'
            })

        # form = AuthenticationForm(request.POST)

        # if form.is_valid():
        #     user = form.get_user()
        #     login(request, user)
        #     return JsonResponse({
        #         'success': True,
        #         'username': form.cleaned_data['username']
        #     })
        # else:
        #     print(form.data)
        #     return JsonResponse({
        #         'success': False,
        #         'error': 'Invalid credentials'
        #     })

    return render(request, 'account/account.html', {'form': AuthenticationForm})


@csrf_exempt  #tmp
def logoutview(request):
    logout(request)
    return JsonResponse({
        'success': True,
    })


def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})
