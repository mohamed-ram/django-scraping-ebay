from bs4 import BeautifulSoup
from django.shortcuts import render
from .forms import WatchForm
import requests


def get_url(request):
    # base_url = "https://www.ebay.com/b/Wristwatches/31387/bn_2408451?mag=1"
    
    dep = request.POST.get("department")
    brand = request.POST.get("brand")
    price_from = request.POST.get("price_from")
    price_to = request.POST.get("price_to")
    
    # if all([dep, brand, price_from, price_to]):
    #     print("all ok")
    base_url =F"https://www.ebay.com/b/Watches/260325?Department={dep.title()}&Brand={brand.title()}&rt=nc&_udlo={price_from}&_udhi={price_to}&mag=1"
    
    return base_url



def get_data(request):
    url = "https://www.ebay.com/b/Watches/260325/bn_7117208191?mag=1"
    data = []
    form = WatchForm()
    if request.method == "POST":
        form = WatchForm(request.POST)
        if form.is_valid():
            url = get_url(request)
            print(url)
    
    
        # fetching data
        page = requests.get(url)
        
        bs = BeautifulSoup(page.text, "html.parser")
        watches_list = bs.find("ul", class_="b-list__items_nofooter").find_all("li", class_="s-item")
        
        for watch in watches_list:
            watch_img = watch.find("img", class_="s-item__image-img")["src"]
            watch_title = watch.find("h3", class_="s-item__title").text
            watch_price = watch.find("span", class_="s-item__price").text
            watch_url = watch.find("div", class_="s-item__info").find("a")["href"]
            
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
    print(data)
    return render(request, 'ebay/home.html', context=context)

