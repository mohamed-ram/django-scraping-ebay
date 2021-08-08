from bs4 import BeautifulSoup
import pandas as pd

from django.shortcuts import render
from .forms import WatchSearchForm
import requests


def get_url(request):
    dep = request.POST.get("department")
    brand = request.POST.get("brand")
    price_from = request.POST.get("price_from")
    price_to = request.POST.get("price_to")
    
    base_url =F"https://www.ebay.com/b/Watches/260325?Department={dep.title()}&Brand={brand.title()}&rt=nc&_udlo={price_from}&_udhi={price_to}&mag=1"
    
    return base_url


# export data to csv file..
def export_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("data.csv", index=False, encoding="utf-8")
    

def get_data(request):
    url = "https://www.ebay.com/b/Watches/260325/bn_7117208191?mag=1"
    data = []
    
    form = WatchSearchForm()
    if request.method == "POST":
        form = WatchSearchForm(request.POST)
        if form.is_valid():
            url = get_url(request)
            print(url)
    
    
        # fetching data
        page = requests.get(url)
        
        bs = BeautifulSoup(page.text, "html.parser")
        watches_list = bs.find("ul", class_="b-list__items_nofooter").find_all("li", class_="s-item")
        
        for watch in watches_list:
            watch_url = watch.find("div", class_="s-item__info").find("a")["href"]
            # watch_img = watch.find("div", class_="s-item__image").find("img", class_="s-item__image-img")["src"]
            watch_img = F"https://i.ebayimg.com/thumbs/images/g/{watch_url.split(':g:')[-1][:16]}/s-l300.jpg"
            watch_title = watch.find("h3", class_="s-item__title").text
            watch_price = watch.find("span", class_="s-item__price").text
            
            data.append({
                "img": watch_img,
                "title": watch_title,
                "price": watch_price,
                "url": watch_url,
            })
            
    
    context = {
        "form": form,
        "watches": data
    }
    # print(data)
    
    return render(request, 'ebay/home.html', context=context)

