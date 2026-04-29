from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


from django.conf import settings
import requests
from .models import Order
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .tasks import send_telegram_notification


User = get_user_model()


@receiver(post_save, sender=User)
def activate_user(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        instance.is_active = True
        instance.save(update_fields=['is_active']) # Mana shu xavfsizroq





@receiver(post_save, sender=Order)
def order_signal(sender, instance, created, **kwargs):
    if created:
        # transaction.on_commit hamma narsa bazaga yozilib bo'lganda ishlaydi
        transaction.on_commit(lambda: notify_admin(instance))

def notify_admin(instance):
    items_text = ''
    for item in instance.items.all():
        name = item.product.name
        qty = item.quantity
        price = item.price_at_purchase
        total = qty * price

        items_text += f"🔹 {name}: {qty} dona — {total:,.0f} so'm\n"

    phone_number = getattr(instance, 'phone_number', None) or instance.user.phone_number
    address = getattr(instance, 'address', None) or instance.user.address

    send_telegram_notification.delay(
        order_id=instance.id,
        products=items_text,
        gmail=instance.user.email,
        phone_number=phone_number,
        address=address,
    )

