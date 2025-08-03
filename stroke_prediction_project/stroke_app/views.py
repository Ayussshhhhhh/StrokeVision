from django.shortcuts import render
from .forms import StrokePredictionForm
from .ml_utils import make_prediction
import pandas as pd

def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'POST':
        form = StrokePredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_data = pd.DataFrame([data])
            prediction, probability = make_prediction(input_data)
            return render(request, 'predict.html', {
                'form': form,
                'prediction': 'Stroke' if prediction == 1 else 'No Stroke',
                'probability': probability * 100  # Convert to percentage
            })
    else:
        form = StrokePredictionForm()
    return render(request, 'predict.html', {'form': form})