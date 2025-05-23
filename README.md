# CryptoManager 📈💰

**Библиотека для работы с криптовалютами и обычными валютами без API ключей**

CryptoManager предоставляет простой и удобный способ получения актуальных курсов криптовалют и фиатных валют, а также конвертации между ними. Библиотека автоматически использует несколько API провайдеров для обеспечения высокой доступности и точности данных без необходимости указания API ключей.

```python
import cryptomanager
from cryptomanager import cm

# Получить цену Bitcoin в USD
BTC_PRICE = cm.price(1, 'BTC')
print(f"Цена биткойна: {BTC_PRICE}")

# Вставка своей переменной
RUBY = 80  # По курсу к доллару
btc_to_ruby = cm.transfer.local(1, 'BTC').to((RUBY, 'RUBY'))
print(f"1 биткойн в рублях: {btc_to_ruby}")

# Перевод в настоящие валюты
btc_to_usdt = cm.transfer(1, 'BTC').to('USDT')
print(f"1 биткойн в долларах: {btc_to_usdt}")

# Создание денежной суммы
usdt = cm.money('USDT')
amount = usdt(1000)
print(f"Сумма: {amount}")
```

## 📦 Установка

```bash
pip install cryptomanager
```

## 🚀 Быстрый старт

### Получение цен криптовалют

```python
import cryptomanager
from cryptomanager import cm

# Получить цену в USD (по умолчанию)
BTC_PRICE = cm.price(1, 'BTC')
print(f"Цена биткойна: {BTC_PRICE}")

# Указать другую фиатную валюту
ETH_EUR = cm.price(1, 'ETH', 'EUR')
print(f"Цена Ethereum в евро: {ETH_EUR}")

# Использование объектов валют
SOL_PRICE = cm.price(1, cm.SOL)
print(f"Цена Solana: {SOL_PRICE}")
```

### Конвертация валют

```python
# Конвертировать между валютами
btc_to_usdt = cm.transfer(1, 'BTC').to('USDT')
print(f"1 биткойн в долларах: {btc_to_usdt}")

eth_to_btc = cm.transfer(10, 'ETH').to('BTC')
print(f"10 Ethereum в биткойнах: {eth_to_btc}")

# Использование объектов валют
eth_to_usdt = cm.transfer(5, cm.ETH).to(cm.USDT)
print(f"5 Ethereum в долларах: {eth_to_usdt}")
```

### Локальная конвертация с фиксированным курсом

```python
# Установка локального курса
RUBY = 80  # Курс к доллару
btc_to_ruby = cm.transfer.local(1, 'BTC').to((RUBY, 'RUBY'))
print(f"1 биткойн в рублях: {btc_to_ruby}")

# Другой пример локального перевода
EUR_RATE = 0.92  # Курс EUR к USD
usd_to_eur = cm.transfer.local(100, 'USD').to((EUR_RATE, 'EUR'))
print(f"100 долларов в евро: {usd_to_eur}")
```

### Работа с денежными суммами

```python
# Создание денежной суммы в USDT
usdt = cm.money('USDT')
usdt_amount = usdt(1000)
print(f"Создана сумма: {usdt_amount}")

# Конвертация в другую валюту
btc_amount = usdt_amount.to('BTC')
print(f"1000 USDT в биткойнах: {btc_amount}")

# Использование объектов валют
eth = cm.money(cm.ETH)
eth_amount = eth(5)
print(f"Создана сумма: {eth_amount}")
```

## ⚙️ Настройки

### Управление кэшированием

```python
# Изменить интервал обновления данных (по умолчанию 60 сек)
cm.set_update_interval(30)  # Обновлять каждые 30 секунд

# Очистить кэш для получения самых свежих данных
cm.clear_cache()
```

### API ключи (опционально)

Библиотека работает без API ключей, но вы можете установить их для расширения возможностей:

```python
# Установить API ключ для CoinMarketCap
cm.set_api_key('coinmarketcap', 'ваш_api_ключ')

# Установить API ключ для Alpha Vantage
cm.set_api_key('alphavantage', 'ваш_api_ключ')
```

### Получение списков поддерживаемых валют

