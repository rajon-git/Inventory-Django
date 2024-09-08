from django.shortcuts import render,redirect
from .forms import CreateUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('user-register')
    else:
        form = CreateUserForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)