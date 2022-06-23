from django.shortcuts import render
from .forms import InputForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        masterString = request.POST['mastersrting']
        stringOne = request.POST['string1']
        stringTwo = request.POST['string2']
        stringThree = request.POST['string3']
        stringFour = request.POST['string4']
        result = _can_word_made(masterString, stringOne, stringTwo, stringThree, stringFour)
        context ={}
        context['data']=result     

        return render(request, 'index.html', context)
    if request.method == 'GET':  
        context ={}
        context['form']= InputForm()
        return render(request, 'index.html', context)



def _can_word_made(masterString, stringOne, stringTwo, stringThree, stringFour) :
    masterStringArray = list(masterString)
    isStrOne = 'Yes'
    isStrTwo = 'Yes' 
    isStrThree = 'Yes'
    isStrFour = 'Yes'
    for str in stringOne:
        if(str in masterStringArray):
            masterStringArray.remove(str)
        else :
            isStrOne = 'No'
            
    for str in stringTwo:
        if(str in masterStringArray):
            masterStringArray.remove(str)
        else :
            isStrTwo = 'No'
            
    for str in stringThree:
        if(str in masterStringArray):
            masterStringArray.remove(str)
        else :
            isStrThree = 'No'
    
    for str in stringFour:
        if(str in masterStringArray):
            masterStringArray.remove(str)
        else :
            isStrFour = 'No'
    
    result = []
    result.append(stringOne + ':' + isStrOne)
    result.append(stringTwo + ':' + isStrTwo)
    result.append(stringThree + ':' + isStrThree)
    result.append(stringFour + ':' + isStrFour)
    return result;