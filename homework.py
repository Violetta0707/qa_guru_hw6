from selene import browser, have
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_fill_practice_form():
    options = Options()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Настройка Selene
    browser.set_driver(driver)

    browser().open('https://demoqa.com/automation-practice-form')

    browser().element('#firstName').type('Виолетта')
    browser().element('#lastName').type('Новикова')
    browser().element('#userEmail').type('violetta.novikova@example.com')
    browser().element('[for="gender-radio-2"]').click()
    browser().element('#userNumber').type('9111234567')

    browser().element('#dateOfBirthInput').click()
    browser().element('.react-datepicker__month-select').select('July')
    browser().element('.react-datepicker__year-select').select('2002')
    browser().element('.react-datepicker__day--001:not(.react-datepicker__day--outside-month)').click()

    browser().element('#subjectsInput').type('English').press_enter()
    browser().element('[for="hobbies-checkbox-3"]').click()
    browser().element('#uploadPicture').send_keys('resources/avatar.png')
    browser().element('#currentAddress').type('г. Санкт-Петербург, ул. Ленина, д. 5')

    browser().element('#state').click()
    browser().element('#react-select-3-option-1').click()
    browser().element('#city').click()
    browser().element('#react-select-4-option-1').click()

    browser().element('#submit').click()

    browser().element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser().all('tbody tr').should(have.texts(
        'Виолетта Новикова',
        'violetta.novikova@example.com',
        'Female',
        '9111234567',
        '01 July,2002',
        'English',
        'Music',
        'avatar.png',
        'г. Санкт-Петербург, ул. Ленина, д. 5',
        'Uttar Pradesh Lucknow'
    ))

    browser().quit()



