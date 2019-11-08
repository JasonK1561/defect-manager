from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Defect(models.Model):
    ########## DEFECT STATUS ATTRIBUTES ###########
    DEFECT_STATUS_NEW = 'New'
    DEFECT_STATUS_OPEN = 'Open'
    DEFECT_STATUS_REJECTED = 'Rejected'
    DEFECT_STATUS_FIXED = 'Fixed'
    DEFECT_STATUS_CLOSE = 'Closed'

    DEFECT_STATUS_CHOICES = [
    (DEFECT_STATUS_NEW, 'New'),
    (DEFECT_STATUS_OPEN, 'Open'),
    (DEFECT_STATUS_REJECTED, 'Rejected'),
    (DEFECT_STATUS_FIXED, 'Fixed'),
    (DEFECT_STATUS_CLOSE, 'Closed'),
    ]

    ########## DEFECT TYPE ATTRIBUTES ###########
    DEFECT_TYPE_CONFIG = 'Configuration'
    DEFECT_TYPE_TESTERROR = 'Tester Error'
    DEFECT_TYPE_UI = 'User Interface'
    DEFECT_TYPE_OTHER = 'Other'

    DEFECT_TYPE_CHOICES = [
    (DEFECT_TYPE_CONFIG, 'Configuration'),
    (DEFECT_TYPE_TESTERROR, 'Tester Error'),
    (DEFECT_TYPE_UI, 'User Interface'),
    (DEFECT_TYPE_OTHER, 'OTHER'),
    ]

    ########## DEFECT SEVERITY ATTRIBUTES ###########
    DEFECT_SEVERITY_LOW = 'Low'
    DEFECT_SEVERITY_MEDIUM = 'Medium'
    DEFECT_SEVERITY_HIGH = 'High'

    DEFECT_SEVERITY_CHOICES = [
    (DEFECT_SEVERITY_LOW, 'Low'),
    (DEFECT_SEVERITY_MEDIUM, 'Medium'),
    (DEFECT_SEVERITY_HIGH, 'High'),
    ]
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    defect_status = models.CharField(max_length=10,
                                    choices=DEFECT_STATUS_CHOICES,
                                    default=DEFECT_STATUS_NEW,
                                    )
    defect_type = models.CharField(max_length=64,
                                    choices=DEFECT_TYPE_CHOICES,
                                    default=DEFECT_TYPE_CONFIG,
                                    )
    severity = models.CharField(max_length=8,
                                choices=DEFECT_SEVERITY_CHOICES,
                                default='',
                                )
    name = models.CharField(max_length=200, default='')
    created_date = models.DateTimeField(default=timezone.now)
    close_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField()
    modified_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("defect_manager_app:defect_detail", kwargs={'pk':self.pk})

    def modified(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

# class Comments
class Comment(models.Model):

    defect = models.ForeignKey('defect_manager_app.Defect', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text
