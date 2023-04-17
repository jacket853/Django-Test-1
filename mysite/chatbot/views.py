from django.shortcuts import render
import openai

# Create our homepage
def home(request):

    if request.method == "POST":
        userQuestion = request.POST['question']

        # API code
        openai.api_key = "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"
        # create OpenAI instance
        openai.Model.list()
        # make a 'Completion' (I'll call it a request)
        # https://platform.openai.com/docs/api-reference/chat/create
        GPT_Response = openai.Completion.create(
            model="text-davinci-003", # text-davinci-003
            prompt=userQuestion,
            temperature=0.1,
            max_tokens=500, # set to 60 for default
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        GPT_Response = GPT_Response["choices"][0]["text"].strip()

        return render(request, "chatbot/home.html", {"userQuestion":userQuestion, "GPT_Response":GPT_Response})
    return render(request, "chatbot/home.html", {})
