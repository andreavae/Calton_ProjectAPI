import requests 
from bs4 import BeautifulSoup 
from PydanticModel import RestaurantReview

def scrape_justeat_reviews(restaurant_name: str):
    # URL construction for demonstration purposes. The actual URL will depend on JustEat's structure.
    url = f"https://www.just-eat.co.uk/restaurants-{restaurant_name.lower().replace(' ', '-')}/reviews"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Restaurant not found or cannot be accessed")

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example scraping logic (this will depend on the actual HTML structure of JustEat's review page)
    reviews = []
    for review in soup.find_all('div', class_='review'):
        rating = int(review.find('div', class_='rating').text.strip())
        comment = review.find('p', class_='comment').text.strip()
        reviews.append(RestaurantReview(restaurant_name=restaurant_name, rating=rating, comment=comment))

    return reviews
