import sys
sys.path.append('lib')

from pydantic import BaseModel

from typing import List, Dict

# Define the Pydantic model for the summarized output
class PostSummary(BaseModel):
    post_title: str
    comment_summary: str
    critical: bool
    post_date: str
    comment_link: str
    post_link: str

class RedditSummaryOutput(BaseModel):
    reddit: List[PostSummary]


