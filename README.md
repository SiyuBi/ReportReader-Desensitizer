# ReportReader-Desensitizer

ReportReader-Desensitizer is a tool designed to mask sensitive information within PDF images. It utilizes PaddleOCR and HANLP to identify and redact sensitive text and numbers in the images generated from the PDF pages.


## Installation

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Clone the Repository

```sh
git clone https://github.com/SiyuBi/ReportReader-Desensitizer.git
cd ReportReader-Desensitizer
```

### Set Up Virtual Environment (Optional but Recommended)

```sh
python -m venv desensitize
source desensitize/bin/activate  # On Windows: desensitize\Scripts\activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
### Command-Line Interface
The tool can be run from the command line with the following arguments:
```sh
--input_dir: Directory containing input PDF files. Default is ./input.
--output_dir: Directory to save output masked images. Default is ./output.
--file_suffix: Custom suffix for masked pdf files. Default is none.
--mask_names: Whether to mask identified names in the PDF. Set to True to enable masking, or False to disable. Default is True.
--mask_numbers: Whether to mask identified numbers in the PDF. Set to True to enable masking, or False to disable. Default is True.
--print_details: Display filenames, names, and masked regions while working. Default is False.
```

### Example Command
```sh
python mask_jpg.py --input_dir ./input --output_dir ./output --file_suffix "_masked" --mask_names True --mask_numbers True --print_details True
```

### Whitelist

The file "whitelist.txt" allows specification of certain names or terms that should not be masked. To modify the whitelist, edit whitelist.txt directly using comma-separated strings.