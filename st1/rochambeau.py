#!/usr/bin/python
#coding:utf-8
import random
guess_list = ["石头","剪刀","布"]
win_combination = [["布","石头"],["石头","剪刀"],["剪刀","布"]]
while True:
    computer = random.choice(guess_list)
    people = raw_input('请输入：石头,剪刀,布\n').strip()
    if people not in guess_list:
        people = raw_input('重新输入：石头,剪刀,步,\n').strip()
        continue
    if computer == people:
        print "computer guess:",computer
        print "you guess:",people
        print "平手，再玩一次！"
    elif [computer,people] in win_combination:
        print "computer guess:",computer
        print "you guess:",people
        print "电脑获胜！"
    else:
        print "computer guess:",computer
        print "you guess:",people
        print "恭喜你获胜了"
        break