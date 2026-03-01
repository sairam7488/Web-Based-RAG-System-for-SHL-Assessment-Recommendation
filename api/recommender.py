# api/recommender.py

def recommend(query: str):
    """
    Temporary dummy recommender.
    This is just to verify FastAPI works.
    """
    return [
        {
            "name": "Sample Assessment",
            "url": "https://www.shl.com/solutions/products/",
            "description": "Dummy assessment for testing",
            "duration": 15,
            "adaptive_support": "Yes",
            "remote_support": "Yes",
            "test_type": ["Knowledge & Skills"]
        }
    ]