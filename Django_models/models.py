from typing import Any
from django.db import models
from django.contrib.auth import get_user_model


class User(models.Model):
    get_user_model()

# Поле title (Заголовок) типа CharField с максимальной длиной
# 100 символов.
# • Поле description (Описание) типа TextField.
# • Поле status (Статус) типа BooleanField со значением по
# умолчанию False.
# • Поле created_at (Дата создания) типа DateTimeField с
# автоматическим

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return Task

# Поле name (Название проекта) типа CharField с максимальной
# длиной 100 символов.
# • Поле description (Описание проекта) типа TextField. •
# Поле start_date (Дата начала проекта) типа DateField. •
# Поле end_date (Дата окончания проекта) типа DateField.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

# Модель Comment (Комментарий):
# • Поле task (Задача) типа ForeignKey, связано с моделью Task. •
# Поле user (Пользователь) типа ForeignKey, связано с моделью
# User.
# • Поле content (Содержание комментария) типа TextField. •
# Поле created_at (Дата создания комментария) типа
# DateTimeField с автоматическим добавлением значения при
# создании записи.

class Comment(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.task,self.user
    