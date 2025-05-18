"""
Модуль для тестирования библиотеки CryptoManager
"""

import sys
import os

# Добавляем путь к библиотеке в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cryptomanager
from cryptomanager import cm

def test_price():
    """Тестирование функции price"""
    print("=== Тестирование cm.price ===")
    
    # Получение цены BTC в USD
    btc_price = cm.price(1, 'BTC')
    print(f"Цена биткойна: {btc_price}")
    
    # Получение цены ETH в EUR
    eth_price = cm.price(1, 'ETH', 'EUR')
    print(f"Цена Ethereum в EUR: {eth_price}")
    
    # Использование объектов валют
    btc_obj_price = cm.price(1, cm.BTC)
    print(f"Цена биткойна (через объект): {btc_obj_price}")
    
    print()

def test_transfer():
    """Тестирование функции transfer"""
    print("=== Тестирование cm.transfer ===")
    
    # Перевод BTC в USDT
    btc_to_usdt = cm.transfer(1, 'BTC').to('USDT')
    print(f"1 биткойн в долларах: {btc_to_usdt}")
    
    # Перевод ETH в BTC
    eth_to_btc = cm.transfer(10, 'ETH').to('BTC')
    print(f"10 Ethereum в биткойнах: {eth_to_btc}")
    
    # Использование объектов валют
    eth_to_usdt = cm.transfer(5, cm.ETH).to(cm.USDT)
    print(f"5 Ethereum в долларах: {eth_to_usdt}")
    
    print()

def test_transfer_local():
    """Тестирование функции transfer.local"""
    print("=== Тестирование cm.transfer.local ===")
    
    # Локальный перевод с фиксированным курсом
    RUBY = 80  # Курс к доллару
    btc_to_ruby = cm.transfer.local(1, 'BTC').to((RUBY, 'RUBY'))
    print(f"1 биткойн в рублях: {btc_to_ruby}")
    
    # Другой пример локального перевода
    EUR_RATE = 0.92  # Курс EUR к USD
    usd_to_eur = cm.transfer.local(100, 'USD').to((EUR_RATE, 'EUR'))
    print(f"100 долларов в евро: {usd_to_eur}")
    
    print()

def test_money():
    """Тестирование функции money"""
    print("=== Тестирование cm.money ===")
    
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
    
    print()

def main():
    """Основная функция для запуска тестов"""
    print("Тестирование библиотеки CryptoManager\n")
    
    test_price()
    test_transfer()
    test_transfer_local()
    test_money()
    
    print("Тестирование завершено")

if __name__ == "__main__":
    main()
