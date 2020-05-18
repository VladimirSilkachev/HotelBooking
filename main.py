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
