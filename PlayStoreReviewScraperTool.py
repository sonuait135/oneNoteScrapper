
import sys
sys.path.append('lib')
from crewai_tools import BaseTool
from datetime import datetime, timedelta

from google_play_scraper import app, Sort, reviews

class PlayStoreReviewScraperTool(BaseTool):
    name: str = "PlayStoreReviewScraper"
    description: str = "Fetch user reviews from a given Play Store app in the last N days."

    def _run(self, app_id: str, days_back: int) -> list:
        """
        Fetches reviews from the Google Play Store app within the last N days.
        
        Args:
        - app_id (str): The Play Store app ID (e.g., 'com.microsoft.office.onenote').
        - days_back (int): Number of days back to filter reviews.
        
        Returns:
        - List of reviews posted within the last N days.
        """
        try:
            # Fetch reviews using google_play_scraper
            result, _ = reviews(
                app_id,  # App's package name
                lang='en',  # Reviews language
                country='us',  # Reviews country
                sort=Sort.NEWEST,  # Sort by newest first
                count=5  # Max number of reviews to fetch
            )
            
            # Filter reviews by the last N days
            threshold_date = datetime.utcnow() - timedelta(days=days_back)
            recent_reviews = []
            
            for review in result:
                review_date = datetime.utcfromtimestamp(review['at'].timestamp())
                if review_date >= threshold_date:
                    recent_reviews.append({
                        'content': review['content'],
                        'author': review['userName'],
                        'rating': review['score'],
                        'created_at': review_date
                    })
            
            return recent_reviews
        
        except Exception as e:
            return {"error": str(e)}
