import streamlit as st

# 创建文件上传器
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # 读取文件内容
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # 如果是文本文件，可以解码成字符串
    if uploaded_file.type == "text/plain":
        string_data = bytes_data.decode('utf-8')
        st.write(string_data)
