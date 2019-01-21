from django import forms
from accounts.models import Accountuser
from accounts.forms import EditForm
from products.models import Category


class ShopUserAdminEditForm(EditForm):
    class Meta:
        model = Accountuser
        fields = '__all__'


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-contol'
            field.help_text = ''