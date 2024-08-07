from convertPDF import mask_name, convertPDF

import fitz
from PIL import Image
import cv2
import numpy as np
import os

import argparse

import time
start_time = time.time()

def mask_pdf(pdf_path=".\\input", output_dir=".\\output", print_details=False):

    # imgs = []
    # turn pdf into jpg
    with fitz.open(pdf_path) as pdf:
        img_dir = os.path.join(output_dir, 'jpg')
        if not os.path.exists(img_dir):
            os.mkdir(img_dir)
        output_dir = os.path.join(output_dir, 'masked')
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        for pg in range(0, pdf.page_count):
            page = pdf[pg]
            mat = fitz.Matrix(2, 2)
            pm = page.get_pixmap(matrix=mat, alpha=False)
            # if width or height > 2000 pixels, don't enlarge the image
            if pm.width > 2000 or pm.height > 2000:
                pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)

            img = Image.frombytes("RGB", [pm.width, pm.height], pm.samples)
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            
            img_path = os.path.join(img_dir, f"page{pg+1}.jpg")
            # Save the image to the output directory
            if print_details:
                print(img_path)
            cv2.imwrite(img_path, img)
            # imgs.append(img_path)
            regions = convertPDF(img_path, print_details=print_details)
            # print boxes
            if print_details:
                print(regions)

            output_path = os.path.join(output_dir, f"page{pg+1}_masked.jpg")
            mask_name(regions, img_path, output_path)


def main(input_dir, output_dir, print_details):
    start_time = time.time()

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, file_name)
            file_output_dir = os.path.join(output_dir, os.path.splitext(file_name)[0])
            if not os.path.exists(file_output_dir):
                os.makedirs(file_output_dir)
            mask_pdf(pdf_path, file_output_dir, print_details)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mask sensitive information in PDFs.")
    parser.add_argument("--input_dir", default=".\input", help="Directory containing input PDF files.")
    parser.add_argument("--output_dir", default=".\output", help="Directory to save output masked images.")
    parser.add_argument("--print_details", type=bool, default=False, help="Display filenames, names, and masked regions while working. True/False")
    args = parser.parse_args()

    main(args.input_dir, args.output_dir, args.print_details)
from convertPDF import mask_name, convertPDF

import fitz
from PIL import Image
import cv2
import numpy as np
import os

import argparse

import time
start_time = time.time()

def mask_pdf(pdf_path=".\\input", output_dir=".\\output", print_details=False):

    # imgs = []
    # turn pdf into jpg
    with fitz.open(pdf_path) as pdf:
        img_dir = os.path.join(output_dir, 'jpg')
        if not os.path.exists(img_dir):
            os.mkdir(img_dir)
        output_dir = os.path.join(output_dir, 'masked')
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        for pg in range(0, pdf.page_count):
            page = pdf[pg]
            mat = fitz.Matrix(2, 2)
            pm = page.get_pixmap(matrix=mat, alpha=False)
            # if width or height > 2000 pixels, don't enlarge the image
            if pm.width > 2000 or pm.height > 2000:
                pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)

            img = Image.frombytes("RGB", [pm.width, pm.height], pm.samples)
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            
            img_path = os.path.join(img_dir, f"page{pg+1}.jpg")
            # Save the image to the output directory
            if print_details:
                print(img_path)
            cv2.imwrite(img_path, img)
            # imgs.append(img_path)
            regions = convertPDF(img_path, print_details=print_details)
            # print boxes
            if print_details:
                print(regions)

            output_path = os.path.join(output_dir, f"page{pg+1}_masked.jpg")
            mask_name(regions, img_path, output_path)


def main(input_dir, output_dir, print_details):
    start_time = time.time()

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, file_name)
            file_output_dir = os.path.join(output_dir, os.path.splitext(file_name)[0])
            if not os.path.exists(file_output_dir):
                os.makedirs(file_output_dir)
            mask_pdf(pdf_path, file_output_dir, print_details)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mask sensitive information in PDFs.")
    parser.add_argument("--input_dir", default=".\input", help="Directory containing input PDF files.")
    parser.add_argument("--output_dir", default=".\output", help="Directory to save output masked images.")
    parser.add_argument("--print_details", type=bool, default=False, help="Display filenames, names, and masked regions while working. True/False")
    args = parser.parse_args()

    main(args.input_dir, args.output_dir, args.print_details)