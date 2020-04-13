from django.db import models

class Show(models.Model):
	title = models.CharField(max_length=64)
	detail_text = models.CharField(max_length=512)
	department = models.CharField(max_length=64, default = "LIGHTING DESIGN")
	sort_order = models.IntegerField()
	cover_image = models.ImageField(default="default.png")
	pub_date = models.DateTimeField('date published')


class Image(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	caption = models.CharField(max_length=200)
	image_filename = models.CharField(max_length=256)
	sort_order = models.IntegerField()