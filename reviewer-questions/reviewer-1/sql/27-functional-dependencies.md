- Trivial Functional Dependency
If Y is a subset of X.
Example: {Student_ID, Name} → Name

- Non-Trivial Functional Dependency
If Y is not a subset of X.
Example: Student_ID → Name

- Full Functional Dependency
Y depends on the entire X, not just part of it.
Example: (Student_ID, Course_ID) → Grade

- Partial Dependency
Y depends on only part of a composite key.
Example: (Student_ID, Course_ID) → Student_Name, where Student_Name depends only on Student_ID.