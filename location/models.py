from django.db import models


class LocationTag(models.Model):
    name = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    # To implement hierarchy of location, a house is a child of a town who is a child of a region
    parent_location = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="child_locations"
    )
    tags = models.ManyToManyField(LocationTag, related_name='locations', blank=True)
    # Short description, surface knowledge of the location (for players)
    description_short = models.TextField(blank=True)
    # Long description, text to read to the players when they first discover the location
    description_long = models.TextField(blank=True)
    # 2 - 5 words to help remember the most important features of the location (If no memorable features, add one)
    description_keywords = models.TextField(blank=True)
    # 2 - 5 words to help categorize the location based on senses (other than sight)
    description_senses = models.TextField(blank=True)
    lore = models.TextField(blank=True)
    image_link = models.ImageField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
