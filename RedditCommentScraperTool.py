
import sys
sys.path.append('lib')
from crewai_tools import Tool, BaseTool
import praw
from datetime import datetime, timedelta

# Initialize the PRAW instance with your Reddit credentials
reddit = praw.Reddit(
    client_id="naRHsiMfccnfjpFymWGc_w",
    client_secret="z7bRWnD_79GvxQjEuqGKSpQUFGheOw",
    user_agent="ProductAnalysisAgent"
)

class RedditCommentScraperTool(BaseTool):
    name: str = "RedditCommentScraper"
    description: str = "Scrapes recent user comments from a given subreddit within the last N days."

    def _run(self, subreddit_name: str, days_back: int) -> list:
        """
        Scrapes user comments from a given subreddit within the last N days.
        
        Args:
        - subreddit_name (str): Name of the subreddit to scrape.
        - days_back (int): Number of days back to look for comments.
        
        Returns:
        - List of comments that were posted in the last N days.
        """
        try:
            # Get the subreddit
            # print(subreddit_name)
            subreddit = reddit.subreddit(subreddit_name)
            threshold_date = datetime.utcnow() - timedelta(days=days_back)

            # List to store comments
            recent_comments = []

            # Fetch comments from the subreddit
            for submission in subreddit.new(limit=10):  # Limit to recent 100 posts
                submission.comments.replace_more(limit=5)
                for comment in submission.comments.list():
                    # Convert the comment creation time to a datetime object
                    comment_date = datetime.utcfromtimestamp(comment.created_utc)
                    if comment_date >= threshold_date:
                        # Construct the comment link
                        comment_link = f"https://www.reddit.com{submission.permalink}{comment.id}/"
                        
                        recent_comments.append({
                            'comment': comment.body,
                            'author': str(comment.author),
                            'created_at': comment_date,
                            'post_title': submission.title,
                            'post_url': submission.url,  # URL to the original post
                            'comment_link': comment_link  # URL to the specific comment
                        })

            return recent_comments

        except Exception as e:
            return {"error": str(e)}

