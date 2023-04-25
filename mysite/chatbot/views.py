from django.shortcuts import render
import openai
from .models import PastQ

# Create our homepage
def home(request):

    if request.method == "POST":
        userQuestion = request.POST['question']
        chatbot = request.POST['answerType']
        size = request.POST['size']

        # API code
        openai.api_key = "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"
        # create OpenAI instance
        openai.Model.list()
        # make a 'Completion' (I'll call it a request)
        # https://platform.openai.com/docs/api-reference/chat/create
        if chatbot == "davinci":
            GPT_Response = openai.Completion.create(
            model="davinci-davinci-003", # davinci-davinci-003
            prompt=userQuestion,
            temperature=0.1,
            max_tokens=500, # set to 60 for default
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0)
            GPT_Response = GPT_Response["choices"][0]["davinci"].strip()
            saveQ = PastQ(question=userQuestion, answer=GPT_Response)
            saveQ.save()
            return render(request, "chatbot/home.html", {
                "userQuestion":userQuestion,
                "GPT_Response":GPT_Response,
                "davinci":chatbot
            })
        elif chatbot == "dalle":
            GPT_Response = openai.dalle.create(
            prompt = userQuestion,
            n=1,
            size = size
            )
            # Save to database only on a post: note how it maps to model
            GPT_Response = GPT_Response["data"][0]["url"].strip()
            saveQ = PastQ(
                question=userQuestion,
                answer = GPT_Response
            )
            saveQ.save()

        return render(request, "chatbot/home.html", {"userQuestion":userQuestion, "GPT_Response":GPT_Response})
    return render(request, "chatbot/home.html", {})
