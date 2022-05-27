from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm


# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        form = UserRegistration()

    return render(request, 'account/register.html', {'form': form})


@login_required
def edit(request):
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
        else:
            form = UserEditForm(instance=request.user)
        context = {
            'form': form,
        }

        return render(request, 'account/edit.html')


def checkUserState(request):
    if request.user.is_authenticated:
        return render(request, 'account/dashboard.html', {'section': 'dashboard'})
    else:
        return render(request, 'account/base.html')
