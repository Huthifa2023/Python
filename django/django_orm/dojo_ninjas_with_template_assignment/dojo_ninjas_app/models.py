from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255, null=True)
#   ninjas = all ninjas related to this dojo (imagin based on related_name)


class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE) #CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


