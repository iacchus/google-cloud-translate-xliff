# google-cloud-translate-xliff.py

Translate `.xlf` files using Google Cloud Translate API.

## Usage

### 1. Create a Google Cloud project with the Translate API enabled

You should set the envvar `GOOGLE_APPLICATION_CREDENTIALS` with cretenials
which have access to that project's translate api:

https://cloud.google.com/docs/authentication/getting-started

### 1. Get the script

```sh
wget https://raw.githubusercontent.com/iacchus/google-cloud-translate-xliff/main/google-gloud-translate-xliff.py

```

### 2. Edit the global variables in the script accordingly

```python
XLIFF_FILENAME = "THIS-IS-THE-XLIFF-FILENAME.xlf"
SOURCE_LANGUAGE = "en"  # original language
TARGET_LANGUAGE = "pt"  # translate to this language
```

### 3. Install the dependencies:

Dependencies:

* Python 3
* Python 3 Pip
* PyPI: `google-cloud-translate`
* PyPI: `translate-toolkit`

The last two normally can be installed with:

```sh
pip install google-cloud-translate   translate-toolkit\[all\]
```

### 4. Make executable and run:

```
chmod +x google-cloud-translate-xliff.py

./google-cloud-translate-xliff.py
```
