from crewai import Task
from textwrap import dedent

class OvernightTasks():
    def __init__(self, *, repository):
        self.repository = repository

    def plan_project(self, agent):
        return Task(description=dedent(f"""
            First read the repository title, description and README.
            Pay special attention to the project's goals and objectives.

            Collect all open issues and open pull requests from the repository.
            Go through each open pull request first.
            Read the title, description and all comments from the pull request and summarize its current state.
            Pay special attention to questions and open acceptance criteria.
            Determine the role(s) who should take action, if any.
            Note down any actions to complete the pull request in the plan.

            Go through each open issue.
            Read the title, description and all comments from the issue and summarize its current state.
            Pay special attention to questions and open acceptance criteria.
            Determine the role(s) who should take action, if any.
            Note down any open actions to complete the issue in the plan.

            Your final answer MUST be a plan that includes a step by step guide
            on how to complete the project in its current state.
            Each step MUST be clear, concise and designated for a single role.
            Each step MUST be actionable and have a clear outcome.

            {self.__repository()}
            """),
            agent=agent
        )

    def plan_session(self, agent, repository):
        return Task(description=dedent(f"""
            First read the repository title, description and README.
            Pay special attention to the project's goals and objectives.

            Fetch the first open issue that is assigned to you.
            Read the title, description and all comments from the issue and summarize its current state.
            Pay special attention to questions and open acceptance criteria.
            Note down any actions to complete the issue.

            Your final answer MUST be a step by step guide
            on how to complete the issue in its current state.
            Each step MUST be clear, concise and designated for your role.
            Each step MUST be actionable and have a clear outcome.

            {self.__repository()}
            """),
            agent=agent
        )

    def work_session(self, agent):
        return Task(description=dedent(f"""
            Read your plan for the session.
            """),
            agent=agent
        ))

    def __repository(self):
        return f"Selected repository: {self.repository}"

