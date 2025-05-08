from django.db import models 

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return f"{self.category_name}"
    

class Subcategories(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=50,unique=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.subcategory_name}"
    

class SubcategoriesChildParentRelation(models.Model):
    parent = models.ForeignKey(Subcategories,on_delete=models.CASCADE,related_name='parent_relations' )
    child = models.ForeignKey(Subcategories,on_delete=models.CASCADE,related_name="child_relations")

    def __str__(self):
        return f"{self.parent}__{self.child}"
    


class Products(models.Model):
    product_id =  models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=100,null=False,unique=True)
    product_description = models.TextField(null=False)
    product_price = models.IntegerField(null=False)
    product_external_info = models.JSONField(null=True,blank=True)
    image = models.ImageField(upload_to="images/")
    path = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.product_name}"

    def toJson(self):
        return {
            "product_id":self.product_id,
            "product_name":self.product_name,
            "product_description":self.product_description,
            "product_price":self.product_price,
            "product_external_info":self.product_external_info,
            #"image":self.image
        }
