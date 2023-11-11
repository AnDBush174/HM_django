from django.shortcuts import render, redirect
from .forms import FeedbackForm


def home_view(request):
    return render(request, 'catalog/contact.html')


def contact_view(request):
    return render(request, 'contact.html')


def contacts(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # перенаправляем пользователя на страницу успешной отправки данных
    else:
        form = FeedbackForm()

    return render(request, 'contacts.html', {'form': form})
