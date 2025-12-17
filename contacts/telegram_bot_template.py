"""
Telegram бот для отправки уведомлений.
Для использования создайте telegram_bot.py с реальными значениями.
"""

import os
import requests

class TelegramNotifier:
    def __init__(self):
        # Берем токен из переменных окружения
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_CHAT_ID_HERE')
        
        if not self.bot_token or self.bot_token == 'YOUR_BOT_TOKEN_HERE':
            print("⚠️ Telegram токен не настроен")
        
    def send_notification(self, name, phone, service_info):
        """Отправка уведомления в Telegram"""
        if not self.bot_token or not self.chat_id:
            print("❌ Telegram не настроен: нет токена или chat_id")
            return False
        
        message = f"📞 Новая заявка!\n\n👤 Имя: {name}\n📱 Телефон: {phone}\n📋 Услуга: {service_info}"
        
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            data = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            
            response = requests.post(url, data=data, timeout=10)
            response.raise_for_status()
            print(f"✅ Telegram отправлен успешно")
            return True
            
        except Exception as e:
            print(f"❌ Ошибка отправки в Telegram: {e}")
            return False

# Создаем экземпляр для импорта
telegram_notifier = TelegramNotifier()
