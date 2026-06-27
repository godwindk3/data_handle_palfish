import pandas as pd

files = {
    "file1": "./raw_data/PalFish - Chatpage 2026 - Trực page T05_2026.csv",
    "file2": "./raw_data/PalFish - Chatpage 2026 - Trực page T04_2026.csv",
    "file3": "./raw_data/PalFish - Chatpage 2026 - Trực page T03_2026.csv",
    "file4": "./raw_data/PalFish - Chatpage 2026 - Trực page T02_2026.csv",
    "file5": "./raw_data/PalFish - Chatpage 2026 - Trực page T01_2026.csv",
}

columns = {}

for name, path in files.items():
    df = pd.read_csv(path, nrows=0)   # Chỉ đọc header
    columns[name] = set(df.columns)

# Tập hợp tất cả các cột
all_columns = set.union(*columns.values())

print(f"Tổng số cột khác nhau: {len(all_columns)}\n")

for name in files:
    missing = all_columns - columns[name]
    extra = columns[name] - (all_columns - missing)

    print("=" * 60)
    print(name)
    print(f"Số cột: {len(columns[name])}")

    if missing:
        print("\nThiếu:")
        for col in sorted(missing):
            print("-", col)
    else:
        print("\nKhông thiếu cột.")

for name, path in files.items():
    df = pd.read_csv(path, nrows=0)

    print("="*60)
    print(name)

    for col in df.columns:
        print(repr(col))
