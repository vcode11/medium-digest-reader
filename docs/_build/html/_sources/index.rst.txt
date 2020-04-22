.. Medium Pay Wall By Pass documentation master file, created by
   sphinx-quickstart on Wed Apr 22 14:37:23 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

How to bypass medium pay wall!
===================================================
I have attempted to bypass the Medium's tracking in the daily digest it sends out to readers.
Medium has a limit of 5 stories per month and to ensure of it it uses cookies to check the number
of times you have visited their site. Earlier it was possible to read the medium articles by opening
them in private tabs as private tabs don't store any site data and cookies. But now medium sends digests
with links to blogs that contains get parameters identifying the email address to which the digest was sent
and they require you to Log In before reading the complete story.

The hack to bypass it
------------------------
I have used regular expressions to get rid of the tracking part of the urls in digest. Now these links can
be accessed easily in private tabs and you can enjoy full story. This script reads your medium digest
e-mail removes the tracking urls and sends you the stories right in your inbox.

Set Up
-----------------------

Download the source code from Github ::

        git clone https://github.com/vcode11/medium-digest-reader.git
        cd medium-digest-reader/

Installing the required packages ::

        pip3 install -r requirements.txt 

Set up Gmail API

+ Go to https://developers.google.com/gmail/api/quickstart/python/
+ Click the Enable Gmail API Button
+ Fill out the form that appears
+ After you have filled out the form a link to download credentials.json appears
+ Download this file in the same medium-digest-reader directory
+ This file contains your gmail credentials. Keep it secret.
+ In the interactive shell enter following code ::
        
        >>> import ezgmail, os
        >>> os.chdir(r'C:\path\to\credentials_json_file')
        >>> ezgmail.init()
+ The ezgmail.init() function will open your browser to a Google sign-in page. Enter your Gmail address and password. The page may warn you “This app isn’t verified,” but this is fine, click Advanced and then Go to Quickstart (unsafe)
+ This will generate a token.json file in the same directory
+ You are all set

Usage
-------
Run the reader.py script using python3 ::
        
        python3 reader.py

You can now check you email box for a tracking free copy of the digest blogs.  

Regarding Improvements
--------------------------
This was a extremely simple pet project of mine. I don't have a good idea of how to use MIME type to send hybird email like the one medium sends.
Please feel free to point out bugs and make PR's to fix and add new improvements.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

