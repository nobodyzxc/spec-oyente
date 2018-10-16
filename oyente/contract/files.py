import csv

with open('contract.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
  for row in rows:
    f = open(row[0] + ".sol", "w")
    f.write(row[1])
