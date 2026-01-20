from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='static/images/')
    image_url = models.URLField(blank=True, help_text="URL of the image if hosted externally")
    link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('FRONTEND', 'Frontend'),
        ('BACKEND', 'Backend'),
        ('TOOLS', 'Tools'),
        ('OTHER', 'Other'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    proficiency = models.IntegerField(default=50, help_text="0-100")

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=100, default='Chennai, Tamil Nadu, India')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default='Completed')
    certificate_id = models.CharField(max_length=100, blank=True)
    date = models.DateField(null=True, blank=True)
    skills = models.TextField(help_text="Comma separated skills")
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    event = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.event}"

