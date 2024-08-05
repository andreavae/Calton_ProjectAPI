# Restaurant Reviews API

This is a FastAPI-based web service for managing restaurant reviews. The API supports adding reviews, fetching reviews from an in-memory store, loading initial reviews from an Excel file, and scraping reviews from JustEat.

## Features

- **Add Review**: An endpoint to add a new review.
- **Fetch Reviews**: An endpoint to retrieve all stored reviews.
- **Fetch Excel Reviews**: An endpoint to retrieve reviews from an Excel file.
- **Scrape JustEat Reviews**: An endpoint to scrape reviews from JustEat.

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn
- Pydantic
- Pandas
- Openpyxl (for reading Excel files)
- BeautifulSoup4 (for web scraping)
- Requests (for web scraping)

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install fastapi uvicorn pydantic pandas openpyxl beautifulsoup4 requests
    ```

4. **Place the Excel file**: Ensure the Excel file `example.xlsx` is located in the directory `C:\Users\andre\Desktop\Calton_ProjectAPI`.

## Usage

1. **Navigate to the project directory**:
    ```bash
    cd C:\Users\andre\Desktop\Calton_ProjectAPI
    ```

2. **Run the FastAPI server**:
    ```bash
    uvicorn main:app --reload
    ```

3. **Access the API**:
    Open your browser and go to `http://127.0.0.1:8000`.

4. **API Documentation**:
    The interactive API documentation can be accessed at `http://127.0.0.1:8000/docs`.
    Alternatively, the alternative documentation can be accessed at `http://127.0.0.1:8000/redoc`.

## Examples of API Requests

### Add Review

To add a review, send a POST request to `/add_review` with the following JSON payload:

**Request:**

```bash
curl -X POST "http://127.0.0.1:8000/add_review" -H "Content-Type: application/json" -d '{
    "restaurant_name": "Example Restaurant",
    "rating": 5,
    "comment": "Great food and service!"
}'
