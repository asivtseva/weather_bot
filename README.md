# weather_bot
## Описание
Бот для получения текущей погоды
## Установка
1. Склонировать этот репозиторий
```
git clone https://github.com/asivtseva/weather_bot.git
cd weather_bot
```
2. Создать и активировать виртуальное окружение
```
python -m venv venv
source venv/bin/activate
```
3. Установить необходимые зависимости
```
pip install -r requirements.txt
```
4. Зарегистрироваться на openweathermap и получить токен
5. Создать телеграм бота с помощью аккаунта @BotFather и получить токен
6. Создать файл .env файл и записать в него токены
```
export TELEGRAM_TOKEN="YOUR TELEGRAM TOKEN"
export WEATHER_TOKEN="YOUR API KEY FROM OPEN WEATHER MAP"
```
```
source .env
```
