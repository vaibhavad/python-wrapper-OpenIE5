# pyopenie
Python wrapper for OpenIE5.  This simply wraps the API from the server included with [OpenIE 5.1.0]() for details.

# Install
```
pip install pyopenie
```

# Usage
First make sure you have the OpenIE5 server running.  See [the instructions here]() for how to do that.

Then the setup just requires you to pass in the url of the server:
```
>>> from pyopenie import OpenIE5
>>> extractor = OpenIE5('http://localhost:9000')
```
