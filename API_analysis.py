
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
API_URL = "https://jsonplaceholder.typicode.com/users"
def get_customers(url) -> list[dict]:
    try:
        response = requests.get(url, timeout=10.0)
        customer_info = response.json()
        return customer_info
    except requests.exceptions.ConnectionError:
        print("Network error. Unable to connect to the server.")

customer_info = get_customers(API_URL)
customer_info  

def explore(record, indent=0):
    for key, value in record.items():
        print("  " * indent + f"- {key}: {type(value).__name__}")
        
        if isinstance(value, dict):
            explore(value, indent + 1)

explore(customer_info[0])

def extract_attributes(customer_info):
    customers_data = []
    
    for item in customer_info:
        
        record = {
            "id": item["id"],
            "name": item["name"],
            "username": item["username"],
            "email": item["email"],
            "email_domain":item["email"].split("@")[1],
            "phone": item["phone"],
            "city": item["address"]["city"],
            "zipcode": item["address"]["zipcode"],
            "latitude": float(item["address"]["geo"]["lat"]),
            "longitude": float(item["address"]["geo"]["lng"]),
            "company": item["company"]["name"],
            "website": item["website"]
        }
        
        customers_data.append(record)
        
    return customers_data
clean_customers = extract_attributes(customer_info)
clean_customers

def unique_cities(customers):
    cities = set()

    for customer in customers:
        cities.add(customer["address"]["city"])

    return cities

city_set = unique_cities(customer_info)
num_customers = len(customer_info)
no_cities = len(city_set)
print(f"Total customers are {num_customers}")
print(f"Total cities are {no_cities}")      
print(f"The total number of customers is {num_customers} and they are locoated in a total of {no_cities} cities. We have equally distributed customers ")

def city_counts(customers):
    counts = {}

    for customer in customers:
        city = customer["address"]["city"]
        counts[city] = counts.get(city, 0) + 1

    return counts
city_counts(customer_info)

def email_domain_counts(customers):
    domains = {}

    for customer in customers:
        domain = customer["email"].split("@")[1]
        domains[domain] = domains.get(domain, 0) + 1

    return domains
email_domain_counts(customer_info)

def to_df(data):
    df = pd.DataFrame(data) 
    return df
df_customers = to_df(customer_info)
df_customers

df_customers.to_csv("output/customers.csv", index=False)

city_dict = city_counts(customer_info)
city_dict
df_city_counts = pd.DataFrame(list(city_dict.items()), columns=["city", "count"])
df_city_counts

df_city_counts.to_csv("output/city_counts.csv", index=False)

def plot_distribution(counts_dict, path):
   
    categories = list(counts_dict.keys())
    values = list(counts_dict.values())
    
    
    plt.figure(figsize=(10, 5))
    
  
    plt.bar(categories, values, color='skyblue')
    
    
    plt.xlabel("Categories")
    plt.ylabel("Count")
    plt.title("Pesa Pulse Customer Distribution")
    plt.xticks(rotation=45, ha='right')
    
   
    plt.tight_layout()
    
    
    plt.savefig(path)
    plt.close()
    print(f"Chart successfully saved to {path}")

plot_distribution(city_dict, "output/city_distribution.png")