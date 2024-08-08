from paddleocr import PaddleOCR, draw_ocr
from paddleocr import PPStructure,draw_structure_result,save_structure_res

import hanlp
hanlp.pretrained.mtl.ALL

from PIL import Image, ImageDraw
import os
# load HanLp model
HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)

# HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)
# load Paddleocr model
ocr = PaddleOCR(use_angle_cls=True, lang="ch", page_num=0, show_log=False)  # need to run only once to download and load model into memory

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
# white list
if os.path.exists("./whitelist.txt"):
    with open("./whitelist.txt", "r", encoding="utf-8") as file:
        read_whitelist = file.read().split(',')
else:
    read_whitelist = []
# print(read_whitelist)

def convertPDF(image, whitelist=read_whitelist, print_details=False):
    result = ocr.ocr(image, cls=True)

    txt_coords = {}
    name_coords = []
    for idx in range(len(result)):
        res = result[idx]
        boxes = [line[0] for line in res]
        txts = [line[1][0] for line in res]
        for i, txt in enumerate(txts):
            txt_coords[txt] = boxes[i]
            ner_result = HanLP([txt], tasks='ner*')
            for name in ner_result['ner/pku'][0]:
                if (name[1] == 'nr' and name[0] not in whitelist):
                    if print_details:
                        print(name, 'person')
                    name_coords.append(txt_coords[txt])

    return name_coords

def getAllboxes(img_path):
    result = ocr.ocr(img_path, cls=True)

    for idx in range(len(result)):
        res = result[idx]
        # image = imgs[idx]
        boxes = [line[0] for line in res]
        txts = [line[1][0] for line in res]

    return boxes, txts

def mask_name(name_coords, img):
    coords = [[(region[0][0], region[0][1]), (region[1][0], region[1][1]), (region[2][0], region[2][1]), (region[3][0], region[3][1])] for region in name_coords]

    for coord in coords:
        mosaic = Image.new("RGB", img.size, color="black")
        draw = ImageDraw.Draw(mosaic)
        draw.polygon(coord, fill="white")
        mask = mosaic.convert('1')
        img.paste(mosaic, mask=mask)

    return img

# boxes, txts = getAllboxes(img_path)
# for i in range(len(boxes)):
#     print(boxes[i], txts[i])
