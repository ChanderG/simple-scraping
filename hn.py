#! /usr/bin/python

import sys
import requests
import lxml.html

def getLinks():
  print "Getting links:\n"
  hxs = lxml.html.document_fromstring(requests.get("https://news.ycombinator.com/").content)
  links = []

  try:
    l = hxs.xpath('//*[@class="title"]/a/text()')
    links = links + l
  except IndexError:
    print "error"

  for i in links:
    print i

if __name__ == "__main__":
  getLinks()
