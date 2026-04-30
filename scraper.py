from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re
import time

def setup_driver():
    driver = webdriver.Chrome ()
    driver.get("https://www.google.com/maps/?hl=en")
    return driver


def search_places(driver, query):
    search_input = driver.find_element(By.XPATH, "//input[@name = 'q']")
    search_input.send_keys(query)
    search_input.send_keys(Keys.ENTER)
    time.sleep(5)

def scroll_and_collect (driver, max_scroll = 10):
    wait = WebDriverWait(driver, 20)
    scrollable = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='feed']")))
    scroll_cout = 0
    while True:
        driver.execute_script("arguments[0].scrollTop += 1000",scrollable)
        time.sleep(5)
        scroll_cout += 1
        business_cards = driver.find_elements(By.XPATH, "//div[@role = 'article']")
        
            

        
        if scroll_cout >= max_scroll:
            print("Cant Scroll any more")
            break

    return business_cards


def extract_business_data(card):
    try:
        card_text = card.text.split('\n')

        # for i, line in enumerate(card_text):
        #     print(f"Line {i}: {line}")
        # print("---")


        name = card_text[0] if len(card_text) > 0 else "N/A"
        rating = card_text[1].split('(')[0] if len(card_text) > 1 else "N/A"
        address= card_text[2] if len(card_text) > 2 else "N/A"
        # parts = address.split('\u00b7')
        raw_address = re.sub(r'^.*·\s*', '', address).strip()


        return{
            "Name" : name,
            "Rating" : rating,
            "Address" : raw_address

        }

    except Exception as e:
        return None


def save_to_excel(all_data, filename ="google_map_resullt.csv"):
    df = pd.DataFrame(all_data)
    # df['Address'] = df['Address'].str.split('·').str[-1].str.strip()
    df.to_csv(filename, index=False)


def main():
    driver = setup_driver()

    query = "restaurants in Dhaka"
    search_places(driver, query)

    time.sleep(5)

    business_cards = scroll_and_collect(driver, max_scroll= 10)
    print(f"Result found: {len(business_cards)} businesses")


    all_data = []
    for card in business_cards:
        data = extract_business_data(card)
        if data:
            all_data.append(data)

    save_to_excel(all_data, filename="google_map_resullt.csv")

    driver.quit()
    print(f"{len(all_data)} businesses saved!")


if __name__ == "__main__":
    main()



#     #     try:
#     #         business_name = itme.find_element(By.XPATH, ".//a[@aria-label]").get_attribute("aria-label")
#     #         business_rating = itme.find_element(By.XPATH, ".//span[@class='MW4etd']").text
#     #         business_review = itme.find_element(By.XPATH, ".//span[@class='UY7F9']").text
#     #         business_address = itme.find_element(By.XPATH, ".//div[@class='W4Efsd']/div[@class='W4Efsd']/span[3]/span").text
            
#     #         time.sleep(3)

#     #         print(f"Name: {business_name}, Rating: {business_rating}, address: {business_address}")

#     #     except Exception as e:
#     #         print(f"Error: {e}")
#     #         continue


#     time.sleep(3)
#     driver.quit()