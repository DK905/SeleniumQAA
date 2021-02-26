# Конфигурация тестов

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Функция обработчика опции
def pytest_addoption(parser):
    # Запрос значения параметра --user_language
    parser.addoption('--language', action='store', default='en',
                     help='Выберите языковую локаль: [en], [ru] и т.п')


# Фикстура открытия браузера - общая для всех вложенных уровней тестирования
@pytest.fixture(scope='function')
def browser(request):
    # Запрашиваем язык интерфейса
    language = request.config.getoption('language')
    # Инициализация самого браузера, либо ошибка при неправильном браузере
    print(f'\nЗапуск браузера с локалью {language} для тестов..')

    # Инициализация блока опций
    options = Options()
    # Устанавливаем смену языка интерфейса сайта на выбранный для теста
    # Проверка на правильность языка не установлена заданием, и исключена за избыточность

    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # Запуск браузера с выбранными параметрами опций
    browser = webdriver.Chrome(options=options)
    yield browser

    # Завершение работы с браузером
    print('\nВыход из браузера..')
    browser.quit()
