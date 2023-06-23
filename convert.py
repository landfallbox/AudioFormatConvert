"""
 @Author: SheepDog
 @Email: landfallbox@gmail.com
 @FileName: convert.py
 @DateTime: 2023/6/23 023 13:37
 @SoftWare: PyCharm
"""

import os
import glob
from pydub import AudioSegment

# 输入文件夹和输出文件夹路径
input_folder = ''
output_folder = ''

# 获取输入文件夹中的所有FLAC、OGG、MFLAC和MGG文件
flac_files = glob.glob(os.path.join(input_folder, '*.flac'))
ogg_files = glob.glob(os.path.join(input_folder, '*.ogg'))

# 遍历FLAC文件并进行转换
for flac_file in flac_files:
    # 构建输出文件路径
    filename = os.path.basename(flac_file)
    output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.mp3')

    print('Converting {} to {}'.format(flac_file, output_file))

    # 执行转换
    audio = AudioSegment.from_file(flac_file, format='flac')
    audio.export(output_file, format='mp3')

# 遍历OGG文件并进行转换
for ogg_file in ogg_files:
    # 构建输出文件路径
    filename = os.path.basename(ogg_file)
    output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.mp3')

    print('Converting {} to {}'.format(ogg_file, output_file))

    # 执行转换
    audio = AudioSegment.from_file(ogg_file, format='ogg')
    audio.export(output_file, format='mp3')

print('Conversion complete!')
