from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

	class Meta:
		model = Product

		fields = [
			"title",
			"description",
			"image",
			"price",
			"quantity",
		]

class BuyForm(forms.ModelForm):
	class Meta:
		model = Product

		fields = [
			"quantity"
		]
		