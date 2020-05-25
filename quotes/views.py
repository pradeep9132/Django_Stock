from django.shortcuts import render, redirect
from .models import stock
from django.contrib import messages
from .forms import StockForm

# Create your views here.
# pk_4201a674bd1d4134ab399ba17fad6630

def home(request):
	# in home we are going to create a request to make connection with an API
	import requests # get data from internet source # pip install requests in Git Bash
	import json # java script object notation for parsing the requested data

#	return render(request, 'home.html',{})

	if request.method == 'POST':
		ticker = request.POST['ticker']
		#tick_val = nse.is_valid_code(ticker)

		#if (nse.is_valid_code(ticker)):
		from nsetools import Nse
		nse = Nse()
		
		api_request = nse.get_quote(ticker)

		try:		#api = json.loads(api_request.content) # parsing the requested data
			api = api_request
		except Exception as e:
			api = 'Error...'

		return render(request, 'home.html',{'api':api})
		#else:
		#	return render(request, 'home.html',{'ticker':"Enter a Ticker"})	
	else:
		return render(request, 'home.html',{'ticker':"Enter a Ticker"})

	#api_request = requests.get(" https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_4201a674bd1d4134ab399ba17fad6630")
	#api_request = requests.get("http://appfeeds.moneycontrol.com/jsonapi/market/indices&ind_id=1")

	#return render(request, 'home.html',{'api':api}) # dictionary comes into picture when requesting API data to get it printed

def about(request):
	return render(request, 'about.html',{})

def stocks(request):
	import requests # get data from internet source # pip install requests in Git Bash
	import json # java script object notation for parsing the requested data
	from nsetools import Nse

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request,("stock added"))
			return redirect('stocks')
	else:
		nse = Nse()
		ticker = stock.objects.all()
		output = []
		for ticker_item in ticker:			
			api_request = nse.get_quote(str(ticker_item)) # need to pass as String, otherwise error
			try:		#api = json.loads(api_request.content) # parsing the requested data
				api = api_request
				output.append(api)
			except Exception as e:
				api = 'Error...'

		return render(request, 'stocks.html',{'ticker':ticker, 'output':output})

def delete(request,stock_id):
	item = stock.objects.get(pk=stock_id) # get the item first from DB based on the DB ID assigned internally for each stock
	item.delete()
	messages.success(request,("Stock Deleted"))
	return redirect ('delete_stock')

def delete_stock(request):
	ticker = stock.objects.all()
	return render(request, 'delete_stock.html',{'ticker':ticker})