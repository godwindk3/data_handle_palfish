import pandas as pd

# Danh sách các file cần gộp
files = [
    
    "./raw_data/PalFish - Chatpage 2026 - Trực page T05_2026.csv",
    "./raw_data/PalFish - Chatpage 2026 - Trực page T04_2026.csv",
    "./raw_data/PalFish - Chatpage 2026 - Trực page T03_2026.csv",
    "./raw_data/PalFish - Chatpage 2026 - Trực page T02_2026.csv",
    "./raw_data/PalFish - Chatpage 2026 - Trực page T01_2026.csv",
]

# Các cột cần loại bỏ
DROP_COLUMNS = [
    "Unnamed: 0",
    "Unnamed: 25",
    "Unnamed: 28",
    "Unnamed: 29",
    "#VALUE!",
    "3",
    "`",
    "Khu Vực"
]

dfs = []

for file in files:
    print(f"Đang đọc: {file}")

    df = pd.read_csv(file, encoding="utf-8")

    # Xóa các cột không cần thiết
    df = df.drop(columns=DROP_COLUMNS, errors="ignore")

    dfs.append(df)

# Gộp tất cả các DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

print(f"\nTổng số dòng: {len(merged_df)}")
print(f"Tổng số cột: {len(merged_df.columns)}")

# Xuất file
merged_df.to_csv(
    "./raw_data/merged_leads.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Đã lưu file: ./cleaned_data/PalFish - Chatpage 2026 - Trực page T01-T05_2026.csv")