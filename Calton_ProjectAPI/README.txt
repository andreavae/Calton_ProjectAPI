# Restaurant Reviews API

This is a FastAPI-based web service for managing restaurant reviews. The API supports adding reviews, fetching reviews from an in-memory store, and loading initial reviews from an Excel file.

## Features

- **Add Review**: An endpoint to add a new review.
- **Fetch Reviews**: An endpoint to retrieve all stored reviews.
- **Fetch Excel Reviews**: An endpoint to retrieve reviews from an Excel file.
- **(Optional) Scrape JustEat Reviews**: A placeholder endpoint for future implementation of scraping reviews from JustEat.

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn
- Pydantic
- Pandas
- Openpyxl (for reading Excel files)

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
    pip install fastapi uvicorn pydantic pandas openpyxl
    ```

4. **Place the Excel file**: Ensure the Excel file `example (1) (1).xlsx` is located in the directory `C:\Users\andre\Desktop\Calton_ProjectAPI`.

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
    Open your browser and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by Swagger.

## API Endpoints

- **Root Endpoint**:
    - `GET /`: Returns a welcome message.
    
- **Add Review**:
    - `POST /add_review`: Adds a new review.
    - **Request Body**:
        ```json
        {
            "restaurant_name": "The Great Restaurant",
            "rating": 5,
            "comment": "The food was excellent and the service was outstanding!"
        }
        ```
    - **Response**:
        ```json
        {
            "message": "Review added successfully"
        }
        ```

- **Fetch Reviews**:
    - `GET /reviews`: Retrieves all stored reviews.
    - **Response**:
        ```json
        [
            {
                "restaurant_name": "The Great Restaurant",
                "rating": 5,
                "comment": "The food was excellent and the service was outstanding!"
            }
        ]
        ```

- **Fetch Excel Reviews**:
    - `GET /excel_reviews`: Retrieves reviews from the Excel file.
    - **Response**:
        ```json
        [
            {
                "restaurant_name": "Some Restaurant",
                "rating": 4,
                "comment": "Great food, decent service."
            }
        ]
        ```

- **Scrape Reviews**:
    - `GET /scrape_reviews/{restaurant_name}`: Placeholder for scraping reviews from JustEat.
    - **Response**:
        ```json
        {
            "message": "Scraping reviews for {restaurant_name} is not implemented yet"
        }
        ```

## Notes

- Ensure the Excel file `example.xlsx` is in the correct directory.
- Customize the `scrape_reviews` endpoint as needed for scraping reviews from JustEat.

## Contributing

If you would like to contribute to this project, please create a fork and submit a pull request.

## License

This project is licensed under the Calton License.
