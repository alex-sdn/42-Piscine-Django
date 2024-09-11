from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            if tip.upvotes.filter(id=user.id).exists():
                tip.rm_upvote(request.user)
            else:
                if tip.downvotes.filter(id=user.id).exists():
                    tip.rm_downvote(request.user)

                tip.upvote(request.user)
            #Update reputation
            tip.author.profile.update_permissions()
    except:
        print('no tip found')

    return redirect('/')

@login_required()
def downvote_tip(request, id):
    user = request.user
    
    try:
        tip = Tip.objects.get(id=id)
        if tip:
            if tip.downvotes.filter(id=user.id).exists():
                tip.rm_downvote(request.user)
            else:
                if (tip.author == user) or user.profile.can_downvote:
                    if tip.upvotes.filter(id=user.id).exists():  #remove upvote anyway?
                        tip.rm_upvote(request.user)

                    tip.downvote(request.user)
                else:
                    print('no downvote permission')
                    messages.error(request, 'You do not have permissions for this')
            #Update reputation
            tip.author.profile.update_permissions()
    except:
        print('no tip found')

    return redirect('/')

@login_required()
def delete_tip(request, id):
    user = request.user

    try:
        tip = Tip.objects.get(id=id)
        if tip:
            if (tip.author == user) or user.has_perm('ex.delete_tip'):
                tip.delete()
            else:
                print('no delete permission')
                messages.error(request, 'You do not have permissions for this')
    except Exception as e:
        print(str(e))

    return redirect('/')