#LIAM CORLEY // 2020

from django.db import models

class Department(models.Model):
	dept_name = models.CharField(max_length=64, default="Null")

	def __str__(self):
		return self.dept_name;

	#Return all shows where department is this department instance
	def getShows(self):
		return Show.objects.filter(department=self)

#Show - the main project element of the portfolio
class Show(models.Model):
	#Show title
	title = models.CharField(max_length=64)
	#Show detail text - should be a short description
	detail_text = models.CharField(max_length=512)
	#The portfolio owner's role in the project, i.e. Lighting Designer, Scenic Designer
	#This ForeignKey field allows for shows to be filtered by department
	department = models.ForeignKey(Department, on_delete=models.CASCADE)

	#Show staff - all optional fields
	dir = models.CharField(max_length=128, blank=True)
	sm = models.CharField(max_length=128, blank=True)
	cd = models.CharField(max_length=128, blank=True)
	sd = models.CharField(max_length=128, blank=True)
	ld = models.CharField(max_length=128, blank=True)
	projd = models.CharField(max_length=128, blank=True)
	props = models.CharField(max_length=128, blank=True)
	photo = models.CharField(max_length=128, blank=True)

	#Order in which the show should appear in the landing page carousel
	#Must be unique
	sort_order = models.IntegerField(unique=True)
	#Image file for the image to appear on the landing carousel
	cover_image = models.ImageField(default="default.png")
	#Date created
	pub_date = models.DateTimeField('date published')

	#Return the title of the show
	def __str__(self):
		return self.title;
	#return a Queryset of images with this show instance as their show
	def getImages(self):
		return Image.objects.filter(show=self)


#Image to be shown on a show's detail page
class Image(models.Model):
	#Show this image belongs to
	show = models.ForeignKey(Show, on_delete=models.CASCADE)\
	#Image caption
	caption = models.CharField(max_length=200)
	#Image file
	image = models.ImageField(default="default.png")
	#Order to appear in detail page carousel
	sort_order = models.IntegerField()

	#Ensure that no two images of the same show may have the same sort_order
	class Meta:
		db_table = 'sort_order'
		constraints = [
			models.UniqueConstraint(fields=['show', 'sort_order'], name='unique sort_order')
		]

	#Return Show name: Caption
	def __str__(self):
		return str(self.show) + ": " + str(self.caption);
