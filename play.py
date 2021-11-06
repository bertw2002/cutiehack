import numpy as np
import cv2
from test import remove_background
import json

# img = cv2.imread('threeitems.jpg' ,3)
# img = cv2.resize(img, (0,0), fx=0.25, fy=0.25) 

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # threshold input image as mask
# mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]
# # negate mask
# mask = 255 - mask



data = {"source":"bananas.jpg","data":[{"Name":"Banana","Confidence":99.91316986083984,"Instances":[{"BoundingBox":{"Width":0.8579597473144531,"Height":0.32362648844718933,"Left":0.07939571887254715,"Top":0.10965920984745026},"Confidence":99.91316986083984},{"BoundingBox":{"Width":0.8140386343002319,"Height":0.35132211446762085,"Left":0.08798880130052567,"Top":0.5643205642700195},"Confidence":99.89134216308594}],"Parents":[{"Name":"Fruit"},{"Name":"Plant"},{"Name":"Food"}]},{"Name":"Plant","Confidence":99.91316986083984,"Instances":[],"Parents":[]},{"Name":"Fruit","Confidence":99.91316986083984,"Instances":[],"Parents":[{"Name":"Plant"},{"Name":"Food"}]},{"Name":"Food","Confidence":99.91316986083984,"Instances":[],"Parents":[]},{"Name":"Bowl","Confidence":65.10478210449219,"Instances":[],"Parents":[]}]}
# for i in data['data']:
#     print(i)
#     print('\n')
#found = [{item['Name']: item} for item in data['data'] if len(item['Instances']) != 0]

# for i in found:
#     print(found)

# print(json.dumps(data, sort_keys=True, indent=4))

print(data[1]['Instances'])





