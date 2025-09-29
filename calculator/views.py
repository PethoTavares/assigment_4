from django.shortcuts import render
from .forms import InputForm
import math

def calculate_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            if a < 1:
                error = "Value A is too small."
            elif c < 0:
                error = "Value C cannot be negative."
            else:
                c_cubed = c ** 3
                if c_cubed > 1000:
                    calc = math.sqrt(c_cubed) * 10
                else:
                    calc = math.sqrt(c_cubed) / a
                result = calc + b
        else:
            error = "Please enter valid numeric values."
    else:
        form = InputForm()

    return render(request, 'calculator/result.html', {
        'form': form,
        'result': result,
        'error': error
    })
