#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import subprocess
import sys

def my_request(url):
  r = requests.get(url)
  html = r.text
  pattern = r"addPlayer\((.+?), (.+?), (.+?), (.+?), (.+?),(.+?), (.+?),(.+?),(.+?),(.+?),(.+?)\);"
  pattern_search = re.search(pattern, html)
  pattern_search = pattern_search.groups()
  url_m38u = pattern_search[0].strip().replace("\"", "")
  file_mp4_re = re.search("https://(.+?)/(.+?)/(.+?)/(.+?)/(.+?)/(.+?)/index.m3u8", url_m38u)
  file_name = file_mp4_re.groups()[5]
  return file_name, url_m38u

def download(file_name, url_m38u):
  file_name = "./"+file_name
  popen = subprocess.Popen(["downloadm3u8", "-o", file_name, url_m38u])
  popen.wait()

if len(sys.argv) > 1:
  url = sys.argv[1]
  if url:  
    file_name, url_m38u = my_request(url)
    download(file_name, url_m38u)


