import mercadopago

# Replace with your access token
ACCESS_TOKEN = "APP_USR-6810946749343910-102714-ed3a34e585628c745f54998a6ac96bc8-422523501"

# Initialize the MercadoPago SDK
sdk = mercadopago.SDK(ACCESS_TOKEN)

# Function to get the payment by ID
def get_payment_by_id(payment_id):
    try:
        # Get the payment via the API
        payment_info = sdk.payment().get(payment_id)
        return payment_info
    except Exception as e:
        print(f"Error getting payment: {e}")
        return None

# Replace with the ID of the payment you want to query
 
