from django.db import models

# Create your models here.
class Blog(models.Model):
#title
    title = models.CharField(max_length=255)
#pub_date
    pub_date = models.DateTimeField()
#body
    body = models.TextField()
#image
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y') 

#Add the blog app to the settings

#create a migration

# Migrate

#Add to the Main
