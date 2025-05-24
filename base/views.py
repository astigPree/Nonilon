from django.shortcuts import render
from django.http import JsonResponse


from . import models
# Create your views here.

def homePage(request):
    context = {}
    
    context['programmingLanguages'] = models.ProgrammingLanguage.objects.all()
    
    context['otherLanguages'] = models.OtherLanguage.objects.all()
    
    context['usedFrameWorks'] = models.UsedFrameWork.objects.all()
    
    context['usedLibraries'] = models.UsedLibrary.objects.all()
    
    context['usedSoftwares'] =  models.UsedSoftware.objects.all()
    
    context['softwareProjects'] = models.SoftwareProject.objects.all()
    
    context['hardwareProjects'] = models.HardwareProject.objects.all()
    
    clients = models.Client.objects.filter(is_used=True)
    if clients:
        context['clients'] = clients[::-1]
    else:
        context['clients'] = []
        
    return render(request, "portfolio/index.html" , context=context)


def submitTestimony(request):
    if request.method == 'POST':
        
        client_code = request.POST.get('client_code')
        name = request.POST.get('name')
        testimony = request.POST.get('testimony')
        rating = request.POST.get('rating')
        
        # Checking if all fields are required
        if not client_code or not name or not testimony or not rating:
            return JsonResponse({
                'message': 'All fields are required'
            }, status=400)
        
        if len(str(client_code)) > 15 :
            return JsonResponse({
                'message': 'Client code is too long'
            }, status=400)
        
        if len(str(name)) > 15 :
            return JsonResponse({
                'message': 'Name is too long'
            }, status=400)
        
        if len(str(testimony)) > 335 :
            return JsonResponse({
                'message': 'Testimony is too long'
            }, status=400)
        
        if str(rating).isdigit() == False:
            return JsonResponse({
                'message': 'Rating must be a number'
            }, status=400)
        
        if int(rating) > 5 or int(rating) < 0 :
            return JsonResponse({
                'message': 'Rating must be between 0 and 5'
            }, status=400)    
        
        # Saving to database
        client = models.Client.objects.filter(client_code=client_code).first()
        
        if not client:
            return JsonResponse({
                'message': 'Registered client not found'
            },status=400)
        
        
        if client.is_used == True:
            return JsonResponse({
                'message': 'Client already used the testimony'
            },status=400)
        
        client.is_used = True
        client.name = str(name)
        client.testimony = str(testimony)
        client.rating = int(rating)
        client.save()
        
        return JsonResponse({
            'message': 'Thank you for your testimony',
            'client_name': name,
            'client_testimony': testimony,
            'client_rating': rating
        },status=200)
        
        
    
    return JsonResponse({
        'message': 'Has error in submitting your testimony'
        }, status=400)