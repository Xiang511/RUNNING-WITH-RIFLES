#!/usr/bin/env python3
"""
將 weapon 資料夾中的 PNG 圖片轉換為 WebP 格式
"""

import os
import sys
from PIL import Image
import time

def convert_png_to_webp(input_dir, quality=80):
    """
    將指定目錄中的所有 PNG 圖片轉換為 WebP 格式
    
    Args:
        input_dir (str): 輸入目錄路徑
        quality (int): WebP 壓縮品質 (1-100，預設80)
    """
    
    if not os.path.exists(input_dir):
        print(f"❌ 錯誤：目錄 {input_dir} 不存在")
        return
    
    # 獲取所有 PNG 檔案
    png_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.png')]
    
    if not png_files:
        print(f"❌ 在 {input_dir} 中沒有找到 PNG 檔案")
        return
    
    print(f"📁 處理目錄: {input_dir}")
    print(f"🔍 找到 {len(png_files)} 個 PNG 檔案")
    print(f"🎛️ WebP 品質設定: {quality}")
    print("-" * 50)
    
    success_count = 0
    error_count = 0
    total_original_size = 0
    total_webp_size = 0
    
    for i, png_file in enumerate(png_files, 1):
        try:
            # 檔案路徑
            png_path = os.path.join(input_dir, png_file)
            webp_file = os.path.splitext(png_file)[0] + '.webp'
            webp_path = os.path.join(input_dir, webp_file)
            
            # 獲取原始檔案大小
            original_size = os.path.getsize(png_path)
            total_original_size += original_size
            
            # 開啟並轉換圖片
            with Image.open(png_path) as img:
                # 如果是 RGBA 模式，轉換為 RGB（WebP 支援透明度，但可以選擇）
                if img.mode == 'RGBA':
                    # 保持透明度
                    img.save(webp_path, 'WEBP', quality=quality, lossless=False)
                else:
                    img.save(webp_path, 'WEBP', quality=quality)
            
            # 獲取轉換後檔案大小
            webp_size = os.path.getsize(webp_path)
            total_webp_size += webp_size
            
            # 計算壓縮率
            compression_ratio = (1 - webp_size / original_size) * 100
            
            print(f"[{i:3d}/{len(png_files):3d}] ✅ {png_file}")
            print(f"        📊 {original_size:,} bytes → {webp_size:,} bytes (-{compression_ratio:.1f}%)")
            
            success_count += 1
            
        except Exception as e:
            print(f"[{i:3d}/{len(png_files):3d}] ❌ 轉換失敗 {png_file}: {str(e)}")
            error_count += 1
        
        # 短暫延遲，避免系統負載過高
        time.sleep(0.1)
    
    # 總結報告
    print("-" * 50)
    print("📈 轉換完成統計:")
    print(f"✅ 成功轉換: {success_count} 個檔案")
    print(f"❌ 轉換失敗: {error_count} 個檔案")
    
    if success_count > 0:
        total_compression = (1 - total_webp_size / total_original_size) * 100
        print(f"📦 原始總大小: {total_original_size:,} bytes ({total_original_size/1024/1024:.2f} MB)")
        print(f"📦 WebP 總大小: {total_webp_size:,} bytes ({total_webp_size/1024/1024:.2f} MB)")
        print(f"🎯 總壓縮率: {total_compression:.1f}%")
        print(f"💾 節省空間: {total_original_size - total_webp_size:,} bytes ({(total_original_size - total_webp_size)/1024/1024:.2f} MB)")

def main():
    """主函數"""
    # weapon 圖片目錄
    weapon_dir = os.path.join("website", "docs", "resources", "img", "weapon")
    
    print("🚀 PNG 到 WebP 轉換工具")
    print("=" * 50)
    
    # 檢查目錄是否存在
    if not os.path.exists(weapon_dir):
        print(f"❌ 錯誤：weapon 目錄不存在: {weapon_dir}")
        return
    
    # 開始轉換
    convert_png_to_webp(weapon_dir, quality=85)  # 使用較高品質
    
    print("\n🎉 轉換程序完成！")
    print("\n💡 提示：")
    print("   - WebP 檔案已建立，原始 PNG 檔案仍保留")
    print("   - 如要刪除 PNG 檔案，請手動確認 WebP 檔案正常後再執行")
    print("   - 記得更新 Markdown 檔案中的圖片連結為 .webp 副檔名")

if __name__ == "__main__":
    main()
