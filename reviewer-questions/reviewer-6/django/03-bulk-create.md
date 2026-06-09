# models.py

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

# views.py or shell

```python
from myapp.models import Student

students = [
    Student(name="John", age=20),
    Student(name="Anna", age=18),
    Student(name="Mike", age=22),
]

Student.objects.bulk_create(students)
```