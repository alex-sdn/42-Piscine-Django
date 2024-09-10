from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.decorators import login_required
from ex.models import Tip

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['content']


def home(request):
    form = TipForm()
    tips = Tip.objects.all()

    context = {
        'form': form,
        'tips': tips,
        'username': request.session.get('username')
    }
    return render(request, 'ex/home.html', context) 

@login_required()
def add_tip(request):
    if request.method == 'POST':
        form = TipForm(request.POST)

        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()

    return redirect('/')

@login_required()
def upvote_tip(request, id):
    user = request.user
    try:
        tip = Tip.objects.get(id=id)

        if tip:
            # test = Tip.objects.filter(author=request.user)
            # if tip in test:
            #     print('oui c dedans')

            if tip.upvotes.filter(id=user.id).exists():
                tip.upvotes.remove(request.user)
            else:
                if tip.downvotes.filter(id=user.id).exists():
                    tip.downvotes.remove(request.user)

                tip.upvotes.add(request.user)
    except:
        print('no tip')

    return redirect('/')

@login_required()
def downvote_tip(request, id):
    user = request.user
    
    try:
        tip = Tip.objects.get(id=id)
        if tip:
            if tip.downvotes.filter(id=user.id).exists():
                tip.downvotes.remove(request.user)
            else:
                if tip.upvotes.filter(id=user.id).exists():
                    tip.upvotes.remove(request.user)

                tip.downvotes.add(request.user)
    except:
        print('no tip')

    return redirect('/')

@login_required()
def delete_tip(request, id):
    user = request.user
    tip = Tip.objects.get(id=id)

    if tip:
        tip.delete()

    return redirect('/')