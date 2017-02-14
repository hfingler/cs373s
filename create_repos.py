import os
import re
import subprocess

#easy_install3 PyGithub
try:
    from github import Github
except:
    print("Script requires PyGithub; run easy_install3 PyGithub")

organization_name = "cs373c-spring-2017"

def create_org_repo(api_org, name, students_github_id):
    repo = api_org.create_repo(name, private=True)
    for name in students_github_id:
        repo.add_to_collaborators(name)

if __name__ == "__main__":
    user = input("Github user: ")
    pw = input("Github password: ")
    github_api = Github(user, pw)
    org = github_api.get_organization(organization_name)
    create_org_repo(org, "test-repo3", ["hfingler", "renfuuu"])
