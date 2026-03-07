from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=30)
    level = models.CharField(max_length=3)
    category = models.CharField(max_length=50, default='Backend')
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Category(models.Model):
    engname = models.CharField(max_length=25)
    rusname = models.CharField(max_length=25)

    class Meta:
        ordering = ['id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.rusname

class Work(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='works')
    image = models.ImageField(upload_to='works', blank=True)
    summary = models.CharField(max_length=220, blank=True)
    description = models.TextField()
    stack = models.TextField()
    features = models.TextField(blank=True)
    results = models.TextField(blank=True)
    link = models.URLField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', '-id']
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']
        verbose_name = 'Сервис'
        verbose_name_plural = 'Виды сервиса'

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=150)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'

    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    title = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    telegram = models.URLField(blank=True)
    github = models.URLField(blank=True)
    about = models.TextField()
    skills = models.ManyToManyField(Skill, related_name='author')
    image = models.ImageField(upload_to='author', blank=True)
    focus_areas = models.TextField(blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'Сообщение от {self.name}: {self.subject}'

class Testimony(models.Model):
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    image = models.ImageField(upload_to='clients')
    text = models.TextField()

    class Meta:
        ordering = ['-id']
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return f'{self.name} {self.lastname}'