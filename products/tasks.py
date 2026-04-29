import time

import requests
from django.conf import settings
from celery import shared_task


@shared_task(bind=True, max_retries=3) # Xato bo'lsa 3 marta qayta urinadi
def send_telegram_notification(self, order_id, products, email, phone_number, address):
    # time.sleep(5)
    try:
        token = settings.TELEGRAM_BOT_TOKEN
        message_text = (f"🆕 Yangi buyurtma: #{order_id}\n\n{products}\n👤 Mijoz: {email}\n"
                        f"📞 Tel: {phone_number}\nAddress: {address}"),

        response = requests.post(
            url=f"https://api.telegram.org/bot{token}/sendMessage",
            data={
                "chat_id": settings.ADMIN_CHAT_ID,
                "text": message_text,
                "parse_mode": "HTML"  # Agar mahsulotlar matnida <b> ishlatsangiz kerak bo'ladi
            },
            timeout=10  # API javobini 10 soniyadan ko'p kutmaslik uchun
        )
        response.raise_for_status()  # Agar status 200 bo'lmasa xato qaytaradi
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)  # 1 daqiqadan keyin qayta urinadi