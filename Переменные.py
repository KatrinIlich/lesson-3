# Переменные
number_homework = 12  # Количество выполненных домашних заданий
time = 1.5  # Количество затраченных часов
course_name = "Python"  # Название курса
# Вычисление времени на одно задание
time_for_one_task = time / number_homework
#Вывод результата
print (f"Курс: {course_name}, "
      f"всего заданий: {number_homework}, "
      f"затрачено часов: {time:.2f}, "
      f"среднее время на задание: {time_for_one_task:.3f} часа")