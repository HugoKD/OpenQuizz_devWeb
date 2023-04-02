from django.shortcuts import render, redirect
from .models import Question, Quizz
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import json as json

@login_required
def dashboard(request):
    if request.method == 'POST':
        checkbox = request.POST.getlist('choice')
        enonce = request.POST.get('enonce')
        if 'qcm' in checkbox:
            choix1 = request.POST.get('choix1')
            choix2 = request.POST.get('choix2')
            choix3 = request.POST.get('choix3')
            choix4 = request.POST.get('choix4')
            reponseqcm = request.POST.get('reponseqcm')
            newquestion = Question(pseudo=str(request.user.username) ,enonce=enonce, reponse1=choix1, reponse2=choix2, reponse3=choix3, reponse4=choix4, reponseVrai=reponseqcm, qcm=True)
            newquestion.save()
        else:
            reponselongue = request.POST.get('reponselongue')
            newquestion = Question(pseudo=str(request.user.username), enonce=enonce, reponse=reponselongue)
            newquestion.save()

        return redirect('/dashboard/')
    quizzs = Quizz.objects.all().filter(pseudo=str(request.user.username))
    for k in range(len(quizzs)):
        quizzs[k].numero = k
        quizzs[k].save()


    context = {
        "quizzs":quizzs,
    }
    return render(request, "administrateur/dashboard.html", context)


#reste à rendre required au moins deux du qcm et la réponse selon le mode


def suppression(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        quizzsupp = Quizz.objects.all().filter(pseudo=str(request.user.username)).filter(numero=numero)
        quizzsupp.delete()
        return redirect("/dashboard/")

    else:
        questions = Question.objects.all().filter(pseudo=str(request.user.username))
        for i in range(len(questions)):
            questions[i].numero = i
            questions[i].save()
        quizzs = Quizz.objects.all().filter(pseudo=str(request.user.username))
        for k in range(len(quizzs)):
            quizzs[k].numero = k
            quizzs[k].save()


        context = {
            "questions": questions,
            "quizzs": quizzs,
        }
        return render(request, "administrateur/dashboard.html", context)



def creation_de_quizz(request):
    questions = Question.objects.all().filter(pseudo=str(request.user.username))
    for i in range(len(questions)):
        questions[i].numero = i
        questions[i].save()
    context = {
        "questions": questions
    }
    return render(request, "administrateur/creationQuizz.html", context)

def enregistrement(request):
    if request.method == 'POST':
        liste = request.POST.get('liste')
        time = request.POST.get('timer')

        classementdisplay =request.POST.get('classementdisplay')
        if classementdisplay=="true":
            classementdisplay = True
        else:
            classementdisplay = False

        stocker = request.POST.get('stocker')
        if stocker=="true":
            stocker = True
        else:
            stocker = False

        mode = request.POST.get('mode')
        name = request.POST.get('name')
        liste_questions = ""
        questions = Question.objects.all().filter(pseudo=str(request.user.username))
        for question in questions:
            if str(question.numero) in liste:
                liste_questions += str(question.id) +', '
        newQuizz = Quizz(pseudo=str(request.user.username),name=name, mode=mode, afficher=classementdisplay, timer=time, stocker=stocker, questions=liste_questions)
        newQuizz.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/dashboard/")
    else:
        quizzs = Quizz.objects.all().filter(pseudo=str(request.user.username))
        for k in range(len(quizzs)):
            quizzs[k].numero = k
            quizzs[k].save()

        context = {
            "quizzs": quizzs,
        }
        return render(request, "administrateur/dashboard.html", context)



def banquequestions(request):
    if request.method == 'POST':
        checkbox = request.POST.getlist('choice')
        enonce = request.POST.get('enonce')
        if 'qcm' in checkbox:
            choix1 = request.POST.get('choix1')
            choix2 = request.POST.get('choix2')
            choix3 = request.POST.get('choix3')
            choix4 = request.POST.get('choix4')
            reponseqcm = request.POST.get('reponseqcm')
            newquestion = Question(pseudo=str(request.user.username), enonce=enonce, reponse1=choix1, reponse2=choix2,
                                   reponse3=choix3, reponse4=choix4, reponseVrai=reponseqcm, qcm=True)
            newquestion.save()
        else:
            reponselongue = request.POST.get('reponselongue')
            newquestion = Question(pseudo=str(request.user.username), enonce=enonce, reponse=reponselongue)
            newquestion.save()

        return redirect('/banque-question/')
    questions = Question.objects.all().filter(pseudo=str(request.user.username))
    for i in range(len(questions)):
        questions[i].numero = i
        questions[i].save()

    context = {
        "questions": questions,
    }
    return render(request, 'administrateur/banquequestions.html', context)


def suppression_question(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        questionsupp = Question.objects.all().filter(pseudo=str(request.user.username)).filter(numero=numero)
        questionsupp.delete()
        return redirect("/banque-question/")

    else:
        questions = Question.objects.all().filter(pseudo=str(request.user.username))
        for i in range(len(questions)):
            questions[i].numero = i
            questions[i].save()()

        context = {
            "questions": questions,
        }
        return render(request, "administrateur/banquequestions.html", context)



def modifierquizz(request, id):
    if request.method == 'POST':

        quizz = Quizz.objects.get(id=id)
        liste = request.POST.get('liste')
        time = request.POST.get('timer')

        classementdisplay = request.POST.get('classementdisplay')
        if classementdisplay == "true":
            classementdisplay = True
        else:
            classementdisplay = False

        stocker = request.POST.get('stocker')
        if stocker == "true":
            stocker = True
        else:
            stocker = False

        mode = request.POST.get('mode')
        name = request.POST.get('name')
        liste_questions = ""
        questions = Question.objects.all().filter(pseudo=str(request.user.username))
        for question in questions:
            if str(question.numero) in liste:
                liste_questions += str(question.id) + ', '
        quizz.questions = liste_questions
        if time != '':
            quizz.timer = time
        quizz.stocker = stocker
        quizz.afficher = classementdisplay
        quizz.mode = mode
        if name != '':
            quizz.name = name
        quizz.save()
        return redirect('/dashboard/')


    quizz = Quizz.objects.all().filter(pseudo=str(request.user.username)).filter(id=id)[0]
    questions = Question.objects.all().filter(pseudo=str(request.user.username))
    liste_id = ''
    for i in range(len(questions)):
        questions[i].numero = i
        questions[i].save()
        liste_id += str(questions[i].id)+', '
    context = {
        "questions": questions,
        "quizz":quizz,
        "liste_id":liste_id,
    }
    return render(request, "administrateur/modifierquizz.html", context)