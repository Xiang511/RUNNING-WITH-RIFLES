#!/usr/bin/env python3
"""
將 Markdown 檔案中的圖片連結從 PNG 格式更新為 WebP 格式
"""

import re
import os

def update_image_links_to_webp(file_path):
    """
    將 Markdown 檔案中的圖片連結從 .png 更新為 .webp
    
    Args:
        file_path (str): Markdown 檔案路徑
    """
    
    if not os.path.exists(file_path):
        print(f"❌ 錯誤：檔案 {file_path} 不存在")
        return False
    
    try:
        # 讀取檔案內容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 計算原始的 PNG 連結數量
        png_pattern = r'!\[([^\]]*\.png)\]\(([^)]*\.png)\)'
        png_matches = re.findall(png_pattern, content)
        original_png_count = len(png_matches)
        
        print(f"📁 處理檔案: {file_path}")
        print(f"🔍 找到 {original_png_count} 個 PNG 圖片連結")
        
        if original_png_count == 0:
            print("✅ 沒有需要更新的 PNG 連結")
            return True
        
        # 替換圖片連結：將 .png 改為 .webp
        # 處理 ![alt_text](path.png) 格式
        def replace_png_link(match):
            alt_text = match.group(1)
            image_path = match.group(2)
            
            # 將 alt_text 和 image_path 中的 .png 都改為 .webp
            new_alt_text = alt_text.replace('.png', '.webp')
            new_image_path = image_path.replace('.png', '.webp')
            
            return f'![{new_alt_text}]({new_image_path})'
        
        # 執行替換
        updated_content = re.sub(png_pattern, replace_png_link, content)
        
        # 檢查是否有變更
        if updated_content == content:
            print("✅ 沒有進行任何更改")
            return True
        
        # 計算更新後的連結數量
        webp_pattern = r'!\[([^\]]*\.webp)\]\(([^)]*\.webp)\)'
        webp_matches = re.findall(webp_pattern, updated_content)
        final_webp_count = len(webp_matches)
        
        # 備份原始檔案
        backup_path = file_path + '.backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"💾 建立備份檔案: {backup_path}")
        
        # 寫入更新後的內容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ 成功更新 {original_png_count} 個 PNG 連結為 WebP 格式")
        print(f"📊 最終 WebP 連結數量: {final_webp_count}")
        
        return True
        
    except Exception as e:
        print(f"❌ 處理檔案時發生錯誤: {str(e)}")
        return False

def main():
    """主函數"""
    print("🚀 PNG 到 WebP 連結更新工具")
    print("=" * 50)
    
    # 要處理的 Markdown 檔案
    markdown_file = "website/docs/resources/Weapons and equipment.mdx"
    
    if not os.path.exists(markdown_file):
        print(f"❌ 錯誤：Markdown 檔案不存在: {markdown_file}")
        return
    
    # 更新圖片連結
    success = update_image_links_to_webp(markdown_file)
    
    if success:
        print("\n🎉 連結更新完成！")
        print("\n💡 提示：")
        print("   - 原始檔案已備份為 .backup 檔案")
        print("   - 所有 PNG 圖片連結已更新為 WebP 格式")
        print("   - 請測試網站確保圖片正常顯示")
    else:
        print("\n❌ 連結更新失敗！")

if __name__ == "__main__":
    main()
