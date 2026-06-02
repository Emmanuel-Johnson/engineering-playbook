| Algorithm      | Best       | Average    | Worst      | Space    | Stable | Adaptive |
| -------------- | ---------- | ---------- | ---------- | -------- | ------ | -------- |
| Bubble Sort    | O(n)       | O(n²)      | O(n²)      | O(1)     | ✅      | ✅*       |
| Selection Sort | O(n²)      | O(n²)      | O(n²)      | O(1)     | ❌      | ❌        |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)     | ✅      | ✅        |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | ✅      | ❌        |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n) | ❌      | ❌        |

- Stable → Keeps order of equal elements
- In-Place → Uses very little extra memory
- Adaptive → Faster for nearly sorted arrays