"""
def createOrder(request,pk):
   
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})

    context = {
        'form':form
    }
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'accounts/order_form.html',context)

"""