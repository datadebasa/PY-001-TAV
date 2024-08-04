# Library

## gTTS 
gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API. Write spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout.

## audiosegment 
Wrapper for pydub.AudioSegment for additional high level methods [audiosegment](https://pypi.org/project/audiosegment/).

## pydub
Manipulate audio with an simple and easy high level interface [pydub](https://pypi.org/project/pydub/).

## Pillow
[Pillow](https://pypi.org/project/pillow/) is the friendly PIL fork by Jeffrey A. Clark and contributors. PIL is the Python Imaging Library by Fredrik Lundh and contributors. As of 2019, Pillow development is supported by Tidelift.
## numpy 

## OpenCV 
The aim of this repository is to provide means to package each new OpenCV release for the most used Python versions and platforms [OpenCV](https://pypi.org/project/opencv-python/) .

## Requests
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method! [request](https://pypi.org/project/requests/)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gTTS.

```bash
pip install gTTS pydub opencv-python requests numpy pillow 
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
