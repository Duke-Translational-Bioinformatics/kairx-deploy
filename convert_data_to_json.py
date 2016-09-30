# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 12:24:28 2016

@author: nn31
"""

import pandas as pd
import simplejson

bora_data = pd.read_csv(open('/Users/nn31/Dropbox/40-githubRrepos/kairx-deploy/KaiRx.Smith.MedList.V15.csv','r'))
json_data = bora_data.to_json(orient='records')


twitterDataFile = open("/Users/nn31/Dropbox/40-githubRrepos/kairx-deploy/kairx_data_csv_to_json_script.json", "w")
# magic happens here to make it pretty-printed
twitterDataFile.write(simplejson.dumps(simplejson.loads(json_data), indent=2))
twitterDataFile.close()