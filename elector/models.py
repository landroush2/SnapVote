from django.db import models
import uuid

# Create your models here.
class Elector(models.Model):

    SEXE_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    elector_id = models.CharField(max_length=255,null=True,unique=True,editable=False)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    front_picture = models.ImageField(upload_to='elector/front_picture/')
    left_side_picture = models.ImageField(upload_to='elector/left_side_picture/')
    right_side_picture = models.ImageField(upload_to='elector/right_side_picture/')
    sexe = models.CharField(max_length=255,choices=SEXE_CHOICES, null=True)
    date_of_issuance = models.DateField(auto_now_add=True)
    date_of_expire = models.DateField(null=True)
    has_vote = models.BooleanField(default=False,null=True)
    candidate_id = models.PositiveIntegerField(null=True,default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs) :
        if not self.pk :
            self.elector_id = str(uuid.uuid4())[0:10]
        super(Elector, self).save(*args, **kwargs)