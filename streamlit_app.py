import os
import streamlit as st

# 获取环境变量
file_path = os.getenv('FILE_PATH')

if file_path:
    try:
        # 读取文件内容
        with open(file_path, 'r') as file:
            content = file.read()
        
        # 在Streamlit页面中显示内容
        st.write(content)
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.error("FILE_PATH environment variable not set")
