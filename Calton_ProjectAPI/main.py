from fastapi import FastAPI, HTTPException
from typing import List
from PydanticModel import RestaurantReview  # Ensure this import is correct
import pandas as pd
from scraper import scrape_justeat_reviews  # Import the scraping function

# Initialize FastAPI app
app = FastAPI()

# In-memory storage for reviews
reviews = []

# Endpoint to add a review
@app.post("/add_review")
def add_review(review: RestaurantReview):
    reviews.append(review)  # Add the review to the in-memory storage
    return {"message": "Review added successfully"}

# Endpoint to fetch all reviews
@app.get("/reviews", response_model=List[RestaurantReview])
def get_reviews():
    return reviews  # Return all reviews

# Load the Excel file containing initial reviews
file_path = "C:\\Users\\andre\\Desktop\\Calton_ProjectAPI\\example.xlsx"  # Ensure the path is correct and absolute
df = pd.read_excel(file_path)

# Convert the DataFrame to a list of dictionaries for easier manipulation
excel_reviews = df.to_dict(orient='records')

# Endpoint to fetch reviews from the Excel file
@app.get("/excel_reviews", response_model=List[RestaurantReview])
def get_excel_reviews():
    return excel_reviews  # Return reviews from the Excel file

# Endpoint to scrape reviews from JustEat
@app.get("/scrape_reviews/{restaurant_name}", response_model=List[RestaurantReview])
def scrape_reviews(restaurant_name: str):
    try:
        scraped_reviews = scrape_justeat_reviews(restaurant_name)
        return scraped_reviews
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint for a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the Restaurant Reviews API"}
