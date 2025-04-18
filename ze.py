import mercadopago
import json
import cobranca
from t import get

sdk = mercadopago.SDK("APP_USR-6810946749343910-102714-ed3a34e585628c745f54998a6ac96bc8-422523501")

def pix(user, valor):
    valor = float(valor)
    payment_data = {
    "transaction_amount": valor,
    "description": f"Spy Zap",
    "payment_method_id": "pix",
    "payer": {    
        "email": "la328028@gmail.com",
        "first_name": "Test",
        "last_name": "User",
        "identification": {
            "type": "CPF",
            "number": "191191191-00"
        },
        "address": {
            "zip_code": "06233-200",
            "street_name": "Av. das Nações Unidas",
            "street_number": "3003",
            "neighborhood": "Bonfim",
            "city": "Osasco",
            "federal_unit": "SP"
        }
    },
    "date_of_expiration":str(get())+".000-04:00",
    }
    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    uid = payment["id"]
    code = payment["point_of_interaction"]["transaction_data"]["qr_code"]
    key = user
    cobranca.cobranca(key,code,uid)
    #pix = payment["point_of_interaction"]["transaction_data"]["ticket_url"]
    return uid
