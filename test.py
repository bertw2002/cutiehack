#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import sys
import json
import cv2

def detect_labels(photo):

    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    
    data = {
        'source': photo,
        'data': response.get('Labels')
    }
    
    return json.dumps(data, indent=4)

    # print('Detected labels for ' + photo) 
    # print()   
    # for label in response['Labels']:
    #     print ("Label: " + label['Name'])
    #     print ("Confidence: " + str(label['Confidence']))
    #     print ("Instances:")
    #     for instance in label['Instances']:
    #         print ("  Bounding box")
    #         print ("    Top: " + str(instance['BoundingBox']['Top']))
    #         print ("    Left: " + str(instance['BoundingBox']['Left']))
    #         print ("    Width: " +  str(instance['BoundingBox']['Width']))
    #         print ("    Height: " +  str(instance['BoundingBox']['Height']))
    #         print ("  Confidence: " + str(instance['Confidence']))
    #         print()

    #     print ("Parents:")
    #     for parent in label['Parents']:
    #         print ("   " + parent['Name'])
    #     print ("----------")
    #     print ()
    # return len(response['Labels'])


def main():
    # script = sys.argv[0]
    
    if len(sys.argv) <= 1:
        print('please supply photo')
        
    photo = sys.argv[1]
    print(detect_labels(photo))
    # photo=''
    # bucket=''
    # label_count=detect_labels(photo, bucket)
    # print("Labels detected: " + str(label_count))

def remove_background(img, threshold):
    """
    This method removes background from your image
    
    :param img: cv2 image
    :type img: np.array
    :param threshold: threshold value for cv2.threshold
    :type threshold: float
    :return: RGBA image
    :rtype: np.ndarray
    """
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshed = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

    cnts = cv2.findContours(morphed, 
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[0]

    cnt = sorted(cnts, key=cv2.contourArea)[-1]

    mask = cv2.drawContours(threshed, cnt, 0, (0, 255, 0), 0)
    masked_data = cv2.bitwise_and(img, img, mask=mask)

    x, y, w, h = cv2.boundingRect(cnt)
    dst = masked_data[y: y + h, x: x + w]

    dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(dst_gray, 0, 255, cv2.THRESH_BINARY)
    b, g, r = cv2.split(dst)

    rgba = [r, g, b, alpha]
    dst = cv2.merge(rgba, 4)

    return dst


if __name__ == "__main__":
    main()


