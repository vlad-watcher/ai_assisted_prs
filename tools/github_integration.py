import requests
import os

def get_last_closed_pull_requests(github_repository: str) -> dict[str, list[str]]:
    """Build a function that accepts github repository string argument in a format 'owner/repository' and get 10 last closed pull requests from that repo.
    For every PR get all its commit messages texts.
    Function must return a dictionary where every key in the root is the PR number.
    And inside PR number key is 2 keys: title, commits
    """

    owner, repository = github_repository.split("/")
    url = f"https://api.github.com/repos/{owner}/{repository}/pulls?state=closed&per_page=5"
    headers = {"Authorization": f"Bearer {os.getenv('GH_TOKEN')}"}
    response = requests.get(url,headers=headers,timeout=30).json()

    # Filter only merged PRs
    response = [pr for pr in response if pr["merged_at"] is not None]

    pull_requests = {}
    try:
        for pr in response:
            pr_number = str(pr["number"])
            commits_url = pr["commits_url"]
            commits = requests.get(commits_url, headers=headers, timeout=30).json()
            commit_messages = [commit["commit"]["message"] for commit in commits]
            pull_requests[pr_number] = {
                "title": pr["title"],
                "commits": commit_messages,
                "pr_number": pr_number,
                "jira_key":"",
                "jira_description":""
            }
    except Exception as e:
        print(response)
        print(e)
    return pull_requests
