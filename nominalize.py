# coding: utf-8
#!/usr/bin/python3
#!flask/bin/python3
import os
import requests

def get_nom(text):
    pretext = "Nominalization: she died because she did not know the rules means her ignorance of the rules caused her death\nNominalization: she did not follow the instructions and she failed means her failure was a result of her ignorance of the instructions\nNominalization: she did not make the right decision and she was expelled means her expulsion was the result of her improper decision\nNominalization: he committed a sin and he was sent to the jail means his sinful act led him to the confinement\nNominalization: the roads were blocked with the traffic, she was late means her failure to arrive at the location on time was a consequence of her poor planning\nNominalization: the prices were increasing so we cannot afford to purchase the item means the increase in the price was the reason for not purchasing\n"
    nom = requests.post("https://api.ai21.com/studio/v1/j1-jumbo/complete",
        headers={"Authorization": "Bearer XXXX SIGN UP FOR AN API TOKEN XXXXXXXXXXXXXXXXXXXX"},
        json={
            "prompt": "{}{}".format(pretext,text),
            "numResults": 1,
            "maxTokens": 64,
            "temperature": 0.88,
            "topKReturn": 0,
            "topP":1,
            "countPenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "frequencyPenalty": {
                "scale": 225,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "presencePenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
          },
          "stopSequences":["↵"]
        }
    )
    return nom.json()['completions'][0]['data']['text']

