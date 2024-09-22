
import os
import praw
from langchain_openai import AzureChatOpenAI

from crewai import Crew, Process, Agent, Task, Crew

from typing import List, Dict
from PlayStoreReviewScraperTool import PlayStoreReviewScraperTool
from RedditCommentScraperTool import RedditCommentScraperTool
from models import RedditSummaryOutput


# Initialize the PRAW instance with your Reddit credentials
reddit = praw.Reddit(
    client_id="naRHsiMfccnfjpFymWGc_w",
    client_secret="z7bRWnD_79GvxQjEuqGKSpQUFGheOw",
    user_agent="ProductAnalysisAgent"
)

os.environ["AZURE_API_KEY"] = "2346034c77ca41c58c8de5231182347f"
os.environ["AZURE_API_BASE"] = "https://onenotepoc.openai.azure.com/"
os.environ["AZURE_API_VERSION"] = "2024-05-01-preview"

deploymentname = "chat35"
keywordAzure = "azure"

gpt4o = AzureChatOpenAI(
    openai_api_version = os.environ.get("AZURE_API_VERSION"),
    model = keywordAzure+"/"+deploymentname,
    openai_api_type = keywordAzure,
    azure_endpoint = os.environ.get("AZURE_API_BASE"),
    api_key = os.environ.get("AZURE_API_KEY")
)



# Instantiate the custom tool
reddit_scraper_tool = RedditCommentScraperTool()

# Instantiate the custom tool
playstore_scraper_tool = PlayStoreReviewScraperTool()

# Create an agent that uses the custom Reddit comment scraper tool
reddit_scraper_agent = Agent(
    verbose=True,
    role="Reddit Scraper",
    goal="Scrape recent user comments from last {N} days from the given subreddit {subreddit}.",
    backstory="You are good at finding the comments from a given subreddit",
    tools=[reddit_scraper_tool],  # Pass the tool here
    llm=gpt4o,
)

# Agent to use the Play Store scraper tool
playstore_review_agent = Agent(
    role="Play Store Review Scraper",
    goal="Fetch recent user reviews from a given Play Store app in the last {N} days.",
    backstory="With a knack of data and attention to detail, you are good at looking through user comments.",
    tools=[playstore_scraper_tool],
    llm=gpt4o,
)

# Instantiate the summarizer agent
summarizer_agent = Agent(
    verbose=True,
    role="Comment Summarizer",
    goal="Summarize user comments from Reddit posts and return them in a structured format.",
    backstory= "You are good at reading and understanding user pain points and able to summarize comments better.",
    llm=gpt4o,
)


# Define a task that uses the agent to scrape comments from the subreddit
def scrape_subreddit_comments_task(context):
    subreddit_name = context.get("subreddit", "OneNote")  # Default to 'OneNote'
    days_back = context.get("days", 7)  # Default to 7 days back
    return reddit_scraper_tool.run(subreddit_name=subreddit_name, days_back=days_back)

scrape_task = Task(
    description="Scrape recent comments from last {N} days for a given subreddit {subreddit}.",
    task_function=scrape_subreddit_comments_task,
    expected_output="A list of user Post and comments from the last {N} days.",
    agent=reddit_scraper_agent
)



# Task to run the Play Store scraper and filter reviews by the last N days
def fetch_playstore_reviews_task(context):
    app_id = context.get("app_id", "")  # Play Store app ID (e.g., 'com.microsoft.office.onenote')
    days_back = context.get("days", 7)  # Default to last 7 days
    return playstore_scraper_tool.run(app_id=app_id, days_back=days_back)

# Define the task
fetch_playstore_task = Task(
    description="Fetch Play Store reviews for a given app {app_id} within the last {N} days.",
    task_function=fetch_playstore_reviews_task,
    expected_output="A list of Play Store reviews from the last {N} days for app {app_id}.",
    agent=playstore_review_agent
)


# Define the task
summarize_task = Task(
    description="Summarize Reddit comments by post and structure the output in a Pydantic model."
           "The comments should be meaningfully summarized. Also assess whether this post is a critical bug/regression. Add post creation date with links as well",
    expected_output="A structured summary of Reddit posts and their comments along with post creation dates and links. Also assess whether this post is a critical bug/regression.",
    context=[scrape_task],
    output_pydantic=RedditSummaryOutput,
    agent=summarizer_agent
)

summarize_task_googlePlay= Task(
    description="Summarize Reddit comments by post and structure the output in a Pydantic model."
           "The comments should be meaningfully summarized. Also assess whether this post is a critical bug/regression. Add post creation date with links as well",
    expected_output="A structured summary of Reddit posts and their comments along with post creation dates and links. Also assess whether this post is a critical bug/regression.",
    context=[fetch_playstore_task],
    output_pydantic=RedditSummaryOutput,
    agent=summarizer_agent
)

def invoke_Crew(data):

    isReddit:bool = data.get('isReddit')
    redditSubject = data.get('redditSubject')
    isGooglePlayStore = data.get('isGooglePlayStore')
    googlePlayStoreSubject = data.get('googlePlayStoreSubject')
    noOfDays = data.get('noOfDays')

    if isReddit == True:
        agentsList=[reddit_scraper_agent, summarizer_agent];
        tasksList=[scrape_task, summarize_task];
    
    if isGooglePlayStore == True:
        agentsList=[playstore_review_agent, summarizer_agent];
        tasksList=[fetch_playstore_task, summarize_task_googlePlay];
     
    crew = Crew (
        agents=agentsList,
        tasks=tasksList,
        process=Process.sequential,
    )

    # Example input data for the task
    input_data = {
        "subreddit": redditSubject, # "OneNote",
        "app_id": googlePlayStoreSubject, # "com.microsoft.office.onenote",  # Play Store app ID
        "N": noOfDays  # Look back 10 days
    }

    # # \print(crew)
     
    # Run the task with the input data
    return crew.kickoff(input_data)