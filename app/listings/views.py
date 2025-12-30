from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing
from django.shortcuts import render

# def hello(request):
#     bands = Band.objects.all()
#     return HttpResponse(f"""
#         <h1>Hello Django !</h1>
#         <p>Mes groupes préférés sont :<p>
#         <ul>
#             <li>{bands[0].name}</li>
#             <li>{bands[1].name}</li>
#             <li>{bands[2].name}</li>
#         </ul>
# """) # cette vue utilise un anti-pattern

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

# def about(request):
#     return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def about(request):
    return render(request, 'listings/about.html')

# def listings(request):
#     all_listings = Listing.objects.all()  # récupère tous les objets Listing
#     listings_html = "<ul>"
#     for listing in all_listings:
#         listings_html += f"<li>{listing.title}</li>"  # crée un <li> pour chaque title
#     listings_html += "</ul>"

#     return HttpResponse(f"""
#         <h1>Listings</h1>
#         <p>Voici toutes les annonces :</p>
#         {listings_html}
#     """) # cette vue utilise un anti-pattern
    # cf: https://www.formation-django.fr/framework-django/vues-templates/

def listings(request):
    all_listings = Listing.objects.all()  # récupère tous les objets Listing
    return render(request, 'listings/listings.html', {'listings': all_listings})