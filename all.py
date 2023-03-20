import os
import csv
import random
datestes='data/0702/datastes'

datasets_csv =open('data/category/0702_7_all/all_image/datasets_info.csv','w',newline='')
datasets_csv_writer = csv.writer(datasets_csv)
trian_csv=open('data/category/0702_7_all/all_image/train.csv','w',newline='')
trian_csv_writer = csv.writer(trian_csv)
test_csv=open('data/category/0702_7_all/all_image/test.csv','w',newline='')
test_csv_writer = csv.writer(test_csv)

datasets_csv_writer.writerow(
    ["view_name","view_id",
    "Total patients",
    "Total  images",
    "Patients in training set",
    "NImages in training set",
    "Patients in tests est",
    "Images in test set"])
print(
    ["view_name","view_id",
    "Total patients",
    "Total  images",
    "Patients in training set",
    "Images in training set",
    "Patients in tests est",
    "Images in test set"])
# info_dict={
#     0:"大动脉短轴切面",200
#     1:"二尖瓣水平短轴切面",30
#     2:"乳头肌水平短轴切面",12
#     3:"心尖水平短轴切面",12
#     4:"心尖四腔心切面",4
#     5:"左室长轴切面",10
#     6:"其他",10
# }
info_dict={
     0: "Short-axis view of the aorta",
     1: "Mitral valve horizontal short-axis view",
     2: "Short-axis section at the level of papillary muscle",
     3: "apical horizontal short-axis section",
     4: "Apical four-chamber view",
     5: "Long-axis view of the left ventricle",
     6: "Other",
}
# info_dict={
#      0: "Short-axis view of the aorta",
#      1: "Mitral valve horizontal short-axis view and Short-axis section at the level of papillary muscle",
#      2: "apical horizontal short-axis section",
#      3: "Apical four-chamber view",
#      4: "Long-axis view of the left ventricle",
# }
# suffle
# folder_num_dict={
#     0: 100,
#     1: 30,
#     2: 13,
#     3: 12,
#     4: 4,
#     5: 10,
# }
folder_num_dict={
    0: 1000,
    1: 1000,
    2: 1000,
    3: 1000,
    4: 1000,
    5: 1000,
    6: 1000,
}
if __name__ == "__main__":
    # Get the current working directory
    for path in os.listdir(datestes):
        if os.path.isdir(os.path.join(datestes, path)):
            # 视图的总地址
            view_path=os.path.join(datestes, path)
            # 视图的名称
            view_id=int(view_path.split('/')[-1])
            # 视图的名称
            # if view_id==1 or view_id==2:
            #     view_id=1
            # elif view_id==3:
            #     view_id=2
            # elif view_id==4:
            #     view_id=3
            # elif view_id==5:
            #     view_id=4
            view_name=info_dict[view_id]
            # 总患者数量
            view_num=len(os.listdir(view_path))
            # 训练集患者数量
            train_num_all=int(view_num*0.8)
            # train_num_all=0
            # train_num=0
            train_num=train_num_all
            # 测试集患者数量
            test_num_all=view_num-train_num_all
            test_num=test_num_all
            # 训练集图像数量
            train_img_num=0
            # 测试集图像数量
            test_img_num=0
            patient_paths=[os.path.join(view_path,patient_path).replace('\\','/') for patient_path in os.listdir(view_path)]
            patient_paths_dir=[]
            while(patient_paths):
                # 如果测试集中患者够了 就跳出循环
                if test_num==0:
                    break
                else:
                    patient_path=patient_paths[-1]
                    # 获取最后一个患者的路径
                    if patient_path.endswith('.jpg') or patient_path.endswith('.png'):
                        img_path=patient_path
                        # 删除该患者
                        patient_paths.pop()
                        # 测试集中患者数量减一
                        test_num-=1
                        # 测试集图像数量加一
                        test_img_num+=1
                        test_csv_writer.writerow([view_id,view_name,img_path])
                    else:
                        # 删除该患者
                        patient_paths_dir.append(patient_paths.pop())
            patient_paths.extend(patient_paths_dir)
            for patient_path in patient_paths:
                # 患者图像或者文件夹地址
                # 如果患者是一个文件夹 就划分为训练集里面去
                if os.path.isdir(patient_path):
                    # 训练集的患者地址 遍历该患者的所有图像
                    images=[]
                    for root, dirs, files in os.walk(patient_path):
                        for file in files:
                            # 图像的地址
                            if file.endswith('.jpg') or file.endswith('.png'):
                                images.append(os.path.join(root,file).replace('\\','/'))
                                # if num<folder_num_dict[view_id]:
                                #     img_path=os.path.join(root,file)
                                #     train_img_num+=1
                                #     # 写入训练集的csv文件
                                #     trian_csv_writer.writerow([view_id,view_name,img_path])
                                #     num+=1
                    # 随机打乱数据
                    random.shuffle(images)
                    for i in range(len(images)):
                        if i<folder_num_dict[view_id]:
                            img_path=images[i]
                            train_img_num+=1
                            # 写入训练集的csv文件
                            trian_csv_writer.writerow([view_id,view_name,img_path])
                    train_num-=1
                else:
                    if patient_path.endswith('.jpg') or patient_path.endswith('.png'):
                        # 测试集中患者数量减一
                        train_num-=1
                        # 测试集图像数量加一
                        train_img_num+=1
                        trian_csv_writer.writerow([view_id,view_name,patient_path])
            # datasets_csv_writer.writerow(["view_name","view_id","训练集患者数量","训练集图像数量","测试集患者数量","测试集图像数量","总患者数量","总图像数量"])
            print([view_name,view_id,view_num,train_img_num+test_img_num,train_num_all,train_img_num,test_num_all,test_img_num])
            datasets_csv_writer.writerow([view_name,view_id,view_num,train_img_num+test_img_num,train_num_all,train_img_num,test_num_all,test_img_num])
                # 写入测试集的csv文件
datasets_csv.close()
trian_csv.close()
test_csv.close()