#!/usr/bin/env python3
"""
刪除 weapon 資料夾中的 PNG 檔案（在確認 WebP 檔案存在的情況下）
"""

import os
import time

def safe_delete_png_files(weapon_dir):
    """
    安全地刪除 PNG 檔案，但只在對應的 WebP 檔案存在時才刪除
    
    Args:
        weapon_dir (str): weapon 資料夾路徑
    """
    
    if not os.path.exists(weapon_dir):
        print(f"❌ 錯誤：目錄 {weapon_dir} 不存在")
        return False
    
    # 獲取所有 PNG 檔案
    png_files = [f for f in os.listdir(weapon_dir) if f.lower().endswith('.png')]
    
    if not png_files:
        print(f"✅ 在 {weapon_dir} 中沒有找到 PNG 檔案")
        return True
    
    print(f"📁 檢查目錄: {weapon_dir}")
    print(f"🔍 找到 {len(png_files)} 個 PNG 檔案")
    print("-" * 50)
    
    deleted_count = 0
    skipped_count = 0
    total_space_saved = 0
    
    for i, png_file in enumerate(png_files, 1):
        try:
            png_path = os.path.join(weapon_dir, png_file)
            webp_file = os.path.splitext(png_file)[0] + '.webp'
            webp_path = os.path.join(weapon_dir, webp_file)
            
            # 檢查對應的 WebP 檔案是否存在
            if os.path.exists(webp_path):
                # 獲取 PNG 檔案大小
                png_size = os.path.getsize(png_path)
                total_space_saved += png_size
                
                # 刪除 PNG 檔案
                os.remove(png_path)
                
                print(f"[{i:3d}/{len(png_files):3d}] ✅ 已刪除: {png_file} ({png_size:,} bytes)")
                deleted_count += 1
                
            else:
                print(f"[{i:3d}/{len(png_files):3d}] ⚠️  跳過: {png_file} (對應的 WebP 檔案不存在)")
                skipped_count += 1
                
        except Exception as e:
            print(f"[{i:3d}/{len(png_files):3d}] ❌ 刪除失敗 {png_file}: {str(e)}")
            skipped_count += 1
        
        # 短暫延遲
        time.sleep(0.05)
    
    # 總結報告
    print("-" * 50)
    print("📈 刪除完成統計:")
    print(f"✅ 成功刪除: {deleted_count} 個 PNG 檔案")
    print(f"⚠️  跳過檔案: {skipped_count} 個")
    
    if deleted_count > 0:
        print(f"💾 釋放空間: {total_space_saved:,} bytes ({total_space_saved/1024/1024:.2f} MB)")
    
    return deleted_count > 0

def main():
    """主函數"""
    print("🗑️  PNG 檔案清理工具")
    print("=" * 50)
    
    # weapon 圖片目錄
    weapon_dir = os.path.join("website", "docs", "resources", "img", "weapon")
    
    if not os.path.exists(weapon_dir):
        print(f"❌ 錯誤：weapon 目錄不存在: {weapon_dir}")
        return
    
    # 安全確認
    print("⚠️  警告：此操作將刪除所有對應 WebP 檔案存在的 PNG 檔案")
    print("請確保：")
    print("1. WebP 檔案已正確生成並可正常使用")
    print("2. Markdown 檔案中的圖片連結已更新為 .webp")
    print("3. 網站測試正常，圖片顯示無問題")
    print()
    
    # 在真實環境中可以加入用戶確認
    # response = input("是否繼續刪除 PNG 檔案？(y/N): ")
    # if response.lower() != 'y':
    #     print("❌ 操作已取消")
    #     return
    
    print("🚀 開始清理 PNG 檔案...")
    print()
    
    # 開始刪除
    success = safe_delete_png_files(weapon_dir)
    
    if success:
        print("\n🎉 PNG 檔案清理完成！")
        print("\n💡 建議：")
        print("   - 測試網站確保所有 WebP 圖片正常顯示")
        print("   - 如有問題，可以重新下載 PNG 檔案")
    else:
        print("\n✅ 沒有需要清理的檔案")

if __name__ == "__main__":
    main()
