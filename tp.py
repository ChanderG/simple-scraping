#! /usr/bin/python

import sys
import requests
import lxml.html

def getLinks():
  print "Getting links:\n"
  links = []
  for i in range (1,5):
    hxs = lxml.html.document_fromstring(requests.get("http://tp.iitkgp.ernet.in/notice/index.php?page=" + str(i)).content)
    try:
      l = hxs.xpath('//a[@class="notice"]/text()')
      links = links + l
    except IndexError:
      print "error"

  for i in links:
    print i

if __name__ == "__main__":
  getLinks()
