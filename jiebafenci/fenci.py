# encoding=utf-8
import jieba
import pandas as pd
import logging
import csv

logging.getLogger().setLevel(logging.INFO)



# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(" ".join(seg_list))
#
# df = pd.read_csv("huifu.csv")
#
# logging.info(df.columns.tolist())
# logging.info(df.shape)
# logging.info(df.loc[3:7])



# for x in range(len(df.loc)):
#     logging.info(df.loc[x])

csvFile = open("fencied.csv", 'w')
writer = csv.writer(csvFile)
writer.writerow(["回复内容"])

with open("huifu.csv") as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        # logging.info(row[0])
        seg_list = jieba.cut(row[0])
        # logging(seg_list)
        str = " ".join(seg_list)
        print([str])
        writer.writerow([str])

csvFile.close()