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
    
    search_input.clear()

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
    query = input("Please press Enter after write the keyword \nwrite your keyword : ")
    driver = setup_driver()

    while True:
        if query.lower() == 'quit':
            print("Goodbye!")
            driver.quit()
            break

        search_places(driver, query)
        time.sleep(5)



    # query = "restaurants in Dhaka"


        business_cards = scroll_and_collect(driver, max_scroll= 10)
        print(f"Result found: {len(business_cards)} businesses")


        all_data = []
        for card in business_cards:
            data = extract_business_data(card)
            if data:
                all_data.append(data)

        filename = f"{query.replace(' ', '_')}.csv"
        save_to_excel(all_data, filename=filename)
        print(f"scraping Done. save to : {filename}")

        query = input("\n next keyword: ")
 




if __name__ == "__main__":
    main()

