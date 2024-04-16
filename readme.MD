## GEMINI API KEY
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
- GEMINI_KEY
- JIRA_EMAIL (your JIRA email)
- JIRA_API_KEY
- GH_TOKEN

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