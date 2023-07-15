# View
- Created in application, not in the project
- It's a python function
- Receive request as param and return a file.

```py
from django.shortcuts import render

def index(request):
  return render(request, 'index.html')
```


# Flow

- urls -> views -> templates