
import pytest
from ALGORITHMS_HW1 import visitors

#тестирование при всех верных входных данных
def test_data_withs_all_dates_correct():
    file = 'data_correct.csv'
    expected = 'Список дней недели с продажами выше или равными средним: понедельник, вторник, суббота, воскресенье\nСписок месяцев с продажами выше или равными средним: январь\nСписок дней недели с продажами ниже средних: среда, четверг, пятница\nСписок месяцев с продажами ниже средних: февраль'
    result = visitors.search_days_and_months_withs_max_sales_withs_high_speed_algorithm(file)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

#тестирование исключения в названии расширения имени файла
def test_data_not_correct_extension_file_name():
    file = 'data_not_correct_extension_file_name.txt'
    with pytest.raises(NameError):
        visitors.search_days_and_months_withs_max_sales_withs_high_speed_algorithm(file)

#тестировани исключения на несуществующий файл
def test_data_not_exist_file():
    file = 'trpr.csv'
    with pytest.raises(FileNotFoundError):
        visitors.search_days_and_months_withs_max_sales_withs_high_speed_algorithm(file)

#тестирование исключения на неверный формат даты
def test_data_withs_uncorrect_format_date():
    file = 'data_not_correct_date.csv'
    with pytest.raises(ValueError):
        visitors.search_days_and_months_withs_max_sales_withs_high_speed_algorithm(file)

#тестирвание исключения на неверную длину обрабатываемой строки файла
def test_not_correct_len_str():
    file = 'data_not_correct_len_str.csv'
    with pytest.raises(ValueError):
        visitors.search_days_and_months_withs_max_sales_withs_high_speed_algorithm(file)

#тестирование исключения на неверный тип данных о кол_ве продаж
def test_not_correct_type_sales():
    file = 'data_not_correct_type_sales.csv'
    with pytest.raises(TypeError):
        visitors.search_days_and_months_withs_max_sales_withs_high_speed_algorithm(file)


