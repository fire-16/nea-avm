#import ibraries
import streamlit as st 
import pandas as pd 
import numpy as np 
import re
from urllib.parse import quote
import requests
import json


#title of tool 

st.header('HOME- AVM', divider='gray')

#postcode input
postcode = st.text_input('Please enter Postcode:')

#validation of postcode
valid = 'False'
if len(postcode.replace(" ", "")) == 5:
  valid = re.compile("^[a-zA-Z]{1}[0-9]{2}[a-zA-Z]{2}")
elif len(postcode.replace(" ", "")) == 6:
  valid = re.compile("^[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}")
elif len(postcode.replace(" ", "")) == 7:  
  valid = re.compile("^[a-zA-Z]{2}[0-9]{3}[a-zA-Z]{2}")
if postcode and valid == 'False':
  st.error("Please enter valid postcode or select an address below")


#postcode to address



addresses=[]
  # request parameters
api_key = "PCWRT-7DQ5Y-4JEMD-QXACD"
country_code = "UK"
search_term = postcode

  # prepare request and encode user-entered parameters with %xx encoding
request_url = f"https://ws.postcoder.com/pcw/{api_key}/address/{country_code}/{quote(search_term, safe='')}"

  # send request
response = requests.get(request_url)

  # process response
if response.status_code == 200:
      json = response.json()
      if len(json) > 0:
          for address in json:

              addresses.append(address["summaryline"])
      else:
          print("No results")
else:
      print(f"Request error: {response.content.decode()}")


#select address
selectAddress = st.selectbox(
'Select Address:',
(addresses))

#advanced search 



with st.container():
  st.write("Advanced search:")

  

#column splitting checbox and features 
  col1, col2 = st.columns(2)
#holds checkbox toggle switch 
  with col2:
           advancedSearch= st.checkbox("Enable advanced search ?", key="disabled")

#hold features of advanced search 
  with col1:
    if advancedSearch == False:       #if checkbox is false #features disabled as advanced search is not powered on 
      bedrooms = st.slider('Please select number of bedrooms:',1,30,disabled=True)
      bathrooms = st.slider('Please select number of bathrooms:',0,10,disabled=True)
      sqft= st.text_input('Please enter square footage:', disabled=True)
      correctSqft=True

    if advancedSearch: #if checkbox is true #features enabled as advanced search is powered on
      bedrooms = st.slider('Please select number of bedrooms:',1,30,)
      bathrooms = st.slider('Please select number of bathrooms:',0,10)
      sqft= st.text_input('Please enter square footage:')
      # check if square footage is above 25 
      correctSqft= False
      if sqft and int(sqft) > 25:
        correctSqft = True
      if sqft and int(sqft) < 25: 
        st.error("Please enter a square footage above 25")







































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
