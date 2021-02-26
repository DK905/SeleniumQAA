# Задание: запуск автотестов для разных языков интерфейса
# pytest -s --language=es test_items.py --tb=line -v
import time


def test_check_for_existence_button_add_to_basket(browser):
    # Тестовая ссылка
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    # В течении 5 секунд будет искаться элемент: это на случай долгой прогрузки сайта
    browser.implicitly_wait(5)
    # Открытие тестовой ссылки в браузере
    browser.get(link)

    # Закомментированная задержка для просмотра локали тестового сайта
    # time.sleep(10)

    # Найдём кнопки по CSS свойству кнопки .btn-add-to-basket
    # Ищутся кнопки, так как поиск одной кнопки возвращает NoSuchElementException при провале
    button_basket = browser.find_elements_by_css_selector('.btn-add-to-basket')

    # Заведомо провальный тест для отработки assert
    # button_basket = browser.find_elements_by_css_selector('BigRedButton')

    # Проверка существования кнопки: при любой ненулевой длине, будет True
    assert len(button_basket), 'Кнопка "добавить в корзину" не найдена'
