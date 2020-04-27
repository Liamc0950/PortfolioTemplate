from django.db import models

class Department(models.Model):
	dept_name = models.CharField(max_length=64, default="Null")

	def __str__(self):
		return self.dept_name;

	#Return all shows where department is this department instance
	def getShows(self):
		return Show.objects.filter(department=self)


class Show(models.Model):
	title = models.CharField(max_length=64)
	detail_text = models.CharField(max_length=512)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)

	#Show staff
	dir = models.CharField(max_length=128, blank=True)
	sm = models.CharField(max_length=128, blank=True)
	cd = models.CharField(max_length=128, blank=True)
	sd = models.CharField(max_length=128, blank=True)
	ld = models.CharField(max_length=128, blank=True)
	projd = models.CharField(max_length=128, blank=True)
	props = models.CharField(max_length=128, blank=True)
	photo = models.CharField(max_length=128, blank=True)


	sort_order = models.IntegerField(unique=True)
	cover_image = models.ImageField(default="default.png")
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.title;
	def getImages(self):
		return Image.objects.filter(show=self)


class Image(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	caption = models.CharField(max_length=200)
	image = models.ImageField(default="default.png")
	sort_order = models.IntegerField()

	class Meta:
		db_table = 'sort_order'
		constraints = [
			models.UniqueConstraint(fields=['show', 'sort_order'], name='unique sort_order')
		]


	def __str__(self):
		return str(self.show) + ": " + str(self.caption);
