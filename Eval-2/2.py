# You are given a list of employees and a list of projects, along with their skill requirements. Each employee has a set of skills denoted as a list of strings. Your goal is to create a function named allocate_projects that efficiently assigns projects to employees based on their skills while maximizing the utilization of available skills.

# The function should take two arguments: employees and projects, where:

# 1. employees is a list of dictionaries, each representing an employee's details like name, skills, and current project (initially set to None).

# 2. projects is a list of dictionaries, each representing a project's details including its name and required skills.

# The function should allocate a project to each employee such that the total number of utilized skills across all projects is maximized. An employee can only be assigned to one project, and a project can only be assigned to one employee. An employee can only be assigned a project if they possess all the required skills for that project.

# The function should return a list of dictionaries, each indicating the assignment of a project to an employee. Each dictionary should have the keys "employee" and "project" where the values are the names of the employee and project respectively.


def allocate_projects(employees,projects):
    assignment = []
    for project in projects:
        project_name=project["name"]
        project_skills=set(project["skills"])
        for employee in employees:
            if not employee["current_project"]:
                employee_skills=set(employee["skills"])
                if project_skills.issubset(employee_skills):
                    employee["current_project"]=project_name
                    assignment.append({"employee":employee["name"], "project":project_name})
                    break
    return assignment

employees=[
    {"name":"john","skills":["python","Database"],"current_project":None},
    {"name":"ema","skills":["java","Testing"],"current_project":None},
    {"name":"kelly","skills":["python","java"],"current_project":None}
    ]

projects=[
    {"name":"ProjectA","skills":["python","Database"]},
     {"name":"ProjectB","skills":["java","Testing"]},
      {"name":"ProjectC","skills":["python","java"]}
]
print(allocate_projects(employees,projects))
