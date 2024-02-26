import os
from github import Github
from github import Auth
from smol_dev.prompts import plan, specify_file_paths, generate_code_sync
import openai
from openai_function_call import openai_function


model = 'gpt-3.5-turbo-0613'
github = Github(auth=Auth.Token(os.environ["GITHUB_TOKEN"]))


def q(prompt):
    completion = openai.ChatCompletion.create(
        model=model,
        temperature=0.7,
        messages=[
            dict(role='system', content='You are a top tier AI developer, overall helpful providing concise answers.'),
            dict(role='user', content=prompt)
        ]
    )
    return completion.choices[0].message.content

def generate_branch_for_issue(issue):
    completion = openai.ChatCompletion.create(
        model=model,
        temperature=0.7,
        messages=[
            dict(role='system', content='You are a top tier AI developer, overall helpful providing concise answers.'),
            dict(role='user', content=f'Generate a git branch name, with very few words, all lowercase separated by hyphens from the following issue title "{issue.title} and issue number {issue.number}. Use the format: issue/NUMBER-few-descriptive-words')
        ]
    )
    return completion.choices[0].message.content

def generate_changes_for_issue(issue):
    # branch_name = generate_branch_for_issue(issue)
    objective = "Python command line application to generate code based on Github issues"

    current_plan = """
App Structure:

1. overnight.py:
   - This is the main entry point of the application.
   - It will handle user input and control the flow of the program.
   - It will prompt the user to enter the details of the Github issue.
   - It will call the necessary functions to generate the code based on the provided input.

2. github_api.py:
   - This file will contain functions to interact with the Github API.
   - It will handle authentication and request the necessary data from the Github API.
   - It will export the necessary functions for retrieving the Github issue data.

3. code_generator.py:
   - This file will contain functions to generate code based on the Github issue data.
   - It will receive the Github issue data as input and create code snippets or files based on the provided data.
   - It will export the necessary functions for code generation.

4. data_schemas.py:
   - This file will define the data schemas for the Github issue and code generation.
   - It will export the necessary data schemas to ensure data consistency and validation.

Variable exports:
- overnight.py: No variable exports.
- github_api.py: Functions for interacting with the Github API.
- code_generator.py: Functions for generating code snippets or files.
- data_schemas.py: Data schemas for Github issue and code generation.

DOM element id names: N/A (This is a command-line application, so there are no DOM elements)

Message names: N/A (This is a command-line application, so there are no messages)

Function names:
- overnight.py: main()
- github_api.py: authenticate(), get_issue_data()
- code_generator.py: generate_code()
- data_schemas.py: GithubIssueSchema, CodeSchema
    """

    new_plan = f"""
Given the objective and current plan, and the following issue, formulate a new plan for the application.\n

Objective: {objective}

Issue title: {issue.title}
Issue body:
{issue.body}

Current plan:
{current_plan}
"""
    latest_plan = plan(new_plan)
    print(latest_plan)
    file_paths = specify_file_paths(objective, latest_plan)
    for file_path in file_paths:
        code = generate_code_sync(objective, latest_plan, file_path)
        print(file_path)
        print(code)

if __name__ == "__main__":
    repository = github.get_repo('Overbryd/overnight')
    for issue in repository.get_issues(state='open'):
        generate_changes_for_issue(issue)

