def calculate_salary(achievement_rate, store_count, incentive_scheme):

    if store_count == 7 and incentive_scheme == "新":
        if achievement_rate < 85:
            return 4600 + 2000 + 280 + 450 + 300
        elif 85 <= achievement_rate < 90:
            return 4600 + 2400 + 280 + 450 + 400
        elif 90 <= achievement_rate < 95:
            return 4600 + 2900 + 280 + 450 + 500
        elif 95 <= achievement_rate < 100:
            return 4600 + 3400 + 280 + 450 + 550
        elif 100 <= achievement_rate < 115:
            return 4600 + 3800 + 280 + 450 + 600
        elif achievement_rate >= 115:
            return 4600 + 4200 + 280 + 450 + 600
    elif store_count == 7 and incentive_scheme == "旧":
        if achievement_rate < 85:
            return 4600 + 2000 + 280 + 450 + 200
        elif 85 <= achievement_rate < 90:
            return 4600 + 2400 + 280 + 450 + 300
        elif 90 <= achievement_rate < 95:
            return 4600 + 2900 + 280 + 450 + 350
        elif 95 <= achievement_rate < 100:
            return 4600 + 3400 + 280 + 450 + 450
        elif 100 <= achievement_rate < 115:
            return 4600 + 3800 + 280 + 450 + 600
        elif achievement_rate >= 115:
            return 4600 + 4200 + 280 + 450 + 600
    elif store_count == 10 and incentive_scheme == "无":
        if achievement_rate < 85:
            return 4600 + 2400 + 400 + 450
        elif 85 <= achievement_rate < 90:
            return 4600 + 2800 + 400 + 450
        elif 90 <= achievement_rate < 95:
            return 4600 + 3300 + 400 + 450
        elif 95 <= achievement_rate < 100:
            return 4600 + 3800 + 400 + 450
        elif 100 <= achievement_rate < 115:
            return 4600 + 4200 + 400 + 450
        elif achievement_rate >= 115:
            return 4600 + 4600 + 400 + 450

achievement_rates = [92.19, 73.69, 62.11, 128.22, 87.42, 79.58, 95.21, 89.17, 112.43, 97.31, 109.79, 97.42, 90.19]
# salaries = [7193, 6465, 5988, 10665, 6812, 5374, 5872, 5914, 6299]

total_new_salary = 0
average_salary = 0

for i in range(len(achievement_rates)):
    achievement_rate = achievement_rates[i]
    print(achievement_rate,"完成率")
    store_count = 7  # 假设管店数量为7
    incentive_scheme = "新"  # 假设激励方案为新
    salary = calculate_salary(achievement_rate, store_count, incentive_scheme)
    print(salary,"工资")
    total_new_salary += salary

average_salary = total_new_salary / len(achievement_rates)

print("一共薪资：", total_new_salary)
print("平均薪资：", average_salary)


