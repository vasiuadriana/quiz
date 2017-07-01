from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Question
from .forms import QuestionForm


def index(request):
    question_list = Question.objects.all()
    template = loader.get_template('pyquiz/index.html')
    context = {
        'questions': [q for q in question_list]
    }
    return HttpResponse(template.render(context, request))


def question(request, question_id):
    question_details = get_object_or_404(Question, pk=question_id)
    question_form = QuestionForm()
    template = loader.get_template('pyquiz/question.html')
    context = {
        'question': question_details,
        'form': question_form
    }
    return HttpResponse(template.render(context, request))


def answer(request, question_id):
    template = loader.get_template('pyquiz/answer.html')
    context = {'answer': request.POST['answer']}
    return HttpResponse(template.render(context, request))
