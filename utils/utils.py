from dotenv import load_dotenv
import os
import requests
import random
import string


load_dotenv()


# Checking mail with hunter.io
def is_valid_email(email):
    hunter_secret_key = os.environ.get("HUNTER_SECRET_KEY")
    headers = {"Authorization": f"Bearer {hunter_secret_key}"}
    params = {"email": email}

    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={hunter_secret_key}"
    response = requests.get(url=url, params=params, headers=headers).json()
    return response["data"]["status"] == "valid"


# Generate referral code
def generates_code():
    length = 10
    items = string.ascii_letters + string.digits
    code = ''.join(random.choice(items) for _ in range(length))

    return code
