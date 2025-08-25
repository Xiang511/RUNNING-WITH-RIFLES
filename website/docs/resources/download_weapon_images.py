#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
武器圖片下載器
從 HTML 表格中提取圖片 URL 並下載到本地
"""

import re
import os
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time

def extract_image_urls_from_html(html_content):
    """從 HTML 內容中提取所有圖片 URL"""
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = []
    
    # 尋找所有圖片標籤
    img_tags = soup.find_all('img')
    
    for img in img_tags:
        src = img.get('src', '')
        data_src = img.get('data-src', '')
        data_image_name = img.get('data-image-name', '')
        
        # 優先使用 data-src（延遲載入），如果沒有則使用 src
        url = data_src or src
        
        # 跳過基64編碼的占位符圖片
        if url and 'data:image/gif;base64' in url:
            continue
        
        if url and 'wikia.nocookie.net' in url:
            # 提取檔案名
            if data_image_name:
                filename = data_image_name.replace(' ', '_')
            else:
                # 從 URL 提取檔案名
                parsed_url = urlparse(url)
                filename = os.path.basename(parsed_url.path).split('?')[0]
            
            if filename and not filename.startswith('.'):
                image_urls.append((url, filename))
                print(f"找到圖片: {filename} -> {url}")
    
    # 去除重複的圖片
    unique_images = {}
    for url, filename in image_urls:
        if filename not in unique_images:
            unique_images[filename] = url
    
    # 返回 (url, filename) 元組列表
    return [(url, filename) for filename, url in unique_images.items()]

def download_image(url, filename, output_dir):
    """下載單張圖片"""
    try:
        # 確保檔案名有副檔名
        if not os.path.splitext(filename)[1]:
            filename += '.png'
        
        file_path = os.path.join(output_dir, filename)
        
        # 如果檔案已存在，跳過
        if os.path.exists(file_path):
            print(f"跳過已存在的檔案: {filename}")
            return True
        
        print(f"正在下載: {url}")
        
        # 設定請求標頭
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # 寫入檔案
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ 下載完成: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ 下載失敗 {url}: {e}")
        return False

def main():
    # 使用完整路徑
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "test.md")
    output_dir = os.path.join(script_dir, "img", "weapon")
    
    print(f"正在讀取檔案: {input_file}")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        print("正在提取圖片 URL...")
        image_urls = extract_image_urls_from_html(html_content)
        
        if not image_urls:
            print("未找到任何圖片 URL")
            return
        
        print(f"找到 {len(image_urls)} 張圖片")
        
        # 確保輸出目錄存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 下載所有圖片
        success_count = 0
        for i, (url, filename) in enumerate(image_urls, 1):
            print(f"\n[{i}/{len(image_urls)}] ", end="")
            if download_image(url, filename, output_dir):
                success_count += 1
            
            # 添加延遲避免過於頻繁的請求
            time.sleep(0.5)
        
        print(f"\n\n下載完成！")
        print(f"成功下載: {success_count}/{len(image_urls)} 張圖片")
        print(f"檔案保存在: {output_dir}")
        
    except Exception as e:
        print(f"處理過程中發生錯誤: {e}")

if __name__ == "__main__":
    main()