```python
# Получить список поддерживаемых криптовалют
cryptos = cm.get_supported_cryptos()
print(f"Поддерживается {len(cryptos)} криптовалют")

# Получить список поддерживаемых фиатных валют
fiats = cm.get_supported_fiats()
print(f"Поддерживается {len(fiats)} фиатных валют")
```

## 🔌 Поддерживаемые API

Библиотека автоматически использует следующие API провайдеры:

### Криптовалютные API:
- Binance
- CoinGecko
- CoinCap
- CryptoCompare
- Kraken
- Bitfinex
- Huobi
- OKX
- Bybit
- CoinMarketCap (опционально с API ключом)
- KuCoin
- Gate.io
- Gemini
- Bitstamp
- Bittrex

### Фиатные API:
- Frankfurter
- Exchangerate.host
- ExchangeRate-API (опционально с API ключом)
- Open Exchange Rates (опционально с API ключом)
- Currency Layer (опционально с API ключом)
- Fixer.io (опционально с API ключом)
- Alpha Vantage (опционально с API ключом)

## 🧩 Расширенное использование

### Прямой доступ к классу CryptoManager

Для более гибкого использования вы можете создать собственный экземпляр класса `CryptoManager`:

```python
from cryptomanager import CryptoManager

# Создать экземпляр с собственными настройками
my_rates = CryptoManager(update_interval=120)

# Установить API ключи при инициализации
api_keys = {
    'coinmarketcap': 'ваш_ключ_coinmarketcap',
    'alphavantage': 'ваш_ключ_alphavantage'
}
my_rates_with_keys = CryptoManager(api_keys=api_keys)

# Использовать методы экземпляра
price = my_rates.price(1, 'BTC')
```

### Обработка ошибок

Рекомендуется использовать try-except для обработки возможных ошибок:

```python
try:
    price = cm.price(1, 'BTC')
    print(f"Цена биткойна: {price}")
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    converted = cm.transfer(1, 'ETH').to('RUB')
    print(f"1 ETH = {converted} RUB")
except Exception as e:
    print(f"Не удалось выполнить конвертацию: {e}")
```

### Логирование

Библиотека использует стандартный модуль `logging` Python. Вы можете настроить уровень логирования:

```python
import logging

# Настроить логирование для отладки
logging.getLogger('cryptomanager').setLevel(logging.DEBUG)

# Или для минимального вывода
logging.getLogger('cryptomanager').setLevel(logging.ERROR)
```

## 📊 Примеры использования

### Мониторинг портфеля криптовалют

```python
portfolio = {
    'BTC': 0.5,
    'ETH': 10,
    'SOL': 50,
    'DOGE': 1000
}

total_usd = 0
for crypto, amount in portfolio.items():
    try:
        value = cm.price(amount, crypto)
        total_usd += value
        print(f"{amount} {crypto} = ${value:,.2f}")
    except Exception as e:
        print(f"Ошибка при получении цены {crypto}: {e}")

print(f"Общая стоимость портфеля: ${total_usd:,.2f}")
```

### Отслеживание изменений цены

```python
import time

crypto = 'BTC'
interval = 60  # секунды
duration = 10  # количество проверок

try:
    initial_price = cm.price(1, crypto)
    print(f"Начальная цена {crypto}: ${initial_price}")

    for i in range(duration):
        time.sleep(interval)
        current_price = cm.price(1, crypto)
        change = ((current_price - initial_price) / initial_price) * 100
        print(f"Текущая цена {crypto}: ${current_price} ({change:+.2f}%)")
except Exception as e:
    print(f"Ошибка: {e}")
```

### Конвертация между несколькими валютами

```python
amount = 1000
base_currency = 'USD'
target_currencies = ['EUR', 'GBP', 'JPY', 'RUB', 'CNY', 'BTC', 'ETH']

for target in target_currencies:
    try:
        converted = cm.transfer(amount, base_currency).to(target)
        print(f"{amount} {base_currency} = {converted} {target}")
    except Exception as e:
        print(f"Ошибка при конвертации в {target}: {e}")
```

## 📜 Лицензия

MIT - используйте как хотите, см. файл [LICENSE](LICENSE) для подробностей.

## Связь:

Telegram: @pavlyska
Discord: pavlyska

Страница на pypl: https://pypi.org/project/cryptomanager/#description

### С ❤ к миру

---

Разработано для удобной работы с криптовалютами и обычными валютами без необходимости API ключей.
