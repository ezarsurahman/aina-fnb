from django.forms import ModelForm
from main.models import FoodEntry
from django.utils.html import strip_tags

class FoodEntryForm(ModelForm):
    class Meta:
        model = FoodEntry
        fields = ["img", "name", "price", "ready", "description"]
    def clean_img(self):
        img = self.cleaned_data["img"]
        return strip_tags(img)

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_ready(self):
        ready = self.cleaned_data["ready"]
        return strip_tags(ready)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)