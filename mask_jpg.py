from convertPDF import identify_areas, mask_areas

import fitz
from PIL import Image
import cv2
import numpy as np
import os

import argparse

import time

def mask_pdf(pdf_path, output_dir=".\\output", file_suffix="_masked", print_details=False, mask_names=True, mask_numbers=True):
    processed_images = []

    with fitz.open(pdf_path) as pdf:
        for pg in range(0, pdf.page_count):
            page = pdf[pg]
            mat = fitz.Matrix(2, 2)
            pm = page.get_pixmap(matrix=mat, alpha=False)
            if pm.width > 2000 or pm.height > 2000:
                pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)

            img = Image.frombytes("RGB", [pm.width, pm.height], pm.samples)
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            
            img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            
            if print_details:
                print(f"Processing page {pg+1}")

            # Pass image data directly to convertPDF
            regions = identify_areas(np.array(img_pil), print_details=print_details, mask_names=mask_names, mask_numbers=mask_numbers)
            
            if print_details:
                print(regions)

            processed_img = mask_areas(regions, img_pil)
            processed_images.append(processed_img)

    if processed_images:
        output_pdf_path = os.path.join(output_dir, os.path.splitext(os.path.basename(pdf_path))[0] + file_suffix + ".pdf")
        processed_images[0].save(output_pdf_path, save_all=True, append_images=processed_images[1:])
        if print_details:
            print(f"PDF saved as {output_pdf_path}")

def main(input_dir, output_dir, file_suffix, print_details, mask_names, mask_numbers):
    start_time = time.time()

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, file_name)
            mask_pdf(pdf_path, output_dir, file_suffix, print_details, mask_names, mask_numbers)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mask sensitive information in PDFs.")
    parser.add_argument("--input_dir", default=".\input", help="Directory containing input PDF files.")
    parser.add_argument("--output_dir", default=".\output", help="Directory to save output masked images.")
    parser.add_argument("--file_suffix", default="", help="Custom suffix for masked pdf files.")
    parser.add_argument("--print_details", type=bool, default=False, help="Display filenames, names, and masked regions while working. True/False")
    parser.add_argument("--mask_names", type=bool, default=True, help="Whether to mask identified names in the PDF. Set to True to enable masking, or False to disable.")
    parser.add_argument("--mask_numbers", type=bool, default=True, help="Whether to mask identified numbers in the PDF. Set to True to enable masking, or False to disable.")

    args = parser.parse_args()

    main(args.input_dir, args.output_dir, args.file_suffix, args.print_details, args.mask_names, args.mask_numbers)
