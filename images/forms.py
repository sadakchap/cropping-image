from PIL import Image
from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    image   = forms.ImageField(label='File',widget=forms.FileInput(attrs={'id':'photo'}))
    x       = forms.FloatField(widget=forms.HiddenInput(attrs={'id':'x_Input'}))
    y       = forms.FloatField(widget=forms.HiddenInput(attrs={'id':'y_Input'}))
    width   = forms.FloatField(widget=forms.HiddenInput(attrs={'id':'width_Input'}))
    height  = forms.FloatField(widget=forms.HiddenInput(attrs={'id':'height_Input'}))

    class Meta:
        model = Photo
        fields = ('image', 'x', 'y', 'width', 'height',)

    def save(self, commit=True):
        photo = super(PhotoForm, self).save(commit=False)
        
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        image = Image.open(photo.image)
        cropped_image = image.crop(x,y,w+x, h+y)
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        if commit:
            photo.save()
            resized_image.save(photo.image.path)
        return photo