#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from testcase_writter.crew import TestcaseWritter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "topic":"E-commerce",
        'user_story': "User Story: Login Feature for an E-commerce App Title: User Login with Email and Password As a Registered user of the e-commerce platform I want to Log in using my email and password So that I can Access my account, view my order history, and manage my profile",
        'current_year': str(datetime.now().year)
    }
    
    try:
        TestcaseWritter().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic":"E-commerce",
        "user_story": """User Story: Login Feature for an E-commerce App

Title: User Login with Email and Password

As a  
Registered user of the e-commerce platform  

I want to  
Log in using my email and password  

So that I can  
Access my account, view my order history, and manage my profile
"""
    }
    try:
        TestcaseWritter().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TestcaseWritter().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "SDET"
    }
    try:
        TestcaseWritter().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
