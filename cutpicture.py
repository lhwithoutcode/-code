

import os
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt	
import cv2 as cv	

jsonPath = "F:/datasets/fanliu2022-12-5/severe-json/"
jpgDirPath = "F:/datasets/fanliu2022-12-5/severe-jpg/"


jsonName = os.listdir(jsonPath)
#print(jsonName)
for json1 in jsonName:
 #   print(json1)
    trmp = '.'.join(json1.split(".")[:-1])
    #print(trmp)
    img = cv2.imread(jpgDirPath + trmp + ".jpg")
  #  print("img=",img)
    path = jsonPath +json1
   # print(path)

    j = 0
   
    with open(path, 'r', encoding='utf-8') as f:
        load_dict = json.load(f)
        dic_data = load_dict["shapes"]

        for i in dic_data:
            pts = np.array(i["points"])
            pts = pts.astype(np.int64)
            #print(pts)
            
            rect = cv2.boundingRect(pts)
            #print(rect)
            x, y, w, h = rect
            #print(x,y,w,h)
            croped = img[y:y + h, x:x + w].copy()
            croped = cv.cvtColor(croped,cv.COLOR_BGR2GRAY)
            # #print(croped.shape)
            # #plt.figure()
            # #plt.imshow(croped)
            # pts = pts - pts.min(axis=0)
            # #print(pts)
            # mask = np.zeros(croped.shape[:2], np.uint8)
            # # #print(mask.shape)
            # cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
            
            
            # dst = cv2.bitwise_and(croped, croped, mask=mask)
            # # #print(dst)
            # bg = np.ones_like(croped, np.uint8) * 255
            # cv2.bitwise_not(bg, bg, mask=mask)
            # dst2 = bg + dst

            #cv2.imwrite('test1.jpg',croped,[int(cv2.IMWRITE_JPEG_QUALITY),100])
            
            Save_File = "F:/datasets/fanliu2022-12-5/result/result/"
            Name_File = i['label']
            #print(Name_File)

            category = load_dict['imagePath']
            #print(category)
            #if "P" in category.split('.')[0] or "p" in category.split('.')[0]:
            trmp1 = '.'.join(category.split(".")[:-1])
            trmp2 ='.'.join(load_dict['imagePath'].split(".")[:-1])
            if "P" in trmp1 or "p" in trmp1:
                save_path = os.path.join(Save_File,Name_File+'/psave', trmp2 +"_"+str(j) + '.jpg')               
            else:
                save_path = os.path.join(Save_File, Name_File + '/',trmp2 + "_" + str(j) + '.jpg')
            print(save_path)

            if os.path.exists(Save_File + Name_File):
                cv2.imwrite(save_path, croped)
            else:
                os.makedirs(Save_File + Name_File + "/psave")
            j += 1

