from .models import SubcategoriesChildParentRelation,Subcategories

def subcategories_json_builder(subcategory:Subcategories):
    return {
        "subcategory_id":subcategory.subcategory_id,
        "subcategory_name":subcategory.subcategory_name,
        "subcategories": [
            subcategories_json_builder(child_parent_relation.child) for child_parent_relation in SubcategoriesChildParentRelation.objects.filter(parent=subcategory)
        ]
    }
