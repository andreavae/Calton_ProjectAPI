from pydantic import BaseModel, Field, validator

# Define the Pydantic model for restaurant reviews
class RestaurantReview(BaseModel):
    restaurant_name: str  # The name of the restaurant
    rating: int = Field(..., ge=1, le=5)  # Rating must be between 1 and 5
    comment: str = Field(..., min_length=5, max_length=500)  # Comment must be between 5 and 500 characters

    # Validator to ensure the comment length does not exceed 500 characters
    @validator('comment')
    def comment_length(cls, v):
        if len(v) > 500:
            raise ValueError('Comment is too long')
        return v