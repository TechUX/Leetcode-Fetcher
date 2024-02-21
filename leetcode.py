import requests
import json

url = "https://leetcode.com/graphql/"
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "",
    "Content-Type": "application/json",
    "baggage": "sentry-environment=production,sentry-release=7366c15b,sentry-transaction=%2Fu%2F%5Busername%5D,sentry-public_key=2a051f9838e2450fbdd5a77eb62cc83c,sentry-trace_id=cd58a4991f3d4ad082c1adf54451481a,sentry-sample_rate=0.03",
}

def profile(username):
    query = { "query": """ query userPublicProfile($username: String!) { matchedUser(username: $username) { username githubUrl twitterUrl linkedinUrl profile { ranking userAvatar realName aboutMe school websites countryName company jobTitle skillTags postViewCount postViewCountDiff reputation reputationDiff solutionCount solutionCountDiff categoryDiscussCount categoryDiscussCountDiff } contestBadge { name expired hoverText icon } } } """, "variables": { "username": username }, "operationName": "userPublicProfile" }

    response = requests.post(url, headers=headers, json=query)

    if response.status_code != 200:
        return {"status":"error","message":"Unknown Error","code":response.status_code}

    try:
        if response.json()["data"]["matchedUser"]:
          return {"status":"ok","profile":response.json()["data"]["matchedUser"]}
        return {"status":"error","profile":"No profile found"}
    except json.JSONDecodeError as e:
        return {"status":"error","message":"JSON Decode Error"}
    
def languagestat(username):
    query = {"query":""" query languageStats($username: String!) { matchedUser(username: $username) { languageProblemCount { languageName problemsSolved } } } """, "variables":{ "username":username }, "operationName":"languageStats" }

    response = requests.post(url, headers=headers, json=query)

    if response.status_code != 200:
        return {"status":"error","message":"Unknown Error","code":response.status_code}

    try:
        if response.json()["data"]["matchedUser"]:
          return {"status":"ok","languageStats":response.json()["data"]["matchedUser"]}
        return {"status":"error","profile":"No profile found"}

    except json.JSONDecodeError as e:
        return {"status":"error","message":"JSON Decode Error"}
