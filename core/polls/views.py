from django.shortcuts import render


def index(request):
    context = {"latest_question_list": [
        {"id": 1, "question_text": f"What's new?", "pub_date": "2021-08-01"},
        {"id": 2, "question_text": "What's up?", "pub_date": "2021-08-02"},
        {"id": 3, "question_text": "What's next?", "pub_date": "2021-08-03"},
    ]}
    return render(request, "polls/index.html", context)
