from django.db import models

# Create your models here.

class Tennant(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True, verbose_name ='Person ID')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    rent_start = models.DateField()
    rent_end = models.DateField()
    appartment = models.ForeignKey('Apartments', null=True, blank=True, on_delete=models.SET_NULL)


    # These were causing problems with the POST information during INTEX, but can be used when displaying data
    #def __str__(self):
    #    phone = '(%s) %s-%s' %(self.phone[0:3],self.phone[3:6],self.phone[6:10])
    #    return phone  
    # def __str__(self):
    #    return (self.first_name)

    class Meta:
        db_table = 'Tennant'


class Admin(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True, verbose_name ='Tennant ID')
    admin = models.IntegerField()
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    person = models.OneToOneField(Tennant, models.CASCADE)

    def __str__(self):
        return (self.admin_id) 

    class Meta:
        db_table = 'Admin'


class Apartments(models.Model):
    house = models.CharField(max_length=50)
    rent = models.IntegerField()

    class Meta:
        db_table = 'Apartments'

