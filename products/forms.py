from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Name', 
                                    widget = forms.Textarea( 
                                        attrs = {
                                            "placeholder" : "Your Title",
                                            'rows'        : 1,
                                            'cols'        : 50
                                        }
                                ))
    desc  = forms.CharField(required=False, widget = forms.Textarea(
                                                            attrs={
                                                                'placeholder' : "Your Discription",
                                                                'class'       : "new-class two",
                                                                'id'          : "new-id",  
                                                                'cols'        : 50,
                                                                'rows'        : 15
                                                            }
                                                        ))
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'desc',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "Mitu" in title:
            raise forms.ValidationError("Not a valid name!")
        else:
            return title



class RawProductForm(forms.Form):
    title = forms.CharField(label='Name', 
                                    widget = forms.Textarea( 
                                        attrs = {
                                            "placeholder" : "Your Title",
                                            'rows'        : 1
                                        }
                                ))
    desc  = forms.CharField(required=False, widget = forms.Textarea(
                                                            attrs={
                                                                'placeholder' : "Your Discription",
                                                                'class'       : "new-class two",
                                                                'id'          : "new-id",  
                                                                'cols'        : 50,
                                                                'rows'        : 15
                                                            }
                                                        ))
    price = forms.DecimalField(initial=199.99)
