
def month_to_season(n):
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    if int(n) in winter:
        return 'Зима'
    elif int(n) in spring:
        return 'Весна'
    elif int(n) in summer:
        return 'Лето'
    elif int(n) in autumn:
        return 'Осень'
    else:
        return 'Bug'


# print(month_to_season(111))

