from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("I am Django Server")

def home(request):

    people = [
        {'name': 'Anshul', 'age': 29},
        {'name': 'Bhupesh', 'age': 15},
        {'name': 'Manish', 'age': 56},
        {'name': 'Mohan', 'age': 12},
        {'name': 'Vivek', 'age': 26}
    ]

    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste eos sapiente nesciunt expedita ullam molestiae veritatis vitae error alias nisi reiciendis obcaecati impedit veniam culpa, officiis ex, quas quia modi necessitatibus, assumenda facilis qui labore! Consequuntur sapiente est dolore mollitia, beatae ducimus iusto excepturi exercitationem, fugiat illo modi esse eos quas. Aperiam illum asperiores ad nostrum, fugit ex a minima perferendis obcaecati architecto et facilis adipisci accusantium odio doloremque dolorem! Praesentium delectus cupiditate ipsum fugiat fuga ducimus placeat voluptatum quos assumenda? Magnam sed beatae ea non dolorum nemo fuga quaerat dignissimos, quisquam, odio sint, perspiciatis ipsam nam minus nesciunt delectus?"""

    return render(request, "index.html", context= {'page': 'Django Demo', 'people': people, 'text': text})
 

def about(request):
    context = {'page' : 'About'}
    return render(request, "about.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "contact.html", context)

