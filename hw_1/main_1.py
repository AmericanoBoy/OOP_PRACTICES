
#Задание №1
#----------------

class Animal:
    def __init__(self, name:str, type:str, age:int):
        self.name = name
        self.type = type
        self.age = age

    def voice_animal(self, voice):
        print(voice)

    def info_animal(self):
        print(f'{self.name} это {self.type} , ему {self.age} лет.')

dog = Animal('Трезор', 'собака', 5 )
dog.info_animal()
dog.voice_animal(input('Он говорит :  '))

#_______________________________________________________________________________

#Задание №2
#-----------------

class Book:
    def __init__(self, title: str, author: str, number_of_pages: int):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages

    def open_book(self, page: int):
        if page > self.number_of_pages:
            print( f'КНИГА НЕ МОЖЕТ БЫТЬ ОТКРЫТА НА УКАЗАННОЙ СТРАНИЦЕ. В КНИГЕ {self.number_of_pages} СТРАНИЦ!')
            return
        print(f'Книга открыта на {page} странице.')

    def current_object_status(self):
        print(f'Название книги: {self.title}. Автор книги: {self.author}. Колличесто страниц: {self.number_of_pages}')


book = Book('Капитал', 'Карл Маркс', 500)
book.open_book(int(input('На какой странице открыть книгу:   ')))
book.current_object_status()

#_____________________________________________________________________________

#Задание №3
#-----------------

class Passenger_Plane:
    def __init__(self, manufacturer:str, model:str, capacity:int, current_height:int, current_speed:int):
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.current_height = current_height
        self.current_speed = current_speed

    def height_change(self, new_height):
        fall = 'ОПАСНОЕ ИЗМЕНЕНИЕ ВЫСОТЫ ВОЗМОЖНО СТОЛКНОВЕНИЕ С ЗЕМЛЕЙ.'
        if new_height < 0:
            print(fall)
            return
        self.current_height = new_height
        print(f'САМОЛЕТ НАХОДИТСЯ НА ЭШЕЛОНЕ: {self.current_height}')

    def take_of_plan(self):
        if self.current_height != 0:
            print('САМОЛЕТ ВЗЛЕТЕЛ')

    def landing_plane(self):
        if self.current_height == 0:
            print('САМОЛЕТ ПРИЗЕМЛИЛСЯ')

    def change_speed(self, new_speed):
        fall = 'СЛИШКОМ МАЛАЯ СКОРОСТЬ. ВОЗМОЖНО СВАЛИВАНИЕ.'
        if self.current_height > 0:
            if new_speed < 380:
                print(fall)
                return
        self.current_speed = new_speed
        print(f'СКОРОСТЬ: {self.current_speed}')

    def  current_object_status(self):
        print(f'Марка самолета: {self.manufacturer}. Модель самолета: {self.model}. Эшелон: {self.current_height}. Скорость: {self.current_speed}.       ')

plan = Passenger_Plane('ТУ','154', 180, 100, 690)
plan.current_object_status()
plan.landing_plane()
plan.take_of_plan()
plan.height_change(int(input('ЗАДАЙТЕ САМОЛЕТУ НОВУЮ ВЫСОТУ:  ')))
plan.change_speed(int(input('ЗАДАЙТЕ САМОЛЕТУ НОВУЮ СКОРОСТЬ: ')))
plan.landing_plane()
plan.take_of_plan()
plan.current_object_status()

#________________________________________________________________________________________________________

#Задание №4
#-----------------

class Music_Album:
    def __init__(self, artist:str, album_name:str, genre:str, lst_songs:list):
        self.artist = artist
        self.album_name = album_name
        self.genre = genre
        self.lst_songs = lst_songs

    def add_song(self, new_song):
        if new_song in self.lst_songs:
            print('ЭТА ПЕСНЯ УЖЕ ЕСТЬ В АЛЬБОМЕ!')
            return
        self.lst_songs.append(new_song)

    def remove_song(self, song):
        if song not in self.lst_songs:
            print('ЭТОЙ ПЕСНИ НЕТ В АЛЬБОМЕ!')
            return
        self.lst_songs.remove(song)

    def song_playback(self, song):
        if song not in self.lst_songs:
            print('ЭТОЙ ПЕСНИ НЕТ В АЛЬБОМЕ!')
            return
        print(f'Проиходит воспроиведение песни {song}')


    def current_object_status(self):
        print(f'Исполнитель: {self.artist}. Название албома: {self.album_name}. Жанр: {self.genre}. Список треков: {self.lst_songs}.')


album = Music_Album('Ах, как хочтся жить!','Пугачева', 'Эстрада', ['Арлекино', 'Старинные часы'])
album.current_object_status()
album.add_song(input('Добавьте новый трек в альбом:  '))
album.remove_song(input('Удалите трек из альбома: '))
album.song_playback(input('Воспроивести трек:  '))
album.current_object_status()