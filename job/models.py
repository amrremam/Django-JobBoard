from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


class job(models.Model):
    title = models.CharField(max_length=80)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=300)
    published_at = models.DateField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name