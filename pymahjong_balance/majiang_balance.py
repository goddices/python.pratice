import re
import sys
file1 = open(sys.path[0]+"/majiang_balance.txt", "r")
file2 = open(sys.path[0]+"/majiang_balance_out.txt", "w")
players = {'朱': 0, '秦': 0, "盛": 0, "路": 0}
lines = file1.readlines()
for r in range(len(lines)):
    detail = lines[r].replace('\n', '').replace("朱峰", '朱').replace("路女", "路")
    digits = re.findall(r"\d+\.?\d*", detail)
    if (len(digits)) != 0:
        winner = ""
        loser = ""
        digit = digits[0]
        dig_index = detail.index(digit)
        is_chong = "输" in detail
        is_zimo = "自摸" in detail
        if is_chong:
            verb_index = detail.index("输")
            winner = detail[verb_index+1: dig_index]
            loser = detail[0:verb_index]
            players[winner] = players[winner] + int(digit)
            players[loser] = players[loser] - int(digit)
        elif is_zimo:
            verb_index = detail.index("自摸")
            winner = detail[0:verb_index]
            players[winner] = players[winner] + 3 * int(digit)
            for key in players:
                if key != winner:
                    # 自摸时，其他玩家都输钱
                    players[key] = players[key] - int(digit)

        # check
        num = int(digit)
        out_row =""
        if(is_chong):
            out_row= format("朱,%d,秦,%d,盛,%d,路,%d" % (
                num if '朱' == winner else -1*num if '朱' == loser else 0,  
                num if '秦' == winner else -1*num if '秦' == loser else 0, 
                num if '盛' == winner else -1*num if '盛' == loser else 0, 
                num if '路' == winner else -1*num if '路' == loser else 0))
        elif is_zimo:
            out_row = format("朱,%d,秦,%d,盛,%d,路,%d" % (
                3* num if '朱' == winner else -1*num, 
                3* num if '秦' == winner else -1*num, 
                3* num if '盛' == winner else -1*num,
                3* num if '路' == winner else -1*num))
        print(out_row)
        file2.write(out_row+'\n')
print(players)
file1.close()
file2.close()
