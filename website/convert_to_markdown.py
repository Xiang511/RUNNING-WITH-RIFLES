#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML to Markdown Table Converter
將 HTML 表格轉換為 Markdown 格式
"""

import re
import os
from bs4 import BeautifulSoup
import html

def clean_text(text):
    """清理文字內容"""
    if not text:
        return ""
    
    # 移除多餘的空白和換行
    text = re.sub(r'\s+', ' ', text.strip())
    
    # 處理特殊字符
    text = html.unescape(text)
    
    # 移除一些不需要的標籤內容
    text = re.sub(r'</?[^>]+>', '', text)
    
    return text

def extract_image_from_cell(cell):
    """從表格單元格中提取圖片信息"""
    img_tags = cell.find_all('img')
    if img_tags:
        img = img_tags[0]
        src = img.get('data-src') or img.get('src', '')
        alt = img.get('data-image-name', '')
        if src and 'wikia.nocookie.net' in src:
            # 提取檔案名
            filename = alt.replace(' ', '_') if alt else src.split('/')[-1].split('?')[0]
            return f"![{filename}](./img/{filename})"
    return ""

def convert_html_table_to_markdown(html_content):
    """將 HTML 表格轉換為 Markdown"""
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    
    markdown_content = ""
    
    for table_idx, table in enumerate(tables):
        rows = table.find_all('tr')
        if not rows:
            continue
            
        # 處理表頭
        header_row = rows[0]
        headers = []
        for th in header_row.find_all(['th', 'td']):
            header_text = clean_text(th.get_text())
            headers.append(header_text)
        
        if not headers:
            continue
            
        # 創建 Markdown 表格
        markdown_content += "\n"
        if table_idx > 0:
            markdown_content += f"\n## 表格 {table_idx + 1}\n\n"
        
        # 表頭
        markdown_content += "| " + " | ".join(headers) + " |\n"
        markdown_content += "|" + "|".join([" --- " for _ in headers]) + "|\n"
        
        # 資料行
        for row in rows[1:]:
            cells = row.find_all(['td', 'th'])
            if len(cells) != len(headers):
                continue
                
            row_data = []
            for i, cell in enumerate(cells):
                if i == 0 and headers[0].lower() in ['image', 'img', '圖像', '圖片']:
                    # 第一欄是圖片
                    cell_content = extract_image_from_cell(cell)
                else:
                    cell_content = clean_text(cell.get_text())
                
                # 處理過長的內容
                if len(cell_content) > 100:
                    cell_content = cell_content[:97] + "..."
                
                # 處理 Markdown 特殊字符
                cell_content = cell_content.replace("|", "\\|")
                row_data.append(cell_content)
            
            markdown_content += "| " + " | ".join(row_data) + " |\n"
    
    return markdown_content

def main():
    input_file = "Weapons and equipment.md"
    output_file = "Weapons and equipment - Markdown.md"
    
    print(f"正在讀取檔案: {input_file}")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        print("正在轉換 HTML 表格為 Markdown...")
        markdown_content = convert_html_table_to_markdown(html_content)
        
        # 添加檔案頭部
        final_content = """# 武器和裝備

> 此檔案由 HTML 表格自動轉換為 Markdown 格式

""" + markdown_content
        
        print(f"正在寫入檔案: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"轉換完成！輸出檔案: {output_file}")
        
    except Exception as e:
        print(f"轉換過程中發生錯誤: {e}")

if __name__ == "__main__":
    main()
