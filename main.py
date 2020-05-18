# Ну что, удачи нам.
class Hotel:
    """Этот класс позволяет работать с каждым клиентом, подающим заявку на бронирование"""

    def __init__(self, date_booking, last_name, first_name, middle_name, number_ppl,  date_in, number_of_days, max_sum):
        """Метод, создающий экземпялр класса"""
        self.date_booking = date_booking
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.number_ppl = number_ppl
        self.date_in = date_in
        self.number_of_days = number_of_days
        self.max_sum = max_sum





with open("booking.txt", "r", encoding="utf-8") as r:
    txt = r.readlines()


for i in txt:        #Создаёт экземпляр класса
    i = i.split()    #Одна строка файла booking.txt = 1 экземпляру
    print(i)
    c = Hotel(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])

    
#Саша-начало (удалить перед отправкой кода)

with open('fund.txt', 'r', encoding='utf-8') as f:
    lst = f.readlines()

dohod = 0
lost_dohod = 0


lst_1 = []
for i in lst:
    ls = 0
    t = i.split()
    if t[1] == 'одноместный':
        ls += 2900
    elif t[1] == 'двухместный':
        ls += 2300
    elif t[1] == 'полулюкс':
        ls += 3200
    else:
        ls += 4100
    if t[3] == 'стандарт':
        ls *= 1
    elif t[3] == 'стандарт_улучшенный':
        ls *= 1.2
    else:
        ls *= 1.5
    t.append(str(ls))
    lst_1.append(t)
print(lst_1)

count_people = 1        #мои конкретные числа, которые в примере Минака
days = 3                #в задаче нужно вместо этих чисел брать из файла txt
max_cons = 5400         #потом удалить эти комментарии

lst_2 = []
skidka = 1
for j in lst_1:
    if j[2] == str(count_people):
        if float(j[4]) <= max_cons:
            lst_2.append(j)

if lst_2 == []:
    skidka = 0.7
    for j in lst_1:
        if j[2] > str(count_people):
            if float(j[4]) <= max_cons:
                lst_2.append(j)


spisok = []

for i in lst_2:
    spisok.append(float(i[4]) * skidka)

r = len(spisok)
for k in range(r):
    spisok.append(spisok[k] + 280)

for t in range(r):
    spisok.append(spisok[t] + 1000)

for i in range(3*r):
    q = max(spisok)
    if q > max_cons:
        c = spisok.index(q)
        spisok.remove(q)
        spisok.insert(c, 0)

prib = max(spisok)
c = spisok.index(prib)
number = lst_2[c % r][0]            #номер занимаемой комнаты
type_number = lst_2[c % r][3]       #комфортность номера
if c // r == 0:
    eating = 'Без питания'
elif c // r == 1:
    eating = 'Завтрак'              #тип питания
else:
    eating = 'Полупансион'

print(number)
print(type_number)

answer = input('Клиент согласен? ').lower()

if answer == 'да':
    dohod += prib
else:
    lost_dohod = lost_dohod + max_cons * days

#Саша-конец( (удалить перед отправкой кода)
