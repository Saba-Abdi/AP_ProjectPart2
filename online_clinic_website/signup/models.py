from django.db import models
from django.core import validators


class User(models.Model):
    name = models.CharField(max_length=25,  validators=[validators.MinLengthValidator(4), validators.RegexValidator(r'^.*[a-zA-Z].*[\w]*$')])
    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            validators.MinLengthValidator(5),
            validators.RegexValidator(r'^.*[a-zA-Z].*[\w]*$')
        ]
    )
    password = models.CharField(
        max_length=50,
        validators=[
            validators.MinLengthValidator(8),
            validators.RegexValidator(r'^\S*$')]
    )
    email = models.EmailField()
    positions = [('secretary', 'secretary'), ('patient', 'patient')]
    position = models.CharField(max_length=16, choices=positions, default='patient')

    # This function returns a string representation of the user object
    def __str__(self):
        return self.username + ' ' + self.password
