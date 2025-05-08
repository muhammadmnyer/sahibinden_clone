from .models import SubcategoriesChildParentRelation,Subcategory

def subcategories_json_builder(subcategory:Subcategory):
    return {
        "subcategory_id":subcategory.subcategory_id,
        "subcategory_name":subcategory.subcategory_name,
        "subcategories": [
            subcategories_json_builder(child_parent_relation.child) for child_parent_relation in SubcategoriesChildParentRelation.objects.filter(parent=subcategory)
        ]
    }
