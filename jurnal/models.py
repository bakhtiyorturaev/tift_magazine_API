from django.db import models
from bosh_sahifa.models import Magazine
from django_ckeditor_5.fields import CKEditor5Field

class AboutMagazine(models.Model):
    magazine = models.ForeignKey(to=Magazine, on_delete=models.CASCADE, verbose_name="Jurnal nomi")
    bio = CKEditor5Field(config_name='extends', verbose_name="Jurnal haqida")
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'Jurnal haqida'
        verbose_name_plural = 'Jurnal haqida'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.magazine.slug + '-haqida'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.magazine.name} - about'

class MagazineNews(models.Model):
    magazine = models.ForeignKey(to=Magazine, on_delete=models.CASCADE, verbose_name="Jurnal nomi")
    title = models.CharField(max_length=500, verbose_name="yangilik nomi")
    content = models.TextField(verbose_name="Yangilik haqida")
    image = models.ImageField(upload_to='jurnal/news', blank=True, null=True, verbose_name="rasm")
    link = models.URLField(blank=True, null=True, verbose_name="havola")

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Jurnal yangiliklari'

    def __str__(self):
        return f'{self.title} - {self.magazine.name}'

class MagazineRequirements(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Masalan: 'Jurnal nomi' elektron jurnalida maqola chop ettirish talablari",
                             verbose_name="jurnal talablari nomi")
    content = CKEditor5Field(config_name='extends', blank=True, null=True, verbose_name="Jurnal tablari to'liq")

    class Meta:
        verbose_name = 'Jurnal talablari'
        verbose_name_plural = 'Jurnal talablari'

    def __str__(self):
        return self.title

class MagazineArchive(models.Model):
    content = CKEditor5Field(config_name='extends', verbose_name="Arxiv")
    class Meta:
        verbose_name = 'Arxiv'
        verbose_name_plural = 'Jurnal arxivlari'

    def __str__(self):
        return 'Archive'

class MagazineStatistics(models.Model):
    title = models.CharField(max_length=200, verbose_name="Statistika nomi")
    content = CKEditor5Field(config_name='extends')

    class Meta:
        verbose_name = 'Statistika'
        verbose_name_plural = 'Jurnal statistikasi'

    def __str__(self):
        return self.title