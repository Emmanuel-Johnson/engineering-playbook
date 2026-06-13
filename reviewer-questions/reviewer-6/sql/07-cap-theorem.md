- CAP Theorem says a distributed system can only fully guarantee 2 out of these 3 at the same time:

- Consistency (C) → Every user sees the same latest data.
- Availability (A) → System always gives a response.
- Partition Tolerance (P) → System still works even if servers lose connection with each other.

- Example:
- If two servers disconnect (network failure), the system must choose:

- give correct/latest data (Consistency)
- OR
- keep responding even if data may differ (Availability).