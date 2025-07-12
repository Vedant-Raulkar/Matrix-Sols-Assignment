from django import forms
from django.forms import inlineformset_factory
from .models import Collage, ImageItem


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class CollageForm(forms.ModelForm):
    class Meta:
        model = Collage
        fields = ['title', 'template_id', 'frame_style']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter collage title',
            }),
            'template_id': forms.Select(attrs={
                'class': 'form-select',
            }),
            'frame_style': forms.Select(attrs={
                'class': 'form-select',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True


class ImageUploadForm(forms.Form):
    images = MultipleFileField(
        widget=MultipleFileInput(attrs={
            'multiple': True,
            'accept': 'image/*',
            'class': 'form-control',
        }),
        help_text='Select up to 10 images',
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].required = True


class CollageCreateForm(forms.ModelForm):
    images = MultipleFileField(
        widget=MultipleFileInput(attrs={
            'multiple': True,
            'accept': 'image/*',
            'class': 'form-control',
            'id': 'images-input',
        }),
        help_text='Select up to 10 images',
        required=True
    )

    class Meta:
        model = Collage
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter collage title',
                'required': True,
            }),
        }

    def clean_images(self):
        images = self.files.getlist('images')
        if len(images) > 10:
            raise forms.ValidationError('You can upload a maximum of 10 images.')
        if len(images) < 1:
            raise forms.ValidationError('Please select at least one image.')
        
        allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
        for image in images:
            if image.content_type not in allowed_types:
                raise forms.ValidationError(f'Invalid file type: {image.name}. Only JPEG, PNG, GIF, and WebP files are allowed.')
        
        return images


class ImageItemForm(forms.ModelForm):
    class Meta:
        model = ImageItem
        fields = ['caption', 'x_position', 'y_position', 'width', 'height']
        widgets = {
            'caption': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Image caption (optional)',
            }),
            'x_position': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
            }),
            'y_position': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
            }),
            'width': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
            }),
            'height': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
            }),
        }

ImageItemFormSet = inlineformset_factory(
    Collage, 
    ImageItem, 
    form=ImageItemForm,
    extra=0,
    can_delete=True
)
