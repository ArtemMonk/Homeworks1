#Пользователь вводит время в секундах. Переведите время в часы,
#минуты, секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

print("Введите любое количество секунд, \nи я их переведу в более приемлемый и удобный вид.")
sec = int(input("Количество секунд = "))
minute = sec//60
hour = minute//60
minute = minute%60
sec = sec%60
print("В переводе на человеческий вид это получается:")
print(hour, ":", minute, ':', sec)