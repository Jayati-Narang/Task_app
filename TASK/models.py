# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Sum, Avg, Func
class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 2)'



class Data(models.Model):
    invoice_id = models.CharField(db_column='Invoice ID', primary_key=True, max_length=225)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    branch = models.CharField(db_column='Branch', max_length=225)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=225)  # Field name made lowercase.
    customer_type = models.CharField(db_column='Customer type', max_length=225)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gender = models.CharField(db_column='Gender', max_length=225)  # Field name made lowercase.
    product_line = models.CharField(db_column='Product line', max_length=225)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unit_price = models.FloatField(db_column='Unit price')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    tax = models.FloatField(db_column='Tax')  # Field name made lowercase.
    total = models.FloatField(db_column='Total')  # Field name made lowercase.
    payment_mode = models.CharField(db_column='Payment Mode', max_length=225)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rating = models.FloatField(db_column='Rating')  # Field name made lowercase.

    def __str__(self):
        return self.invoice_id
    class Meta:
        managed = False
        db_table = 'Data'
        
    def get_top_5_rated(self):
        x = []
        objs = self.objects.raw(' SELECT * FROM( SELECT *, @rn := IF(@prev = city, @rn + 1, 1) AS rn, @prev := city FROM Data JOIN (SELECT @prev := NULL, @rn := 0) AS vars ORDER BY city, rating DESC) AS T1 WHERE rn <= 5;')
        for o in objs:
            x.append([o.product_line, o.city, o.rating])
        return x
    
    def get_total_payment_wise(self):
        objs = self.objects.values('payment_mode').annotate(Total=Sum('total'))
        return objs
    
    def get_avg_rating_product_branch_wise(self):
        objs = self.objects.values('branch', 'product_line').annotate(Average=Round(Avg('rating'))).order_by('branch')
        return objs

    
    
         
        
        
            
    
