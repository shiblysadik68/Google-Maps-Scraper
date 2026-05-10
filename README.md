# 📍 Google Maps Scraper

<div align="center">

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.15-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*Automatically extract business data from Google Maps using Python & Selenium*

[Overview](#-overview) •
[Features](#-what-this-project-does) •
[Installation](#-how-to-run) •
[Output](#-output) •
[Challenges](#-challenges-i-faced)

</div>

---

## 🎯 Overview

This is a **Python-based Google Maps scraper** built with Selenium. I created this project to help businesses and individuals extract location-based data from Google Maps automatically.

The scraper takes a **keyword as input** from the terminal, searches Google Maps, auto-scrolls through all results, visits each business page to get phone numbers, and saves everything into a **clean CSV file**.

---

## ✨ What this project does

<table>
<tr>
<td>

🔍 **Smart Search**
- Takes keyword input from terminal
- Searches Google Maps automatically
- Supports any location or business type

</td>
<td>

📊 **Complete Data Extraction**
- Business name, rating, address
- Phone number from each business page
- Handles dynamic content loading

</td>
<td>

⚡ **User Friendly**
- Simple terminal interface
- Search multiple keywords in one session
- Auto-saves to CSV after each search

</td>
</tr>
</table>

---

## 📊 Output

The scraper saves all data into a CSV file named after your search keyword.

**Example:** `restaurants_in_Dhaka.csv`

### Collected data includes:

| Field | Description | Example |
|-------|-------------|---------|
| 📛 **Name** | Business name | "Thai Chi Restaurant" |
| ⭐ **Rating** | Star rating | "4.1" |
| 📍 **Address** | Full address | "Level 7, 117/A, Gulshan Ave" |
| 📞 **Phone** | Phone number | "01711-901034" |

### Sample Output:
```
Name,Rating,Address,Phone_Number
Seasonal Tastes,4.6,"The Westin, Main Gulshan Ave",01730-304871
Amrit restaurant,4.7,21 Road No. 17,01982-700700
Breeze Restaurant,4.4,"House# 1/C, 1/D, Road# 16",01305-073888
Meat Theory,4.8,"Tower B11, Level 14",01633-642902
```

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|:----------:|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Core programming language |
| ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white) | Browser automation |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) | Data manipulation & CSV export |

</div>

**Additional:** ChromeDriver, Regex

---

## 🚀 How to run

### 📦 1. Clone the repository
```bash
git clone https://github.com/shiblysadik68/Google-Maps-Scraper.git
cd Google-Maps-Scraper
```

### ⚙️ 2. Install dependencies
```bash
pip install selenium pandas
```

### 🔧 3. Setup ChromeDriver

Download [ChromeDriver](https://chromedriver.chromium.org/downloads) based on your Chrome version and either:
- Add it to **PATH**, or
- Place it inside the **project folder**

> 💡 **Tip:** Check your Chrome version: `Chrome → Settings → About Chrome`

### ▶️ 4. Run the script
```bash
python scraper.py
```

### 🖥️ 5. Usage
```
write your keyword: restaurants in Dhaka
→ Browser opens automatically
→ Searches Google Maps
→ Scrolls through all results
→ Visits each business for phone number
✅ Saved to: restaurants_in_Dhaka.csv

next keyword: hotels in Cox's Bazar
→ Same process repeats
✅ Saved to: hotels_in_Cox's_Bazar.csv

next keyword: quit
👋 Goodbye!
```

---

## 🏗️ Code Structure

```python
✅ setup_driver()           → Browser setup with options
✅ search_places()          → Search Google Maps
✅ scroll_and_collect()     → Auto scroll & collect business cards
✅ extract_business_data()  → Extract all data including phone
✅ save_to_excel()          → Save to CSV
✅ main()                   → Controls the entire flow
```

---

## 🧠 What I learned

<details>
<summary><b>Click to expand learning journey</b></summary>

While working on this project, I gained hands-on experience with:

- ✅ Scraping **dynamic websites** with Selenium
- ✅ Handling **lazy loading** with auto-scroll
- ✅ Working with **Unicode/invisible characters** in scraped data
- ✅ Using **Regex** for text cleaning
- ✅ **Navigating between pages** to collect detailed data
- ✅ Using `aria-label` attributes to extract data
- ✅ Building **clean function-based** code structure
- ✅ Managing **user input** in automation scripts
- ✅ Proper **loop control** with break conditions

</details>

---

## 🐛 Challenges I faced

<table>
<tr>
<td width="50%">

### 1️⃣ Invisible Unicode Character

**Problem:**
Address field contained an invisible character `\ue934` (wheelchair icon) which broke the text splitting logic.

**Solution:**
Used **Regex** to remove everything before the last `·`:

```python
import re
address = re.sub(r'^.*·\s*', '', raw).strip()
```

</td>
<td width="50%">

### 2️⃣ Language Issue

**Problem:**
Google Maps was opening in Bengali automatically.

**Solution:**
Added `?hl=en` to force English:

```python
driver.get("https://www.google.com/maps/?hl=en")
```

</td>
</tr>
<tr>
<td width="50%">

### 3️⃣ Phone Number Extraction

**Problem:**
Multiple elements had the same class name. Couldn't identify which one was the phone number.

**Solution:**
Used `aria-label` attribute which clearly contains "Phone:":

```python
phone = driver.find_element(
    By.XPATH,
    "//button[contains(@data-item-id, 'phone')]"
).get_attribute("aria-label").replace("Phone: ", "")
```

</td>
<td width="50%">

### 4️⃣ Stale Element Error

**Problem:**
After clicking a business and going back, all collected cards became stale (unusable).

**Solution:**
Collected the business **URL first**, then navigated using `driver.get(link)`:

```python
link = card.find_element(
    By.XPATH, ".//a[@href]"
).get_attribute("href")
driver.get(link)
```

</td>
</tr>
</table>

---

## 📈 Performance

<div align="center">

| Metric | Value |
|:------:|:-----:|
| 📜 **Scroll Depth** | 10 scrolls (configurable) |
| 📚 **Results per search** | 40-60+ businesses |
| 📞 **Phone extraction** | Per business page visit |
| ⏱️ **Total Execution** | ~5-8 minutes per search |

</div>

---

## 🔧 Project File Structure

```
Google-Maps-Scraper/
│
├── 📄 scraper.py       # Main scraper script
├── 📊 output.csv       # Sample output data
├── 📝 README.md        # Project documentation
└── 📜 LICENSE          # MIT License
```

---

## 🚧 Future Improvements

- [ ] Add **website URL** extraction
- [ ] Add **business hours** extraction
- [ ] Add **business category** extraction
- [ ] Export to **Excel** with formatting
- [ ] Add **headless mode** for background execution
- [ ] Support **multiple keywords** in one run
- [ ] Add **progress bar** for better UX
- [ ] Add **duplicate removal**

---

## ⚠️ Note

> **Important:** This project is made for **learning purposes only**.
> Always respect website rules and `robots.txt` before scraping.
> Implement appropriate delays to avoid overloading servers.

---

## 👤 Author

<div align="center">

**Shibly Sadik**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/shiblysadik68)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shibly-sadik-0bbb59129/)

*Open for freelance projects and collaboration!*

</div>

---

## 🌟 Support

<div align="center">

**If you found this project helpful, please give it a ⭐!**

[![Star this repo](https://img.shields.io/github/stars/shiblysadik68/Google-Maps-Scraper?style=social)](https://github.com/shiblysadik68/Google-Maps-Scraper)

</div>

---

<div align="center">

**Happy Scraping! 🚀**

Made with ❤️ by [Shibly Sadik](https://github.com/shiblysadik68)

</div>