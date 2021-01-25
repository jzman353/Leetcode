import requests
from bs4 import BeautifulSoup
'''
def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #Go to web page, right click on price, inspect element, copy path name
    #elems = soup.select('html.a-ws.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-transform3d.-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.a-ember body.a-m-us.a-aui_72554-c.a-aui_control_group_273125-t1.a-aui_dropdown_274033-t1.a-aui_link_rel_noreferrer_noopener_274172-c.a-aui_mm_desktop_exp_291916-c.a-aui_mm_desktop_launch_291918-c.a-aui_mm_desktop_targeted_exp_291928-t1.a-aui_mm_desktop_targeted_launch_291922-t1.a-aui_pci_risk_banner_210084-c.a-aui_perf_130093-c.a-aui_preload_261698-c.a-aui_tnr_v2_180836-c div#a-page div#dp.musical_instruments.en_US div#dp-container.a-container div#ppd div#rightCol.rightCol.rightCol-bbcxoverride div#desktop_buybox.celwidget div#buybox div#qualifiedBuybox.celwidget div.a-section form#addToCart.a-content div.a-box-group div.a-box.a-last div.a-box-inner div.a-section.a-spacing-none.a-padding-none div#priceInsideBuyBox_feature_div.celwidget div.a-section span#price_inside_buybox.a-size-medium.a-color-price')
    #return elems[0].text.strip()

    inspect_element_available = """html.a-ws.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-hires.a-transform3d.-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.a-ember body.a-m-us.a-aui_72554-c.a-aui_mm_desktop_exp_291916-c.a-aui_mm_desktop_launch_291918-c.a-aui_mm_desktop_targeted_exp_291928-t1.a-aui_mm_desktop_targeted_launch_291922-t1.a-aui_pci_risk_banner_210084-c.a-aui_perf_130093-c.a-aui_preload_261698-c.a-aui_rel_noreferrer_noopener_309527-c.a-aui_tnr_v2_180836-c div#a-page div#dp.toy.en_US div#dp-container.a-container div#ppd div#rightCol.rightCol.rightCol-bbcxoverride div#desktop_buybox.celwidget div#buybox div#qualifiedBuybox.celwidget div.a-section form#addToCart.a-content div.a-box-group div.a-box.a-last div.a-box-inner div.a-section.a-spacing-none.a-padding-none div#priceInsideBuyBox_feature_div.celwidget div.a-section span#price_inside_buybox.a-size-medium.a-color-price"""

    elems = soup.select(inspect_element_available)
    print(elems)
    return elems[0].text.strip()

link = "https://www.amazon.com/Exploding-Kittens-LLC-EKG-ORG1-1-Card/dp/B010TQY7A8/ref=zg_bs_toys-and-games_home_3?_encoding=UTF8&psc=1&refRID=NAR6737X5N0X6XGFTA5C"
print(getAmazonPrice(link))
'''
def getAmazonPrice(productUrl):
    """
    import requests
    from glob import glob # a nice package that allows you to get things like a list of filenames inside a folder
    from bs4 import BeautifulSoup
    import pandas as pd
    from datetime import datetime
    from time import sleep
    """
    # http://www.networkinghowtos.com/howto/common-user-agent-list/
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
    """
    # imports a csv file with the url's to scrape
    prod_tracker = pd.read_csv('trackers/TRACKER_PRODUCTS.csv', sep=';')
    prod_tracker_URLS = prod_tracker.url
    """
    # fetch the url
    #page = requests.get(prod_tracker_URLS[0], headers=HEADERS)
    page = requests.get(productUrl, headers=HEADERS)
    # create the object that will contain all the info in the url
    soup = BeautifulSoup(page.content, features="lxml")

    # product title
    title = soup.find(id='productTitle').get_text().strip()

    # to prevent script from crashing when there isn't a price for the product
    try:
        #ID's
        #price
        #price_inside_buybox
        #priceblock_ourprice
        #a-price-whole
        price = float(soup.find(id='price').get_text().replace('$', '').strip())
    except:
        try:
            price = float(soup.find(id='price_inside_buybox').get_text().replace('$', '').strip())
        except:
            try:
                price = float(soup.find(id='priceblock_ourprice').get_text().replace('$', '').strip())
            except:
                try:
                    price = float(soup.find(id='a-price-whole').get_text().replace('$', '').strip())
                except:
                    price = ''

    # review score
    try:
        review_score = float(soup.select('.a-star-4-5')[0].get_text().split(' ')[0].replace(",", "."))
    except:
        review_score = ''

    # how many reviews
    review_count = int(soup.select('#acrCustomerReviewText')[0].get_text().split(' ')[0].replace(".", "").replace(",", ""))

    # checking if there is "Out of stock" and if not, it means the product is available
    try:
        a = soup.select('#availability')[0].get_text().strip()
        if 'In Stock.' in a:
            stock = 'In Stock'
        elif 'Available from these sellers' in a:
            stock = 'In Stock'
        elif 'Currently unavailable' in a:
            stock = 'Currently unavailable'
        else:
            #print(a)
            stock = "Unsure if Available"
    except:
        #print(a)
        stock = 'Unsure if Available'

    return [title, price, review_score, review_count, stock]
link = 'https://www.amazon.com/Promised-Land-Barack-Obama/dp/1524763160/ref=zg_bs_books_home_1?_encoding=UTF8&psc=1&refRID=45HVYBRF5YHKDXZC8YJM'
print(getAmazonPrice(link))
link = 'https://www.amazon.com/Exploding-Kittens-LLC-EKG-ORG1-1-Card/dp/B010TQY7A8/ref=zg_bs_toys-and-games_home_3?_encoding=UTF8&psc=1&refRID=NAR6737X5N0X6XGFTA5C'
print(getAmazonPrice(link))
link = 'https://www.amazon.com/DualSense-Wireless-Controller-PlayStation-5/dp/B08FC6C75Y/ref=pd_rhf_ee_s_pd_crcd_0_6/147-9034847-8530432?_encoding=UTF8&pd_rd_i=B08FC6C75Y&pd_rd_r=cc877240-dae0-408f-b219-257657ecdf59&pd_rd_w=mPrGM&pd_rd_wg=YjQ0N&pf_rd_p=8019ba47-0a12-4976-b76b-5c932d60db6f&pf_rd_r=CH8DC2PXC1BQ1X9KMSHJ&psc=1&refRID=CH8DC2PXC1BQ1X9KMSHJ'
print(getAmazonPrice(link))
link = 'https://www.amazon.com/MSI-GeForce-320-Bit-Architecture-Graphics/dp/B08HR5SXPS/ref=pd_rhf_ee_s_pd_crcd_0_5/147-9034847-8530432?_encoding=UTF8&pd_rd_i=B08HR5SXPS&pd_rd_r=cc877240-dae0-408f-b219-257657ecdf59&pd_rd_w=mPrGM&pd_rd_wg=YjQ0N&pf_rd_p=8019ba47-0a12-4976-b76b-5c932d60db6f&pf_rd_r=CH8DC2PXC1BQ1X9KMSHJ&psc=1&refRID=CH8DC2PXC1BQ1X9KMSHJ'
print(getAmazonPrice(link))
link = 'https://smile.amazon.com/Holiday-Ultimate-Playstation-Spider-Man-Horizon/dp/B082S2LYV1/ref=sr_1_1?crid=3DB5B8QXG5G9H&dchild=1&keywords=playstation+5&qid=1609303401&sprefix=pla%2Caps%2C264&sr=8-1'
print(getAmazonPrice(link))
"""
link = 
print(getAmazonPrice(link))
"""