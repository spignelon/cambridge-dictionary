# Cambridge-Dictionary
Cambridge dictionary CLI which also caches the words and meanings in a local database
---

### To setup first install:
1. ```pip install requests```
2. ```pip install bs4```

### Usage:
```python cambridge.py word```

---

### Usage tutorial
[![asciicast](https://asciinema.org/a/K8mwaAYJTEpK2VRDEAZJ2jcWe.svg)](https://asciinema.org/a/K8mwaAYJTEpK2VRDEAZJ2jcWe)

---
Once you search for the word and gets the meaning, it saves it into a local database from which it retrieves them if you search for the same word again in the future instead of fetching it from the server. This makes it quick, run even when there's no internet connection (assuming that your local database is of substantial size) and prevents making too many queries to the server.
