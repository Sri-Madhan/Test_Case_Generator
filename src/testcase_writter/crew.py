from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TestcaseWritter():
	"""TestcaseWritter crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	# @agent
	# def researcher(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['researcher'],
	# 		verbose=True
	# 	)

	# @agent
	# def reporting_analyst(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['reporting_analyst'],
	# 		verbose=True
	# 	)
	
	@agent
	def test_case_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['test_case_generator'],
			verbose=True,
			allow_delegation=True
		)
	
	@agent
	def edge_case_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['edge_case_analyzer'],
			verbose=True,
			allow_delegation=True
		)

	@agent
	def expected_output_predictor(self) -> Agent:
		return Agent(
			config=self.agents_config['expected_output_predictor'],
			verbose=True,
			allow_delegation=True
		)
	
	@agent
	def test_coverage_evaluator(self) -> Agent:
		return Agent(
			config=self.agents_config['test_coverage_evaluator'],
			verbose=True,
			allow_delegation=True
		)
	
	@agent
	def test_case_documentation(self) -> Agent:
		return Agent(
			config=self.agents_config['test_case_documentation'],
			verbose=True,
			allow_delegation=True
		)
	
	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# # https://docs.crewai.com/concepts/tasks#overview-of-a-task
	# @task
	# def research_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['research_task'],
	# 	)

	# @task
	# def reporting_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['reporting_task'],
	# 		output_file='report.md'
	# 	)

	
	
	@task
	def test_case_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['test_case_generation_task'],
			agent=self.test_case_generator(),
			output_file='test_cases.json'
		)

	@task
	def edge_case_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['edge_case_analysis_task'],
			# context=[test_case_task],
			agent=self.edge_case_analyzer(),
			output_file='edge_cases.json'
	)

	@task
	def expected_output_prediction_task(self) -> Task:
		return Task(
			config=self.tasks_config['expected_output_prediction_task'],
			# context=[edge_case_task],
			agent=self.expected_output_predictor(),
			output_file='expected_outputs.json'
	)

	@task
	def coverage_evaluation_task(self) -> Task:
		return Task(
			config=self.tasks_config['coverage_evaluation_task'],
			# context=[expected_output_task],
			agent=self.test_coverage_evaluator(),
			output_file='coverage_outputs.json'
	)

	@task
	def documentation_task(self) -> Task:
		return Task(
			config=self.tasks_config['documentation_task'],
			# context=[documentation_task],
			agent=self.test_case_documentation(),
		    output_file='final_tc.json'
	)



	@crew
	def crew(self) -> Crew:
		"""Creates the TestcaseWritter crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge
			# Instantiate tasks
		# tasks_obj = TestcaseWritter()

		# # Create tasks and pass dependencies
		# test_case_task = tasks_obj.test_case_generation_task()
		# edge_case_task = tasks_obj.edge_case_analysis_task(self,test_case_task)  # `context` receives `test_case_task`
		# expected_output_task = tasks_obj.expected_output_prediction_task(edge_case_task)  # `context` receives `edge_case_task`
		# reporting_task = tasks_obj.reporting_task(expected_output_task)  

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
