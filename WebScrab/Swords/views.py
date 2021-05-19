from django.shortcuts import render
import requests
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from .models import Words,Url
from django.contrib import messages


# Create your views here.
def frquent(request):


    return render(request,'Swords/frequency.html')


def result(request):
    if request.method == 'POST':
        nurl = request.POST['url']
        print(nurl)
        if Url.objects.filter(ur=nurl).exists():
            messages.info(request,'The data is coming from database ,Url alredy used !!')
            data= Words.objects.all().filter(url__ur=nurl).order_by('-number')
            print(data)
            return render(request, 'Swords/result.html', {'data': data})
        else:
            word = stopwords.words('english')
            r = requests.get(nurl)

            soup = BeautifulSoup(r.content, "html.parser")

            text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))

            m = (x.rstrip(punctuation).lower() for y in text for x in y.split() if x not in word)
            c = Counter(m)
            k = c.most_common(10)
            url_ins = Url.objects.create(ur=nurl)
            for key, value in k:
                wor = Words(word=key, number=value, url=url_ins)
                print("hii", key, value)
                wor.save()
            data = Words.objects.all().filter(url__ur=nurl).order_by('-number')
            messages.info(request, 'The data is Fresh, data is coming from Given Url !!')

            return render(request, 'Swords/result.html',{'data':data} )


    else:
        return render(request, 'Swords/result.html')


        # return render(request, 'Swords/result.html')

