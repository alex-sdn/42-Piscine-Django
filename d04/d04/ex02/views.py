from django.shortcuts import render
from django import forms
from django.conf import settings
from django.utils import timezone

class InputForm(forms.Form):
    Input = forms.CharField(label="Input")

def form(request):
    log_file = settings.EX02_LOGS_PATH
    form = InputForm()

    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():
            input_data = form.cleaned_data['Input']
            current_time = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
            
            # write input to logs file
            with open(log_file, 'a') as file:
                file.write(f'{current_time} - {input_data}\n')
    
    # open logs file
    try:
        with open(log_file, 'r') as file:
            logs = file.readlines()
    except:
        logs = []

    context = {'form': form,
               'logs': logs}
    return render(request, 'ex02/form.html', context)
