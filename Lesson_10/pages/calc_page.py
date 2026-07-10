import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    DELAY_TIME = (By.CSS_SELECTOR, "#delay")
    SEVEN_BTN = (By.XPATH, "//span[normalize-space()='7']")
    PLUS_BTN = (By.XPATH, "//span[normalize-space()='+']")
    EIGHT_BTN = (By.XPATH, "//span[normalize-space()='8']")
    EQUALLY_BTN = (By.XPATH, "//span[@class='btn btn-outline-warning']")
    SUM = (By.XPATH, "//div[@class='screen']")

    def __init__(self, driver) ->None:
        """
        Конструктор задает начальное значение параметра driver.
        
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Ввод нового времени задержки {new_delay_time}")
    def delay_input(self, new_delay_time: str) -> str:
        """
        Функция вводит новое время задержки вывода результата расчета в соответствии с заданной переменной (new_delay_time).

        :param delay: str — время задержки в секундах.
        """
        delay_time = self.driver.find_element(*self.DELAY_TIME)
        delay_time.clear()
        delay_time.send_keys(new_delay_time)

    @allure.step("Ввод выражения тестового выражения \"7+8\" и ожидание вывода ответа \"15\"")
    def calc_sum(self) -> None:
        """
        Функция вводит на калькуляторе выражение "7+8" и дожидается вывода ответа "15".

        :param button: str — текст на кнопке, которую нужно нажать.
        :param sum: str - сумма на дисплее калькулятора.
        """
        seven_btn = self.driver.find_element(*self.SEVEN_BTN)
        seven_btn.click()

        plus_btn = self.driver.find_element(*self.PLUS_BTN)
        plus_btn.click()

        eight_btn = self.driver.find_element(*self.EIGHT_BTN)
        eight_btn.click()

        equally_btn = self.driver.find_element(*self.EQUALLY_BTN)
        equally_btn.click()

        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.SUM, "15"))

    @allure.step("Возвращение расчетного значения для проверки")
    def calc_result(self) -> str:
        """
        Функция возвращает посчитанную в калькуляторе сумму "15".

        :param sum: str - сумма на дисплее калькулятора.
        """
        calc_sum = self.driver.find_element(*self.SUM)
        return calc_sum.text
