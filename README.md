# pyopenie
Python wrapper for OpenIE5.  This simply wraps the API from the server included with [OpenIE 5.1.0](https://github.com/dair-iitd/OpenIE-standalone).

# Install
```
pip install pyopenie
```

# Usage
First make sure you have the OpenIE5 server running.  See [the instructions here](https://github.com/dair-iitd/OpenIE-standalone#running-as-http-server) for how to do that.

Then the setup just requires you to pass in the url of the server:
```
>>> from pyopenie import OpenIE5
>>> extractor = OpenIE5('http://localhost:9000')
```
Any English sentence can be passed to OpenIE5 server.
```
>>> extractions = extractor.extract("The U.S. president Barack Obama gave his speech to thousands of people.")
```
The result is a JSON list of extractions with confidence, offset and other properties.
```
>>> extractions
[
    {
        "confidence": 0.38089450366724514,
        "sentence": "The U.S. president Barack Obama gave his speech on Tuesday to thousands of people.",
        "extraction": {
            "arg1": {
                "text": "Barack Obama",
                "offsets": [...]
            },
            "rel": {
                "text": "[is] president [of]",
                "offsets": [...]
            },
            "arg2s": [
                {
                    "text": "United States",
                    "offsets": [...]
                }
            ],
            "context": null,
            "negated": false,
            "passive": false
        }
    },
    {
        "confidence": 0.9168198459177435,
        "sentence": "The U.S. president Barack Obama gave his speech on Tuesday to thousands of people.",
        "extraction": {
            "arg1": {
                "text": "The U.S. president Barack Obama",
                "offsets": [...]
            },
            "rel": {
                "text": "gave",
                "offsets": [...]
            },
            "arg2s": [
                {
                    "text": "his speech",
                    "offsets": [...]
                },
                {
                    "text": "on Tuesday",
                    "offsets": [...]
                },
                {
                    "text": "to thousands of people",
                    "offsets": [...]
                }
            ],
            "context": null,
            "negated": false,
            "passive": false
        }
    }
]
```
Individual properties can also be accessed.
```
>>> extractions[0]['confidence']
0.38089450366724514

>>> extractions[0]['extraction']['arg1']['text']
'Barack Obama'
```
