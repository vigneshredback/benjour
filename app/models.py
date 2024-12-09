from django.db import models

# Create your models here.

class Journal(models.Model):
    title = models.CharField(max_length=100)
    stylesheet_file = models.FileField(upload_to='uploads/stylesheet', blank=False, null=False)
    journal_template_file = models.FileField(upload_to='uploads/template', blank=False, null=False)
    author = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# class Issue(models.Model):
#     title = models.CharField(max_length=100)
#     journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

class Paper(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)
    pdf_file = models.FileField(upload_to='uploads/paper')
    word_file = models.FileField(upload_to='uploads/template', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title