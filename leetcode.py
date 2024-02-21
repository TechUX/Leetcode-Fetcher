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

def skillstat(username):
    query = {"query":""" query skillStats($username: String!) { matchedUser(username: $username) { tagProblemCounts { advanced { tagName tagSlug problemsSolved } intermediate { tagName tagSlug problemsSolved } fundamental { tagName tagSlug problemsSolved } } } } """, "variables":{"username":username}, "operationName":"skillStats" }

    response = requests.post(url, headers=headers, json=query)
    
    if response.status_code != 200:
        return {"status":"error","message":"Unknown Error","code":response.status_code}

    try:
        if response.json()["data"]["matchedUser"]:
          return {"status":"ok","skillStats":response.json()["data"]["matchedUser"]}
        return {"status":"error","profile":"No profile found"}

    except json.JSONDecodeError as e:
        return {"status":"error","message":"JSON Decode Error"}

def contestranking(username):
    query = {"query":""" query userContestRankingInfo($username: String!) { userContestRanking(username: $username) { attendedContestsCount rating globalRanking totalParticipants topPercentage badge { name } } userContestRankingHistory(username: $username) { attended trendDirection problemsSolved totalProblems finishTimeInSeconds rating ranking contest { title startTime } } } """, "variables":{"username":username}, "operationName":"userContestRankingInfo"}

    response = requests.post(url, headers=headers, json=query)

    if response.status_code != 200:
        return {"status":"error","message":"Unknown Error","code":response.status_code}

    try:
        if "errors" in response.json() and response.json()["errors"][0]["message"] == "User matching query does not exist." :
          return {"status":"error","profile":"No profile found"}
        return {"status":"ok","contestRanking":response.json()["data"]["userContestRanking"]}

    except json.JSONDecodeError as e:
        return {"status":"error","message":"JSON Decode Error"}

def problemsolved(username):
    query = {"query":""" query userProblemsSolved($username: String!) { allQuestionsCount { difficulty count } matchedUser(username: $username) { problemsSolvedBeatsStats { difficulty percentage } submitStatsGlobal { acSubmissionNum { difficulty count } } } } ""","variables":{"username":username},"operationName":"userProblemsSolved"}

    response = requests.post(url, headers=headers, json=query)

    if response.status_code != 200:
        return {"status":"error","message":"Unknown Error","code":response.status_code}

    try:
        if "errors" in response.json() and response.json()["errors"][0]["message"] == "That user does not exist." :
            return {"status":"error","profile":"No profile found"}

        return {"status":"ok","problemSolved":{"submission":response.json()["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"], "beats":response.json()["data"]["matchedUser"]["problemsSolvedBeatsStats"]}}

    except json.JSONDecodeError as e:
        return {"status":"error","message":"JSON Decode Error"}

