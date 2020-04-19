# PySendMail-Attachments :computer: :e-mail: :key:

## Summary
#### What is SMTP?
SMTP (*Simple Mail Transfer Protocol*) is a communication protocol for electronic mail transmission. As an Internet standard, SMTP was first defined in 1982 by RFC 821, and updated in 2008 by RFC 5321 to Extended SMTP additions, which is the protocol variety in widespread use today. Mail servers and other message transfer agents use SMTP to send and receive mail messages. Proprietary systems such as Microsoft Exchange and IBM Notes and webmail systems such as Outlook.com, Gmail and Yahoo! Mail may use non-standard protocols internally, but all use SMTP when sending to or receiving email from outside their own systems. SMTP servers commonly use the Transmission Control Protocol on port number 25.

- port 587 should only be used for submissions [This port, coupled with TLS encryption] (i.e., mail client to mail server),
- port 25 should only be used for relaying (i.e., mail server to mail server communications), and
- port 465 should no longer be used at all.

##### For test SMTP with CLI (PuTTY)

- Request: 

``` raw smtp.gmail.com 587 > HELO client – Host (Gmail) - Secure(TLS) – Port(587)```

- Response: 

```diff
! 250 smtp.gmail.com at your service
```

#### Useful links
* [SMTP CLI](https://www.mailgun.com/blog/which-smtp-port-understanding-ports-25-465-587/ "SMTP CLI")
* [What SMTP](https://www.sparkpost.com/blog/what-smtp-port/ "What SMTP")
* [SMTP Port](https://www.jscape.com/blog/smtp-ports "SMTP Port")

#### What is MIME?
MIME (*Multipurpose Internet Mail Extensions*) is an Internet standard that extends the format of email messages to support text in character sets other than ASCII, as well as attachments of audio, video, images, and application programs. Message bodies may consist of multiple parts, and header information may be specified in non-ASCII character sets. Email messages with MIME formatting are typically transmitted with standard protocols, such as the Simple Mail Transfer Protocol (SMTP), the Post Office Protocol (POP), and the Internet Message Access Protocol (IMAP). 

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

##### For test encode and decode (Base64 > ASCII, etc.)
* [Online converter](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html "Base64 converter")

#### Useful links
* [Base64](https://en.wikipedia.org/wiki/Base64 "Base64")
* [MIME](https://en.wikipedia.org/wiki/MIME "MIME")
* [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol "SMTP")


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
* _PySendMail-Attachements_ is distributed under the **LGPL** version 3 license.
