import requests


https_request = requests.get("https://fastapi.jurkiewicz.tech/")
api_data = https_request.json()
# teraz wyciągamy konkretny element z naszego słownika
header = "Client's headers"
print(f"IP klienta to {api_data[header]['x-forwarded-for']}")
print(f"Przeglądarka klienta to {api_data[header]['user-agent']}")
