import pandas as pd

# df = pd.read_csv("./raw_data/All File Thu Hiền - SM Hanoi.csv", encoding="utf-8")

# # Lọc dữ liệu
# filtered_df = df[
#     (df["Month of payment"].astype(str).str.strip() == "2026/5") &
#     (df["Type"].astype(str).str.strip() != "续费")
# ]

# # Xuất ra file CSV mới
# filtered_df.to_csv(
#     "./raw_data/SM Hanoi_filtered_2026_5.csv",
#     index=False,
#     encoding="utf-8-sig"   # Giữ tiếng Việt/tiếng Trung khi mở bằng Excel
# )

# print(f"Đã xuất {len(filtered_df)} dòng vào file filtered_2026_5.csv")



# # Đọc file
# df = pd.read_csv("./raw_data/All File Thu Hiền - HCM REV.csv", encoding="utf-8")

# # Lọc dữ liệu
# filtered_df = df[
#     (df["Month of payment"].astype(str).str.strip() == "2026/5") &
#     (~df["Type"].astype(str).str.strip().isin(["续费", "Resell"]))
# ]

# # Xuất ra file mới
# filtered_df.to_csv(
#     "./raw_data/HCM REV_filtered_2026_5.csv",
#     index=False,
#     encoding="utf-8-sig"
# )

# print(f"Đã xuất {len(filtered_df)} dòng.")



# Đọc 2 file
df1 = pd.read_csv("./raw_data/HCM REV_filtered_2026_5.csv", encoding="utf-8")
df2 = pd.read_csv("./raw_data/SM Hanoi_filtered_2026_5.csv", encoding="utf-8")

# Thêm cột TEAM cho df1
df1["TEAM"] = "HCM"

# Gộp theo hàng
merged = pd.concat([df1, df2], ignore_index=True)

# Xuất file
merged.to_csv(
    "./raw_data/SM_HN_HCM_REV_filtered_2026_5.csv",
    index=False,
    encoding="utf-8-sig"
)

print(merged.shape)