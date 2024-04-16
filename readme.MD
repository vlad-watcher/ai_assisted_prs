## AI ASSISTED PR DESCRIPTIONS
This project is supposed to feed all information about last 10 Pull Requests to Gemini
and get meaningful and clear description about what was done in the task.

## GEMINI API KEY - REQUIRED
Can be created here: https://makersuite.google.com/app/apikey

## GITHUB ACCESS TOKEN
Can be created here: https://github.com/settings/tokens

### TOKEN PERMISSIONS
- repo
    - repo:status
    - repo:public_repo
- admin:org
    - read:org
- admin:enterprise
    - read:enterprise
- project
    - read:project

## ENVIRONMENT VARIABLES
- GEMINI_KEY - REQUIRED
- JIRA_EMAIL (your JIRA email) - Not mandatory
- JIRA_API_KEY - Not mandatory
- JIRA_SERVER - Not mandatory
- GH_TOKEN - Not mandatory if use only for public repos

## .ENV FILE
You can create a .env file in project root instead of adding environment variables directly
```
GEMINI_KEY=...
JIRA_EMAIL=...
JIRA_API_KEY=...
GH_TOKEN=...
```

## INSTALL REQUIREMENTS
```
pip install -r requirements.txt
```

## HOW TO RUN
```
python ai_prs.py --gh_repo simple-elf/allure-report-action
```

#### Optional key argument for Gemini Api Key
```
python ai_prs.py --gh_repo simple-elf/allure-report-action --prs 3 --gemini_key <your_key>
```