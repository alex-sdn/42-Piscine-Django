from django.shortcuts import render

pages = [
    {'name':'django', 'title':'Ex01 : Django, framework web'},
    {'name':'affichage', 'title':'Ex01 : Processus d’affichage d’une page statique'},
    {'name':'templates', 'title':'Ex01 : Moteur de template'}
]

def django(request):
    context = {'pages': pages,
               'current': pages[0]}

    return render(request, 'ex01/django.html', context)

def affichage(request):
    context = {'pages': pages,
               'current': pages[1]}

    return render(request, 'ex01/affichage.html', context)

def templates(request):
    context = {'pages': pages,
               'current': pages[2]}

    return render(request, 'ex01/templates.html', context)

# def base(request, pk):

#     page = None
#     for i in pages:
#         # print(pk)
#         # print(i['name'])
#         if i['name'] == pk:
#             page = i

#     context = {'pages':pages,'current': page}
#     return render(request, 'ex01/base.html', context)
