from django.db import models

class Course(models.Model):
    nome = models.CharField('Nome', max_length=200)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    star_date = models.DateField('Data início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem')

    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
