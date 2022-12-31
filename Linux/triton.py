#! /usr/bin/python3 -W ignore
def run ():
    import csv
    import os
    # from selenium import webdriver
    # from selenium.webdriver.firefox.options import Options
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC
    from requests import get
    from bs4 import BeautifulSoup as Bs
    import tabula
    import time
    from datetime import date
    print("fetching from browser...",end = "\r")
    # fireFoxOptions = Options()
    # fireFoxOptions.headless=True
    # driver = webdriver.Firefox(options=fireFoxOptions)

    text = get("https://gr.triton-am.com/mutual-fund-price-list/").text
    soup = Bs(text,'html.parser')
    # try:
        # WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CLASS_NAME, "porto-links-item")))
        # driver.execute_script("window.scrollTo(0, 550)")
    # except:
    #    driver.quit()
        # pass
    #print("loaded")
    #    driver.quit()
    # time.sleep(1)
    # pdf = driver.find_element(By.CLASS_NAME,"porto-links-item")
    # pdf.click()
    #btn = driver.find_element(By.ID,"download")
    #btn.click()
    # url = driver.current_url
    # print (url)
    # driver.quit()
    links = []

    for div in soup.find_all(class_ = 'porto-links-item'):

        for link in div:
            if (link.get('href') is not None):
                links.append(link.get('href'))
    
    url = links[0]
    print(url)
    print("converting to csv ...         ",end = "\r")

    df = tabula.read_pdf(url,pages=1)[0]
    outfile = os.path.expanduser("/tmp/tmp_triton.csv")
    df.to_csv(outfile)
    
    print("parsing from csv ...       ",end = "\r")
    print("                                                                 ",end = "\r")

    price = 0
    with open(outfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if (row[3] == "GRF000087004"): 
                price = row[7]
                res = ""
                res+='\n'+("...... TRITON .....")
                units = 705.864
                price = float(price.replace(',','.'))
                val = units*price
                clear = val - 160
                gain = clear - 160 - 32000
                percent = gain/32000 *100
                res+='\n'+ (f"current unit Price.......{price}")
                res+='\n'+ (f"Value (705.864 units)....{round(val,2)}")
                res+='\n'+ (f"Clear Value (- 160 fee)..{round(clear,2)}")
                res+='\n'+ (f"Gain.....................{round(gain,2)}")
                res+='\n'+ (f"Gain %...................{round(percent,2)}%")
                print (res)
                # return (res)
                return {
                    "current unit Price":price,
                    "Value (705.864 units)":round(val,2),
                    "Clear_Value (- 160 fee)":round(clear,2),
                    "Gain":round(gain,2),
                    "Gain_%":round(percent,2)
                }

    with open(os.path.expanduser("~/Triton/log.csv"), '+a') as log:
        log.write(f"{date.today()},{price}\n")
        log.close()

if __name__ == "__main__":
    run()
