'''Проект HotelBooking,
    разработчики: Винников С. 35%, Попов К. 34%, Силкачев В. 30%'''
class Hotel:
    """Этот класс позволяет работать с каждым клиентом, подающим заявку на бронирование"""

    dohod = 0
    lost_dohod = 0

    def __init__(self, date_booking, last_name, first_name, middle_name, number_ppl,  date_in, number_of_days, max_sum):
        """Метод, создающий экземпляр класса"""
        self.date_booking = date_booking
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.number_ppl = number_ppl
        self.date_in = date_in
        self.number_of_days = number_of_days
        self.max_sum = max_sum

    def value(self):
        '''Метод, позволяющий доход отеля, а так же работает с каждой поступающей заявкой.'''
        with open("booking.txt", "r", encoding="utf-8") as r:
            txt = r.readlines()

        with open('fund.txt', 'r', encoding='utf-8') as f:
            lst = f.readlines()

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

        lst_2 = []
        skidka = 1
        for j in lst_1:
            if j[2] == str(self.number_ppl):
                if float(j[4]) <= int(self.max_sum):
                    lst_2.append(j)

        if lst_2 == []:
            skidka = 0.7
            for j in lst_1:
                if j[2] > str(self.number_ppl):
                    if float(j[4]) <= int(self.max_sum):
                        lst_2.append(j)

        spisok = []
        for i in lst_2:
            spisok.append(float(i[4]) * skidka)

        r = len(spisok)
        for k in range(r):
            spisok.append(spisok[k] + 280)

        for t in range(r):
            spisok.append(spisok[t] + 1000)

        for i in range(2 * r):
            q = max(spisok)
            if q > int(self.max_sum):
                c = spisok.index(q)
                spisok.remove(q)
                spisok.insert(c, 0)
        if len(spisok) == 0:
            prib = 0
        else:
            prib = max(spisok)
            c = spisok.index(prib)
            number = lst_2[c % r][0]       # номер занимаемой комнаты

            count_days = int(self.date_in.split('.')[0]) + int(self.date_in.split('.')[1]) + int(self.number_of_days)
            if int(number) == 0:           # Проверка, не занят ли выбранный программой номер.
                if d[int(number)] == 0:
                    d[int(number)] = count_days
                    pass
                else:
                    if count_days >= d[int(number)]:
                        d[int(number)] = 0
                    else:
                        d[int(number)] = 1
                        lst_2.remove(str([s % r][0]))

            type_number = lst_2[c % r][3]  # комфортность номера

            if c // r == 0:
                eating = 'Без питания'
            elif c // r == 1:
                eating = 'Завтрак'  # тип питания
            else:
                eating = 'Полупансион'
            answer = input('Клиент согласен? ').lower()

            if answer == 'да':
                Hotel.dohod += prib * int(self.number_of_days)
            else:
                Hotel.lost_dohod += int(self.max_sum) * int(self.number_of_days)

        if prib == 0 or answer != 'да':
            Hotel.lost_dohod += int(self.max_sum) * int(self.number_of_days)
            print("--------------------------------------------------------------------------------------\n"
                  ""
                  "Поступила заявка на бронирование:\n"
                  "", self.first_name, self.middle_name, self.max_sum, self.number_of_days,self.date_in,
                  '\n' "Заявка на бронирование отклонена\n"
                  "--------------------------------------------------------------------------------------")
        else:
            print("--------------------------------------------------------------------------------------\n"
                  ""
                  "Поступила заявка на бронирование:\n"
                  "", self.last_name, self.first_name, self.middle_name, self.max_sum, self.number_of_days,self.date_in,
                  '\n' "Найден: \n"
                  ""
                  "номер",number,'стоимость',prib,"\n",
                  "--------------------------------------------------------------------------------------")



with open("booking.txt", "r", encoding="utf-8") as r:
            txt = r.readlines()

for i in txt:  # Создаёт экземпляр класса
    i = i.split()  # Одна строка файла booking.txt = 1 экземпляру
    c = Hotel(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
    c.value()
print('Доход отеля: ',Hotel.dohod)
print('Неполученный доход: ',Hotel.lost_dohod)
