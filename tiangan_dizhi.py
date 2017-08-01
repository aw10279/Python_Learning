# -*- coding: utf-8 -*-

tiangan = '甲乙丙丁戊己庚辛壬癸'
dizhi = '子丑寅卯辰巳午未申酉戌亥'

jiazi = [tiangan[x % len(tiangan)] + dizhi[x % len(dizhi)] for x in range(60)]   #巧用%取余数的功能在最小公倍数60范围内遍历所有组合

print(jiazi)