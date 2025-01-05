from django.contrib.auth.models import Group
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator
from django.db import models

from merchandising.models import Division

DAYS = {
    'Mon': 'Понедельник',
    'Tue': 'Вторник',
    'Wed': 'Среда',
    'Thu': 'Четверг',
    'Fri': 'Пятница',
    'Sat': 'Суббота',
    'Sun': 'Воскресенье',
}
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование должности')
    salary = models.FloatField(verbose_name='Оклад')
    description = models.CharField(max_length=1000, verbose_name='Описание должностных обязанностей')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class ReasonForAbsence(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название причины')
    description = models.CharField(max_length=1000, verbose_name='Описание причины')

    class Meta:
        verbose_name = 'Причина отсутствия'
        verbose_name_plural = 'Причины отсутствия'


class Employee(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    division = models.ForeignKey(Division, verbose_name='ID подразделения', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name='ID роли', on_delete=models.CASCADE)
    work_phone = models.IntegerField(validators=[MaxValueValidator(999999999999999)], verbose_name='Рабочий телефон')
    personal_phone = models.IntegerField(validators=[MaxValueValidator(999999999999999)], verbose_name='Личный телефон')
    email = models.CharField(max_length=50, verbose_name='Электронная почта')
    inn = models.IntegerField(validators=[MaxValueValidator(999999999999)], verbose_name='ИНН')
    snils = models.IntegerField(validators=[MaxValueValidator(99999999999)], verbose_name='СНИЛС')
    date_of_employment = models.DateTimeField(verbose_name='Дата приёма на работу')
    date_of_medical = models.DateTimeField(verbose_name='Дата прохождения медосмотра')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Passport(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='ID сотрудника')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    gender = models.CharField(max_length=1, choices={'M': 'Мужчина', 'W': 'Женщина'}, verbose_name='Пол')
    seriya = models.IntegerField(validators=[MaxValueValidator(9999)], verbose_name='Серия')
    number = models.IntegerField(validators=[MaxValueValidator(999999)], verbose_name='Номер')
    department_code = models.IntegerField(validators=[MaxValueValidator(99999999)], verbose_name='Код подразделения выдачи')
    registration_address = models.CharField(max_length=150, verbose_name='Адрес прописки')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')

    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'


class ForeignPassport(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='ID сотрудника')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    gender = models.CharField(max_length=1, choices={'M': 'Мужчина', 'W': 'Женщина'}, verbose_name='Пол')
    number = models.IntegerField(validators=[MaxValueValidator(999999999)], verbose_name='Номер')
    department_code = models.IntegerField(validators=[MaxValueValidator(99999999)],
                                          verbose_name='Код подразделения выдачи')
    citizenship = models.CharField(max_length=50, verbose_name='Гражданство')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    date_of_expiration = models.DateField(verbose_name='Дата окончания действия')

    class Meta:
        verbose_name = 'Иностранный паспорт'
        verbose_name_plural = 'Иностранные паспорта'


class MilitaryCard(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='ID сотрудника')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    military_office_address = models.CharField(max_length=150, verbose_name='Адрес военкомата')
    place_of_birth = models.CharField(max_length=150, verbose_name='Место рождения')
    education = models.CharField(max_length=150, verbose_name='Образование')
    category = models.CharField(max_length=2, verbose_name='Категория')

    class Meta:
        verbose_name = 'Военное удостоверение'
        verbose_name_plural = 'Военные удостоверения'


class EmployeeSchedule(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='ID сотрудника')
    days_of_presence = ArrayField(models.CharField(max_length=3, choices=DAYS, verbose_name='Дни присутствия'))
    time_start = models.TimeField(verbose_name='Время начала смены')
    time_end = models.TimeField(verbose_name='Время окончания смены')

    class Meta:
        verbose_name = 'Расписание работника'
        verbose_name_plural = 'Расписания работников'
