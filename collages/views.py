from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Collage, ImageItem
from .forms import CollageCreateForm, ImageItemFormSet
import json


def home(request):
    if request.user.is_authenticated:
        recent_collages = Collage.objects.filter(user=request.user)[:3]
    else:
        recent_collages = []
    
    return render(request, 'collages/home.html', {
        'recent_collages': recent_collages,
    })


@login_required
def collage_list(request):
    collages = Collage.objects.filter(user=request.user)
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        collages = collages.filter(
            Q(title__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(collages, 12)  # Show 12 collages per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'collages/list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
    })


@login_required
def collage_create(request):
    if request.method == 'POST':
        form = CollageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            collage = form.save(commit=False)
            collage.user = request.user
            
            # Get template and frame style from POST data
            template_id = request.POST.get('template_id', 'template_2_1')
            frame_style = request.POST.get('frame_style', 'modern')
            
            collage.template_id = template_id
            collage.frame_style = frame_style
            collage.save()
            
            # Handle multiple image uploads
            images = request.FILES.getlist('images')
            for i, image in enumerate(images):
                ImageItem.objects.create(
                    collage=collage,
                    image=image,
                    order=i + 1
                )
            
            messages.success(request, f'Collage "{collage.title}" created successfully!')
            return redirect('collages:detail', pk=collage.pk)
    else:
        form = CollageCreateForm()
    
    return render(request, 'collages/create.html', {
        'form': form,
    })


@login_required
def collage_detail(request, pk):
    collage = get_object_or_404(Collage, pk=pk, user=request.user)
    images = collage.images.all()
    
    return render(request, 'collages/detail.html', {
        'collage': collage,
        'images': images,
    })



@login_required
def collage_delete(request, pk):
    collage = get_object_or_404(Collage, pk=pk, user=request.user)
    
    if request.method == 'POST':
        collage_title = collage.title
        collage.delete()
        messages.success(request, f'Collage "{collage_title}" deleted successfully!')
        return redirect('collages:list')
    
    return render(request, 'collages/delete.html', {
        'collage': collage,
    })



