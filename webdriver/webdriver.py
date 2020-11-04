from selenium import webdriver


class WebDriver:
    driver = None

    def get(self):
        if self.driver is None:
            self.driver = webdriver.Chrome(executable_path='C:/Users/Tetiana_Haiuk/PycharmProjects/pythonProject/webdriver/chromedriver.exe')
            return self.driver