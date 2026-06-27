import pandas as pd

df = pd.read_csv('./raw_data/All File Thu Hiền - SM Hanoi.csv', encoding='utf-8')

# # Chuẩn hóa về string và loại bỏ khoảng trắng
# phone = df["Phone"].astype(str).str.strip()

# # Tính độ dài
# length = phone.str.len()

# # Thống kê
# print(length.value_counts().sort_index())
# print(df["Phone"].tail(20))
# print(df["Phone"].dtype)



uid = (
    df["UID"]
    .fillna("")
    .str.strip()
)

# Thống kê độ dài
length = uid.str.len()

print(length.value_counts().sort_index())