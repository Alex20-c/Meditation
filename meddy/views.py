from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Procedure,Profile
from .forms import ProcedureForm,ProfileForm,VoteForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
# from .serializer import ProfileSerializer,ProcedureSerializer

# Create your views here.

def home(request):
    all_procedure = Procedure.fetch_all_images()
    return render(request,"meddy/index.html",{"all_images":all_procedure})

@login_required(login_url='/accounts/login/')
def new_procedure(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProcedureForm(request.POST,request.FILES)
        if form.is_valid():
            user_image = form.save(commit=False)
            user_image.user = current_user
            user_image.save()
        return redirect('home')
    else:
        form = ProcedureForm()
    return render(request,"meddy/new_procedure.html",{"form":form})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.prof_user = current_user
            profile.profile_Id = request.user.id
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/new_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        logged_user = Profile.objects.get(prof_user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=logged_user)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'profile/edit_profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    procedure = Procedure.objects.filter(user = current_user)

    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile/profile.html',{'profile':prof,'procedure':procedure})

@login_required(login_url='/accounts/login/')
def procedure_review(request,procedure_id):
    try:
        single_procedure = Procedure.get_single_procedure(procedure_id)
        average_score = round(((single_procedure.steps + single_procedure.process)/3),2)
        if request.method == 'POST':
            vote_form = VoteForm(request.POST)
            if vote_form.is_valid():
                single_procedure.vote_submissions+=1
                if single_procedure.steps == 0:
                    single_procedure.steps = int(request.POST['steps'])
                else:
                    single_procedure.steps = (single_procedure.steps + int(request.POST['steps']))/2
                if single_procedure.process == 0:
                    single_procedure.process = int(request.POST['process'])
                else:
                    single_procedure.process = (single_procedure.process + int(request.POST['process']))/2
                
                single_procedure.save()
                return redirect('procedure_review',procedure_id)
        else:
            vote_form = VoteForm()

    except Exception as  e:
        raise Http404()
    return render(request,'meddy/procedure_review.html',{"vote_form":vote_form,"single_procedure":single_procedure,"average_score":average_score})
