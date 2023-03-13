from django.shortcuts import render
from .models import Transaction
from django.shortcuts import redirect
# Create your views here.

def index(request):
    transactions = Transaction.objects.all()
    return render(request, 'index.html', {'transactions': transactions})

def tform(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        mode = request.POST.get('mode')
        t = Transaction.objects.create(date=date, description=description, amount=amount, mode=mode)
        t.save()
        return redirect('index')
    return render(request, 'tform.html')