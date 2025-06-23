from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CompleteProfileForm

@login_required
def complete_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CompleteProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to home/dashboard
    else:
        form = CompleteProfileForm(instance=user)
    return render(request, 'accounts/complete_profile.html', {'form': form})

@login_required
def profile_check(request):
    user = request.user
    if not user.role or not user.department or not user.games:
        return redirect('complete_profile.html')
    return redirect('/')  


@login_required
def view_profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


