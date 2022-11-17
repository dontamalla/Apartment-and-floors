from djago.db import models

class Apartments(models.Model):
    facility_name = models.CharField(max_length=255)
    id = models.IntegerFeild()
    facility_type =models.CharField(max_length=255)
    company = models.CharField(max_length=255)

    class Meta:
        db_table = "apartment_table";

Class Floors(models.Model):
    floor_name = models.CharField(max_length=255)
    floor_number = models.IntegerField()
    id = models.IntegerField()
    facility_id = models.IntegerFeild()
    active = models.BoolienField()


    class Meta:
        db_table = "floor_table";