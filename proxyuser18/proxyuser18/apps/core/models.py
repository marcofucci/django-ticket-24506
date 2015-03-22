from django.contrib.auth.models import User as OriginalUser


class User(OriginalUser):
    class Meta:
        proxy = True
