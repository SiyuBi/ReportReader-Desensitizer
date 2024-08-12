# ReportReader-Desensitizer

ReportReader-Desensitizer 是一个用于为 PDF 文件脱敏的工具，利用 PaddleOCR 和 HANLP 来识别并打码 PDF 页面中的人名和证件、电话号码（长串数字）。


## 安装

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

## 使用
### Command-Line Interface
该工具可以通过命令行运行，使用以下参数：
```sh
--input_dir: 输入 PDF 文件的目录。默认值为 ./input。
--output_dir: 保存输出打码后 PDF 文件的目录。默认值为 ./output。
--file_suffix: 输出 PDF 文件的自定义后缀。默认值为空。
--mask_names: 是否屏蔽 PDF 中识别出的名称。设置为 True 以启用屏蔽，或设置为 False 以禁用屏蔽。默认值为 True。
--mask_numbers: 是否屏蔽 PDF 中识别出的数字。设置为 True 以启用屏蔽，或设置为 False 以禁用屏蔽。默认值为 True。
--print_details: 运行过程中显示文件名、名称和屏蔽区域。默认值为 False。
```

### Example Command
```sh
python mask_jpg.py --input_dir ./input --output_dir ./output --file_suffix "_masked" --mask_names True --mask_numbers True --print_details True
```

### Whitelist

文件 "whitelist.txt" 允许指定不应屏蔽的某些名称或术语。要修改白名单，请直接使用英文逗号分隔的字符串编辑 whitelist.txt 文件。