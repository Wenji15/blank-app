import streamlit as st
from chardet import detect
import json

def read_json(file_path):
    # try:
    with open(file_path, 'rb') as file:
        file_content = file.read()
        encoding = detect(file_content)['encoding']

        # 如果检测失败，默认使用 utf-8
        if not encoding:
            encoding = 'utf-8'

        content = file_content.decode(encoding)
        data = json.loads(content)
        return data

st.set_page_config(page_title="数据后处理过程演示", layout="wide")
config_file_path = st.text_input('输入配置文件路径', help='json', )
if st.button("读取配置文件"):
    json_file = read_json(config_file_path)
    st.write(json_file)
