import os
import json

def generate_index():
    # 设定你要扫描的子文件夹
    target_dir = 'books'
    
    # 获取目录下所有以 .pdf 结尾的文件名列表
    # 这一步等同于在本地直接读取文件系统
    if os.path.exists(target_dir):
        pdf_files = [f for f in os.listdir(target_dir) if f.endswith('.pdf')]
    else:
        pdf_files = []
        
    # 将获取到的文件名列表，写入一个名为 book_list.json 的文件中
    # ensure_ascii=False 确保中文字符正常保存，不被转码
    with open('book_list.json', 'w', encoding='utf-8') as f:
        json.dump(pdf_files, f, ensure_ascii=False)
        
    print(f"成功扫描到 {len(pdf_files)} 个 PDF 文件，已生成 book_list.json")

if __name__ == "__main__":
    generate_index()