from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

data = [
    ['最新产品', '每日', '优惠', '20', '%'],  # 5
    ['淘宝', '刷单', '信用', '工资', '日结'],  # 5
    ['明天', '来', '我', '办公室', '一趟'],  # 5
    ['今天的', '报告', '发到', '我', '邮箱'],  # 5
    ['今天', '我们', '去', '哪里', '吃'],  # 5
    ['信用卡', '分期', '优惠', '利率', '点击'],  # 5
    ['这家', '餐厅', '很好吃', '价格', '优惠']  # 5
]
total_words = 35
for row in  data:

# Y = [
#     [1], [1], [0], [0], [0], [1], [0]
# ]
# model = gnb.fit(X, Y)
# test_X1 = ['今天', '去哪里', '吃']
# test_Y1 = model.predict(test)
# print(test_Y1)
# test_X2 = ['淘宝', '链接', '发一下']
# test_Y2 = model.predict(test)
# print(test_Y2)
# test_X3 = ['明天', '发起会议', '邀请']
# test_Y3 = model.predict(test)
# print(test_Y3)
