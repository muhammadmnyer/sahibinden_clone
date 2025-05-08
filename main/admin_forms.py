from django import forms
from .models import Product,Category,Subcategory,SubcategoriesChildParentRelation

class TestingDynamicForm(forms.Form):
    

    def __init__(self, path:list,*args, **kwargs):
        
        super().__init__(*args, **kwargs)



        self.fields['path'] = forms.CharField(widget=forms.HiddenInput(), initial=','.join(map(str, path)))

        if(len(path) == 0):
            self.fields['field'] = forms.ModelChoiceField(
                queryset=Category.objects.all(),
                label="Category: ",
                empty_label="select an option",
                widget=forms.Select(attrs={
                    'onchange': 'this.form.submit()',
                    'class': 'auto-submit'  
        })
            )

        elif (len(path) == 1):
             self.fields['field'] = forms.ModelChoiceField(
                queryset=Subcategory.objects.filter(category=Category.objects.get(category_id=path[0])),
                label=f"{Category.objects.get(category_id=path[0])}'s subcategory: ",
                empty_label="select an option",
                widget=forms.Select(attrs={
                        'onchange': 'this.form.submit()', 
                        'class': 'auto-submit'  
                    })
            )

        else:
            parent_id = path[-1]
            child_ids = SubcategoriesChildParentRelation.objects.filter(parent_id=parent_id).values_list('child', flat=True)
            if(len(child_ids)>0):
                self.fields['field'] = forms.ModelChoiceField(
                    queryset=Subcategory.objects.filter(subcategory_id__in=child_ids),
                    label=f"{Subcategory.objects.get(subcategory_id=parent_id)}'s subcategory: ",
                    empty_label="select an option",
                    widget=forms.Select(attrs={
                        'onchange': 'this.form.submit()',
                        'class': 'auto-submit'
                    })
                ) 
            else:
                self.fields['info'] = forms.CharField(
                    required=False,
                    label='',
                    initial=f'Done.\n final path: {path}',
                    widget=forms.TextInput(attrs={
                        'readonly': 'readonly',
                        'style': 'border:none; background:transparent; font-weight:bold;'
                    })
                )

        


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'path': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        path = self.data.get('path', '')
        path_list = list(map(int, path.split(','))) if path else []

        pathfield = forms.CharField(
            widget=forms.HiddenInput(),
            initial = ','.join(map(str, path_list))
        )

        # Add dynamic dropdown
        if len(path_list) == 0:
            category_select = forms.ModelChoiceField(
                queryset=Category.objects.all(),
                label="Category",
                widget=forms.Select(attrs={'onchange': 'this.form.submit();'})
            )
        elif len(path_list) == 1:
            category_select = forms.ModelChoiceField(
                queryset=Subcategory.objects.filter(category_id=path_list[0]),
                label="Subcategory",
                widget=forms.Select(attrs={'onchange': 'this.form.submit();'})
            )
        else:
            parent_id = path_list[-1]
            children = SubcategoriesChildParentRelation.objects.filter(parent_id=parent_id).values_list('child', flat=True)
            if children:
                category_select = forms.ModelChoiceField(
                    queryset=Subcategory.objects.filter(subcategory_id__in=children),
                    label="subcategory",
                    widget=forms.Select(attrs={'onchange': 'this.form.submit();'})
                )

