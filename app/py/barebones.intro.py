# -*- coding: utf-8 -*-
"""
### @file
### @verbatim
### main:
###   - date: created="Mon Apr 20 12:58:29 2015"
###     last: lastmod="Mon Apr 20 12:58:29 2015"
###     desc: |
###         desc
###
###
### @endverbatim
"""

### ------------------------------------------------------------------------
### begin_: init python
if('python_region'):
###!{{{
###!- caption:  init_python
###!  body: |
      ## std lib
      import blockspring
      import datetime
      import json
      import logging
      import operator
      import os
      import re
      import sys
      import yaml
      
      ## pprint
      import pprint
      oDumper = pprint.PrettyPrinter(indent=4);
    
      pass;
###!}}}

###!{{{
###!- caption:  barebones_runParsed ;; running an already-created blockspring function
###!  date:     created="Mon Apr 20 13:01:56 2015"
###!  goal:     |
###!       show output from a blockspring function online
###!       run on your local machine
###!  result:   |
###!       YES_WORKY
###!  
###!  seealso:   |
###!      https://api.blockspring.com/docs/python-api-reference
###!  
###!  dreftymacid: updating_wormy_steam
###!  body: |
      def barebones_runParsed():
        res = blockspring.runParsed("historic-stock-prices", {
          "ticker": "MSFT",
          "start_date": "2014-1-1",
          "end_date": "2014-1-2"
        })
        print res.params["historical_quotes"]        
###!}}}


### ------------------------------------------------------------------------
### begin_: nameismain
if(__name__ == '__main__'):
###!{{{
###!- caption:  __caption__
###!  date:     created="Wed Feb 18 13:11:30 2015"
###!  tags:     __tags__
###!  desc: |   
###!  		__desc__
###!  
###!  
###!  dreftymacid: __dreftymacid__
###!  body: |
      
      barebones_runParsed()
        
      pass;
###!}}}


