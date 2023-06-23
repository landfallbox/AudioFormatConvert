# AudioFormatConvert
## 项目描述

基于 Python 实现音频文件格式转换。

## 运行环境

项目运行所需环境已在 requirements.txt 中给出，以下是一些补充内容：

项目借助 pydub 实现音频文件格式转换，而 pydub 依赖于 FFmpeg 实现相关功能，故运行项目前应当保证本地已经安装了 FFmpeg 并将其添加到环境变量中。

## 技术栈

Python：3.10

## 已实现功能

FLAC => MP3

OGG => MP3

## 使用方法

项目的代码实现在 convert.py 中，通过修改 input_folder 指定要转换的文件所在的文件目录，通过修改 output_folder 指定转换后文件输出到哪个文件目录，之后运行脚本即可。

## 代实现功能

MFLAC => MP3

MGG => MP3

·······

## 参考资料

1. [Windows 10系统下安装FFmpeg教程详解_ffmpeg window10_SLASH-YONG的博客-CSDN博客](https://blog.csdn.net/qq_43803367/article/details/110308401)



