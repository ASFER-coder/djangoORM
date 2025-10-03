from django.db import models

class Talaba(models.Model):
    ismi = models.CharField(max_length=100)
    yoshi = models.IntegerField()
    kursi = models.IntegerField()
    guruhi = models.CharField(max_length=20)
    universiteti = models.CharField(max_length=150)

    def student(self):
        return f"{self.ismi} ({self.kursi}-kurs, {self.universiteti})" 