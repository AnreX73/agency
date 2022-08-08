from django.db import models


# Тип объекта городской недвижимости
class InCityObjectType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип объекта')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип объекта'
        verbose_name_plural = 'Тип объекта'
        ordering = ['id']


# Район города
class InCityRegion(models.Model):
    title = models.CharField(max_length=100, verbose_name='Район города')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Район города'
        verbose_name_plural = 'Район города'
        ordering = ['id']


# Станция метро
class MetroStation(models.Model):
    title = models.CharField(max_length=100, verbose_name='Станция метро')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Станцию метро'
        verbose_name_plural = 'Станция метро'
        ordering = ['id']


# Количество комнат
class RoomAmount(models.Model):
    title = models.CharField(max_length=25, verbose_name='Количество комнат')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Количество комнат'
        verbose_name_plural = 'Количество комнат'
        ordering = ['id']


# Санузел
class BathroomType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип санузла')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип санузла'
        verbose_name_plural = 'Тип санузла'
        ordering = ['id']


# тип лифта
class ElevatorType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип лифта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип лифта'
        verbose_name_plural = 'Тип лифта'
        ordering = ['id']


# состояние объекта
class FlatState(models.Model):
    title = models.CharField(max_length=100, verbose_name='Состояние')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояние'
        ordering = ['id']


# тип стройматериалов
class ObjectConstruction(models.Model):
    title = models.CharField(max_length=100, verbose_name='тип стройматериалов')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тип стройматериалов'
        verbose_name_plural = 'тип стройматериалов'
        ordering = ['id']


# объект городской недвижимости
class InCityObject(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    price = models.CharField(max_length=255, verbose_name='Цена')
    is_for_sale = models.BooleanField(default=True, verbose_name='Продажа')
    is_for_rent = models.BooleanField(default=False, verbose_name='Аренда')
    is_hot = models.BooleanField(default=False, verbose_name='горячий вариант')
    object_type = models.ForeignKey(InCityObjectType, on_delete=models.PROTECT, verbose_name='тип объекта')
    object_adress = models.CharField(max_length=255, blank=True, verbose_name='адрес объекта')
    city_region = models.ForeignKey(InCityRegion, on_delete=models.PROTECT, verbose_name='район города')
    metro = models.ForeignKey(MetroStation, on_delete=models.PROTECT, verbose_name='станция метро')
    metro_distance = models.CharField(max_length=255, blank=True, verbose_name='расстояние до метро')
    rooms = models.ForeignKey(RoomAmount, on_delete=models.PROTECT, verbose_name='количество комнат')
    square = models.CharField(max_length=255, blank=True, verbose_name='площадь')
    kitchen = models.CharField(max_length=255, blank=True, verbose_name='площадь кухни')
    rooms_layout = models.CharField(max_length=255, blank=True, verbose_name='планировка')
    floor = models.CharField(max_length=25, blank=True, verbose_name='Этаж')
    bathroom = models.ForeignKey(BathroomType, on_delete=models.PROTECT, verbose_name='санузел')
    elevator = models.ForeignKey(ElevatorType, on_delete=models.PROTECT, verbose_name='лифт')
    state = models.ForeignKey(FlatState, on_delete=models.PROTECT, verbose_name='состояние')
    construction = models.ForeignKey(ObjectConstruction, on_delete=models.PROTECT, verbose_name='тип постройки')
    year = models.CharField(max_length=25, blank=True, verbose_name='Год постройки / Сдачи')
    content = models.TextField(blank=True, verbose_name='текстовое описание ')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')


# Тип объекта загородной недвижимости
class OutCityObjectType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип объекта')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип объекта'
        verbose_name_plural = 'Тип объекта'
        ordering = ['id']


# форма собственности
class TypeOfOwnership(models.Model):
    title = models.CharField(max_length=155, verbose_name='форма собственности')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'форму собственности'
        verbose_name_plural = 'форма собственности'
        ordering = ['id']


# электроснабжение
class Electricity(models.Model):
    title = models.CharField(max_length=25, verbose_name='Электроснабжение')
    note = models.CharField(max_length=255, blank=True, verbose_name='примечание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Электроснабжение'
        verbose_name_plural = 'Электроснабжение'
        ordering = ['id']


# вода
class Water(models.Model):
    title = models.CharField(max_length=25, verbose_name='Вода')
    note = models.CharField(max_length=255, blank=True, verbose_name='примечание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вода'
        verbose_name_plural = 'Вода'
        ordering = ['id']


# газ
class Gas(models.Model):
    title = models.CharField(max_length=25, verbose_name='Газ')
    note = models.CharField(max_length=255, blank=True, verbose_name='примечание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Газ'
        verbose_name_plural = 'Газ'
        ordering = ['id']


# посадки
class Landings(models.Model):
    title = models.CharField(max_length=25, verbose_name='Посадки')
    note = models.CharField(max_length=255, blank=True, verbose_name='примечание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Посадки'
        verbose_name_plural = 'Посадки'
        ordering = ['id']


# баня
class Bath(models.Model):
    title = models.CharField(max_length=25, verbose_name='Баня')
    note = models.CharField(max_length=255, blank=True, verbose_name='примечание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баня'
        verbose_name_plural = 'Баня'
        ordering = ['id']
