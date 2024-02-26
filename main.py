from crewai import Crew
from overnight_agents import OvernightAgents
from overnight_tasks import OvernightTasks

class SoftwareDevelopmentCrew:
    def __init__(self, repository):
        self.repository = repository

    def run(self):
        agents = OvernightAgents()
        tasks = OvernightTasks(repository=self.repository)

        pm_agent = agents.project_manager()

        crew = Crew(
          agents=[
              pm_agent,
          ],
          tasks=[
            tasks.plan_project(pm_agent),
          ],
          verbose=True
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
  crew = SoftwareDevelopmentCrew(sys.argv[1])
  result = crew.run()
  print(result)

