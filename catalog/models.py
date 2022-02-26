from django.db import models

# for our categories and associated products

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(
        max_length=50,
        unique=True,
        help_text='unique value for product page URL'

    )
    description=models.TextField()
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='categories'
        ordering=['created_at']
        verbose_name_plural='Categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return 'catalog_category/'+self.slug

class Product(models.Model):
    name=models.CharField(max_length=255, unique=True)
    slug=models.SlugField(
        max_length=255,
        unique=True,
        help_text='unique value for product page URL'
         )
    brand=models.CharField(max_length=50)
    sku=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    old_price=models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=0.00)
    is_active=models.BooleanField(default=True)
    quantity=models.PositiveIntegerField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    categories=models.ManyToManyField(Category)
    image=models.ImageField(upload_to='products/%Y/%m/%d')
    thumbnail=models.ImageField(upload_to='products/thumbnails/%Y/%m/%d', blank=True)

    class Meta:
        db_table='products'
        ordering=['created_at']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return 'catalog_category/'+self.slug

    def sale_price(self):
        if self.price < self.old_price:
            return self.price
        else:
            return None