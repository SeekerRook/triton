from sys import argv
import json
from os  import system

system(f"wget {argv[1]}/triton-api")
with open('triton-api','r') as f:
    data = json.load(f)
    Gain = data['Gain_%']
    Val = data['Clear_Value (- 160 fee)']
    g = data['Gain']
system(f"curl -d \" Value : {Val} Gain : {g} ({Gain}%) \" ntfy.sh/seekerrook-triton")
   

system(f"rm ./triton-api*")
