from django.shortcuts import render,redirect
from django.views import View
from customer.models import MenuItem, OrderModel
from django.http import HttpResponse

class Index(View):
    def get(self,request, *args , **kwargs):
        return render(request,'customer/index.html')

class About(View):
    def get(self,request, *args, **kwargs):
        return render(request,'customer/about.html')
    
class Order(View):
    def get(self,request, *args, **kwargs):
        Biriyani = MenuItem.objects.filter(category__name__contains='Biriyani')
        North_Indian = MenuItem.objects.filter(category__name__contains='North Indian')
        Chinese = MenuItem.objects.filter(category__name__contains='Chinese')
        Ice_Creams = MenuItem.objects.filter(category__name__contains='Ice Creams')
        Cakes_Bakery = MenuItem.objects.filter(category__name__contains='Cakes & Bakery')
        Dosa = MenuItem.objects.filter(category__name__contains='Dosa')
        Arabic = MenuItem.objects.filter(category__name__contains='Arabic')
        Juices_Shakes = MenuItem.objects.filter(category__name__contains='Juices_Shakes')


        context = {

            'Biriyani':Biriyani,
            'Juices_Shakes': Juices_Shakes,
            'North Indian': North_Indian,
            'Chinese':Chinese,
            'Ice Creams': Ice_Creams,
            'Cakes & Bakery': Cakes_Bakery,
            'Dosa': Dosa,
            'Arabic': Arabic
        }

        return render (request, 'customer/order.html',context)

    def post(self, request, *args, **kwargs):
        name= request.POST.get('name')
        email= request.POST.get('email')
        street= request.POST.get('street name')
        city= request.POST.get('City')
        state= request.POST.get('State')
        zip_code= request.POST.get('Zip Code')
        
        order_items={
            'items':[]
        }
        items= request.POST.getlist('items[]')

        for item in items:
            menu_item= MenuItem.objects.get(pk__contains=int(item))
            item_data={
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }
            order_items['items'].append(item_data)
        totalprice=0
        item_ids= []

        for item in order_items['items']:
            totalprice += item['price']
            item.ids.append(item['id'])

        order =OrderModel.objects.create(
            price=totalprice,
            name=name,
            email=email,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code)
        order.item.add(*item_ids)

        context={
            'items': order_items['items'],
            'price': totalprice
        }

        return redirect('Orderconfirmation',pk=order.pk)
class OrderConfirmation(View):
    def get(self, request, pk,*args,**kwargs):
        order=OrderModel.objects.get(pk = pk)

        context={
            'pk' : order.pk,
            'items': order.items,
            'price':order.price,
        }

        return HttpResponse (request, 'customer/order_confirmation.html',context)
    

    def get(self, request,pk,*args,**kwargs):
        print(request.body)

class Search(View):
    def get(self,request,*args,**kwargs):
        if request.method=='GET':
            query=request.GET.get('query')
            name = MenuItem.objects.all().filter(category__name__contains='query')
                #North_Indian = MenuItem.objects.filter(category__name__contains='North Indian')
                #Chinese = MenuItem.objects.filter(category__name__contains='Chinese')
                #Ice_Creams = MenuItem.objects.filter(category__name__contains='Ice Creams')
                #Cakes_Bakery = MenuItem.objects.filter(category__name__contains='Cakes & Bakery')
                #Dosa = MenuItem.objects.filter(category__name__contains='Dosa')
                #Arabic = MenuItem.objects.filter(category__name__contains='Arabic')
                #Juices_Shakes = MenuItem.objects.filter(category__name__contains='Juices_Shakes')
                #price=MenuItem.objects.filter(price__icontains=query)

            return render(request, 'customer/search.html',{'name':name})
                

            #else:
               # print("No such item in the menu")
                #return HttpResponse(request, 'customer/search.html',{})
                


###class OrderPayConfirmation(View):
 ##   def get (self,request, *args, **kwargs):
   ##     return render(request,'custr')