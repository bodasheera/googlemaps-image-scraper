from  selenium import webdriver
import time
import urllib.request


CHROME_DRIVER_PATH = "D:/Personal Projects/chromedriver.exe"
WEBSITE = "https://www.google.com/maps/place/Jungle+Wood+House+Home+Stay/@14.8304215,74.7775492,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOu8BI6DkzeBEfcacrljutkEPLEM-6rs3bpGjmp!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOu8BI6DkzeBEfcacrljutkEPLEM-6rs3bpGjmp%3Dw203-h152-k-no!7i2576!8i1932!4m10!3m9!1s0x3bbeb9e5186ff17d:0xe6fffd996626e42a!5m2!4m1!1i2!8m2!3d14.8304215!4d74.7775492!14m1!1BCgIgAQ?hl=en"

DATASET_DIRECTORY = "./Datasets/"


def get_driver():
    driver= webdriver.Chrome(executable_path= CHROME_DRIVER_PATH)
    driver.maximize_window()
    return driver


def load_website(driver):
    driver.get(WEBSITE)
    return driver
    

def scrape_images(driver):
    time.sleep(5)

    count = 0

    while True:
        time.sleep(5)
        images_webelements = driver.find_elements_by_xpath("//div[@class='gallery-image-low-res']/div")

        if count != 0 and len(images_webelements) == count:
            break

        min_index = count 
        max_index = len(images_webelements) 

        for index in range(min_index, max_index):
            image_webelement = images_webelements[index]
            driver.execute_script("arguments[0].scrollIntoView();", image_webelement)
            image_url = image_webelement.get_attribute('style').split('"')

            if len(image_url) == 3:
                image_url = image_url[1]
                filename = image_url.split('/')[-1]+ '.jpeg'
                urllib.request.urlretrieve(image_url , DATASET_DIRECTORY + filename)


            count = count + 1


driver = get_driver()
driver = load_website(driver)
data = scrape_images(driver)