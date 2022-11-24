from Logic import *

def test_enter():
    try:
        full_puth = base.go_to_site('')
        allure.attach(driver.get_screenshot_as_png(), name='Скриншот страницы входа', attachment_type=AttachmentType.PNG)
        with allure.step(f'Запрос оправлен путь {full_puth}'):
            assert full_puth == None, f'Неверный ответ путь {full_puth}'
    except (Exception) as err:
        print(f'Error:   {err}')
        raise