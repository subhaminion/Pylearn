#!/usr/bin/python
import urllib
import json
# import os
# title = os.environ["word"]
# print title
print '***Hello Human Welcome To Subhams Terminal Dictionary Application***'
title = raw_input('Enter your word: ')
url = 'http://glosbe.com/gapi/translate?from=eng&dest=eng&\
format=json&phrase='+title+'&pretty=true'
result = json.load(urllib.urlopen(url))
print 'Meaning: ', result["tuc"][0]["meanings"][1]["text"]