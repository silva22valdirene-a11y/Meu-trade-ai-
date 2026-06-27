import hmac
import hashlib
import time
import requests

def place_order(symbol, quantity, price):
    # O Mercado Bitcoin exige que você crie uma string baseada na sua chave
    # e na data atual, e depois assine com SHA512.
    pass 
