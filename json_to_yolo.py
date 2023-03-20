import json
import os

def convert(img_size, box):
    x1_center = box[0] + (box[2]-box[0]) / 2.0
    y1_center = box[1] + (box[3]-box[1]) / 2.0
    
    w_1 = box[2] - box[0]
    h_1 = box[3] - box[1]
    
    x1_normal = x1_center / img_size[0]
    y1_normal = y1_center / img_size[1]
    
    w_1_normal = w_1 / img_size[0]
    y_1_normal = h_1 / img_size[1]
    
    return (x1_normal, y1_normal, w_1_normal, y_1_normal)


def decode_json(json_floder_path, json_name):
    txt_name = 'F:\code\json_to_yolo\severe/' + json_name.split('.')[0] + '.txt'
    txt_file = open(txt_name, 'w')

    json_path = os.path.join(json_floder_path, json_name)
    data = json.load(open(json_path, 'r'))

    img_w = data['imageWidth']
    img_h = data['imageHeight']

    for i in data['shapes']:

        if (i['shape_type'] == 'rectangle' and (i['label'] == '3' or i['label'] == '1' or i['label'] == '2'or i['label'] == 'mild'or i['label'] == 'general'or i['label'] == 'severe')):
            x1 = float(i['points'][0][0])
            y1 = float(i['points'][0][1])
            x2 = float(i['points'][1][0])
            y2 = float(i['points'][1][1])
            print(x1)
            print(y1)
            print(x2)
            print(y2)
            print(img_w)
            print(img_h)

            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write( '0' + " " + " ".join([str(i) for i in bbox]) + '\n')


if __name__ == "__main__":

    json_floder_path = r'F:\datasets\反流yolo数据集\severe'  #改成自己的json文件存储路径
    json_names = os.listdir(json_floder_path)
    for json_name in json_names:
        decode_json(json_floder_path, json_name)


