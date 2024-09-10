
```bash
pip install pyshorteners
```

Now, let's create the Python script:

```python
import pyshorteners

def shorten_url(long_url):
    # Initialize the URL shortener
    s = pyshorteners.Shortener()

    # Shorten the URL using the default shortening service (usually TinyURL)
    short_url = s.short(long_url)

    return short_url

def main():
    long_url = input("Enter the long URL: ")
    short_url = shorten_url(long_url)
    print("Short URL:", short_url)

if __name__ == "__main__":
    main()
```
