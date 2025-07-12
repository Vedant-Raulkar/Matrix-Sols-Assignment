from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('collages:home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to Collage Editor.')
            return redirect('collages:home')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {
        'form': form,
    })


@login_required
def profile(request):
    """User profile view"""
    from collages.models import Collage, ImageItem
    from django.utils import timezone
    from datetime import datetime
    
    # Get statistics
    total_collages = Collage.objects.filter(user=request.user).count()
    total_images = ImageItem.objects.filter(collage__user=request.user).count()
    
    # Get collages created this month
    current_month = timezone.now().replace(day=1)
    recent_collages = Collage.objects.filter(
        user=request.user,
        created_at__gte=current_month
    ).count()
    
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'total_collages': total_collages,
        'total_images': total_images,
        'recent_collages': recent_collages,
    })
