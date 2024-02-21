# Leetcode-Fetcher
A python flask API to fetch user details from Leetcode just by username

# Tech used
- python flask
- python requests
- graphql
- json

# Endpoints available

BASE_URL = 

|Endpoint | HTTP Method|Example|Description|
|-|-|-|-|
|/`username`|GET|/devesh75|return all info for user|
|/profile/`username`|GET|/profile/devesh75|return basic profile info for user|
|/languagestat/`username`|GET|/languagestat/devesh75|return stats of questions solved by different language|
|/skillstat/`username`|GET|/skillstat/devesh75|return stats of skills of user|
|/contestranking/`username`|GET|/contestranking/devesh75|return contest ranking of user|
|/problemsolved/`username`|GET|/problemsolved/devesh75|return number of questions solved|
|/badges/`username`|GET|/badges/devesh75|return badges hold by user|
|/calendar/`username`|GET|/calandar/devesh75|return active year, streak, etc of user|
|/submissions/`username`|GET|/submissions/devesh75|return last 20 submission of user|

