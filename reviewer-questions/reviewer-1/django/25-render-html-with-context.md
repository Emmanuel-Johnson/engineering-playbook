```python
from django.shortcuts import render

def home(request):
    datas = [
        {
            "customer_id": 1,
            "full_name": "John Doe",
            "age": 31,
            "country": "USA",
            "total_amount": 400,
            "customer_category": "Low Value Customer",
            "shipping_status": "Delivered",
        },
        {
            "customer_id": 2,
            "full_name": "Robert Luna",
            "age": 22,
            "country": "USA",
            "total_amount": 250,
            "customer_category": "Low Value Customer",
            "shipping_status": "Pending",
        },
        {
            "customer_id": 3,
            "full_name": "David Robinson",
            "age": 22,
            "country": "UK",
            "total_amount": 12000,
            "customer_category": "High Value Customer",
            "shipping_status": "Delivered",
        },
        {
            "customer_id": 4,
            "full_name": "John Reinhardt",
            "age": 25,
            "country": "UK",
            "total_amount": 700,
            "customer_category": "Low Value Customer",
            "shipping_status": "Pending",
        },
        {
            "customer_id": 5,
            "full_name": "Betty Doe",
            "age": 28,
            "country": "UAE",
            "total_amount": 0,
            "customer_category": "Low Value Customer",
            "shipping_status": "Pending",
        },
    ]
    return render(request, 'home.html', {"datas" : datas})
```




{% for data in datas %}
<div>
    <p>Customer ID: {{ data.customer_id }}</p>
    <p>Full Name: {{ data.full_name }}</p>
    <p>Age: {{ data.age }}</p>
    <p>Country: {{ data.country }}</p>
    <p>Total Amount: {{ data.total_amount }}</p>
    <p>Customer Category: {{ data.customer_category }}</p>
    <p>Shipping Status: {{ data.shipping_status }}</p>
</div>
<hr>
{% empty %}
<p>No data available.</p>
{% endfor %}