import requests

response = requests.get(f"https://fakestoreapi.com/products/1")

data = response.json()

print(data)
print(data["price"])
print(data["category"])
# nesta caso eu peço peço uma informação especifica e ele tras exatamente o que pediu do site