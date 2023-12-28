f = open("train.csv", "r")
a = f.readlines()
f.close()

summ = 0
male = 0
female = 0
s = []
for i in range(1, len(a)):
    s = a[i].strip().split(',')
if s[1] == '1' and s[5] == 'male':
    male += 1
if s[1] and s[5] == 'female':
    female += 1

summ = male + female
print("Общее кол-во выживших -", summ, '|', 'Кол-во выживших мужчин -', male, '|', 'Кол-во выживщих женщин -', female)