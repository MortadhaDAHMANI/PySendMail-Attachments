# PySendMail-Attachements :computer: :e-mail: :key:

## Summary
#### What is Base64?
In computer science, Base64 is a group of binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation. The term Base64 originates from a specific MIME content transfer encoding.

Each Base64 digit represents exactly 6 bits of data. Three 8-bit bytes (i.e., a total of 24 bits) can therefore be represented by four 6-bit Base64 digits.

Common to all binary-to-text encoding schemes, Base64 is designed to carry data stored in binary formats across channels that only reliably support text content. Base64 is particularly prevalent on the World Wide Web where its uses include the ability to embed image files or other binary assets inside textual assets such as HTML and CSS files.

#### Example
##### CSV File
```csv
name,email,grade
John Doe,john.doe@gmail.com,B+
Mortadha DAHMANI,mortadha.dahmani@gmail.com,A
```
##### CSV File into Base64 
```diff
+ bmFtZSxlbWFpbCxncmFkZQ0KSm9obiBEb2Usam9obi5kb2VAZ21haWwuY29tLEIrDQpNb3J0YWRoYSBEQUhNQU5JLG1vcnRhZGhhLmRhaG1hbmlAZ21haWwuY29tLEE=
```

##### For test encode and decode
* [Online converter](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html "AT Commands")

## Requirements
- ``Python 2.7 or Python 3.4 and newer``

- ``If running on Windows: Windows 7 or newer``

### Google account manager 
```diff
- Change your Less secure app access On
```

![alt iviny](https://github.com/MortadhaDAHMANI/PySendMail-Attachements/raw/master/LSA2.png)

## Installation

This installs a package that can be used from Python:

```python
   import email, smtplib, ssl, os
```
### From PyPI

pySerial can be installed from PyPI:

    python -m pip install smtplib

Using the `python`/`python3` executable of the desired version (2.7/3.x). 

Developers also may be interested to get the source archive, because it
contains examples, tests and the this documentation. By using PyPI, you will be using the latest stable version.

## Preview
### Terminal

![alt iviny](https://github.com/MortadhaDAHMANI/PySendMail-Attachements/raw/master/pyMail.png)

### Donation
If this project help you, you can give me a tip ;)

<a href="https://paypal.me/mamdpay" rel="In"> <img src="https://www.pngarts.com/files/4/Paypal-Donate-PNG-High-Quality-Image.png" alt="Donation" height="70"></a>

### Author
* This version has been created by: [**Mortadha DAHMANI**](mailto:mortadha.dahmani@gmail.com)

<a href="https://www.linkedin.com/in/mortadhadahmani" rel="In"> <img src="https://github.com/MortadhaDAHMANI/Py-SIM800L/raw/master/in2.jpg" alt="In" height="40"></a>

### Revision History
* Initial Release : 08 April 2020

### License
* PySendMail-Attachements is distributed under the **LGPL** version 3 license.
