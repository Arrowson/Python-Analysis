from watson_developer_cloud import ToneAnalyzerV3

userInput = input("Input Cover Letter: ")

tone_analyzer = ToneAnalyzerV3(
    url="https://gateway.watsonplatform.net/tone-analyzer/api",
    iam_apikey="2409uypSaECrApSnGEfl-KKHyCyXW6ppaBThMeo8Ckv0",
    version="2016-05-19"
)

response = tone_analyzer.tone(userInput, content_type="text/plain")

data = response.result["document_tone"]["tone_categories"][0]["tones"]
 
print("")
print("")
print("The higher the score for each aspect, the more of that tone is registered")
print("")
print("")
for piece in data:
    print(piece["tone_name"])
    print("          score: " , piece["score"]*100, "%")

