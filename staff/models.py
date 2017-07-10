from django.db import models
from django.core.validators import RegexValidator


class ContactUsModel(models.Model):
    """
    The class defines a model to store the data received from `contact us`
    form on the website.
    """
    phone_regex = RegexValidator(regex=r'^\+?\d{8,15}')

    name = models.CharField(max_length=254, null=False)
    email = models.EmailField()
    phone_number = models.CharField(
        validators=[phone_regex, ],
        blank=True,
        max_length=16
    )
    text = models.TextField()

    def __str__(self):
        return '<Contact Us: {} says {}>'.format(
            self.name, self.text[:20] + ('...' if len(self.text) > 20 else ''))


