# Common Time Methods and Operations in Python

Use the `datetime` module for working with time and dates.

```python
from datetime import datetime, time, timedelta
```

---

## 1. Get Current Time

```python
now = datetime.now()
print(now)
```

---

## 2. Get Only Time

```python
print(now.time())
```

---

## 3. Access Hour, Minute, Second

```python
print(now.hour)
print(now.minute)
print(now.second)
```

---

## 4. Create Custom Time

```python
t = time(14, 30, 45)
print(t)
```

---

## 5. Format Time (`strftime`)

```python
print(now.strftime("%H:%M:%S"))   # 24-hour format
print(now.strftime("%I:%M %p"))   # 12-hour AM/PM format
```

---

## 6. Convert String to Time (`strptime`)

```python
t = datetime.strptime("18:45:20", "%H:%M:%S")
print(t)
```

---

## 7. Time Arithmetic

```python
future = now + timedelta(hours=2)
past = now - timedelta(minutes=30)

print(future)
print(past)
```

---

## 8. Difference Between Times

```python
t1 = datetime.now()

# some code

t2 = datetime.now()

print(t2 - t1)
```

---

# Important Operations

```python
+ timedelta()   # Add time
- timedelta()   # Subtract time
t2 - t1         # Find difference between times
strftime()      # Convert datetime to string
strptime()      # Convert string to datetime
```
