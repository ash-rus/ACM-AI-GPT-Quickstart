import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


def assistant_prompt():
    return """You are a dog with strong philosophical opinions. You are very wise and will give out philosophical advice from the perspective of a dog."""  # Prompt given to the model

conversation=[{"role": "system", "content": assistant_prompt()}]    # The conversation is an array of messages
                                                                    # "system" messages are instructions given to the model
                                                                    # "user" messages are given by the person having the conversation
                                                                    # "assistant" messages are responses given by the model

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]                                    # Gets a "prompt" or "message" from the user
        conversation.append({"role": "user", "content": format(prompt)})   # Adds the user's message to the conversation array

        response = openai.ChatCompletion.create(                           # Creating a "response" object, which contains a response message from the model
            model="gpt-3.5-turbo",
            messages=conversation                                          # We pass in the conversation so far
        )

        conversation.append({"role": "assistant", "content": format(response['choices'][0]['message']['content'])}) # Adds the model's response to the conversation array
        return redirect(url_for("index", result=response['choices'][0]['message']['content']))                      # Redirects the user to the index page, with the model's response as a parameter

    result = request.args.get("result")
    return render_template("index.html", result=result)