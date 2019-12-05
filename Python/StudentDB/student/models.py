from django.db import models

# Create your models here.


class Major(models.Model):
    class Meta:
        verbose_name_plural = "Majors"
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    age = models.IntegerField()
    year = models.IntegerField()
    year_of_graduation = models.IntegerField()
    major = models.ForeignKey(Major, on_delete= models.SET_NULL, null=True)

    def __str__(self):
        return self.name
