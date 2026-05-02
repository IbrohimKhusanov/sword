from django.db import models



class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



class ContactType(models.TextChoices):
    TELEGRAM = 'telegram', 'Telegram'
    GMAIL = 'gmail', 'Gmail'
    PHONE = 'phone', 'Phone'
    INSTAGRAM = 'instagram', 'Instagram'
    WHATSAPP = 'whatsapp', 'WhatsApp'



class ContactLink(models.Model):
    service = models.ForeignKey(Services, related_name='contacts', on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=20, choices=ContactType.choices)
    value = models.CharField(max_length=200)  # @username yoki email yoki telefon

    def __str__(self):
        return f"{self.contact_type}: {self.value}"