from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Job(models.Model):

    METHOD_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('indeed', 'Indeed'),
        ('otta', 'Otta'),
        ('company_website', 'Company Website'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.TextField(blank=True)
    company = models.TextField(blank=True)
    date_applied = models.DateField()
    method = models.CharField(max_length=15, choices=METHOD_CHOICES)
    cover_letter = models.TextField(blank=True)
    referral = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    first = models.BooleanField(default=False)
    second = models.BooleanField(default=False)
    third = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])