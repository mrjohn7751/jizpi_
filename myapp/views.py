from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views import View
from .forms import ArticleElonForm, ArticleNewsForm, Qabul24Form, KorupsiyaForm
from .models import *
from django.conf import settings
from django.utils import translation

# Create your views here.


def set_language(request):
    user_language = request.GET.get('language', 'uz')
    if user_language not in dict(settings.LANGUAGES):
        user_language = 'uz'
    translation.activate(user_language)
    response = redirect('/')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response





def q2024(request):
    if request.method == 'POST':
        form = Qabul24Form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('q2024Success', pk=instance.pk)  # Redirect with the pk of the saved instance
    else:
        form = Qabul24Form()
    
    return render(request,'qabul2024/q2024.html', {'form': form})




def q2024info(request, pk):
    instance = get_object_or_404(ArticleQabul2024, pk=pk)
    
    # Safely access the URL of file5, handling the case where file5 is None
    file5_url = instance.file5.url if instance.file5 else None
    
    q2024 = ArticleQabul2024.objects.all()
    return render(request, 'qabul2024/q2024-info.html', {'q2024': q2024, 'instance': instance, 'file5_url': file5_url})


def q2024Success(request, pk):
    instance = get_object_or_404(ArticleQabul2024, pk=pk)
    file5_url = instance.file5.url if instance.file5 else None
    q2024 = ArticleQabul2024.objects.all()
    return render(request, 'qabul2024/q2024-success.html', {'q2024': q2024, 'instance': instance, 'file5_url': file5_url})









class home(LoginRequiredMixin, View):
    def get(self, request):
        # Ma'lumotlarni olib kelish
        Article_news = ArticleNews.objects.all()
        Article_elon = ArticleElon.objects.all()
        
        # Kontekst yaratish
        context = {
            'Article_news': Article_news,
            'Article_elon': Article_elon,
        }
        
        # Shablonni ko'rsatish
        return render(request, 'users/home.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request,'users/login.html')
        


def logout_user(request):
    logout(request)
    return redirect('index')  




######################################################################################
######################################################################################
# create uchun


def create_article_elon(request):
    if request.method == 'POST':
        form = ArticleElonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # yoki kerakli URL
    else:
        form = ArticleElonForm()
    return render(request, 'users/create_article_elon.html', {'form': form})



######################################################################################
######################################################################################
# create uchun



def create_article_news(request):
    if request.method == 'POST':
        form = ArticleNewsForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)  # Obyektni yaratish, lekin hozircha saqlamaslik
            article.save()  # Endi saqlang
            
            return redirect('home')  # yoki 'home' URL uchun kerakli argumentlar bering
    else:
        form = ArticleNewsForm()
    return render(request, 'users/create_article_news.html', {'form': form})


######################################################################################
######################################################################################
# delate uchun


def delete_article_news(request, pk):
    article = get_object_or_404(ArticleNews, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('home')  # Muvaffaqiyatli o'chirilgandan so'ng foydalanuvchini kerakli URLga yo'naltirish
    return render(request, 'users/delete_article_news.html', {'article': article})

def delete_article_elon(request, pk):
    article = get_object_or_404(ArticleElon, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('home')  # Muvaffaqiyatli o'chirilgandan so'ng foydalanuvchini kerakli URLga yo'naltirish
    return render(request, 'users/delete_article_elon.html', {'article': article})



################################################################################################


def video(request):
    return render(request,'news/video.html')


# Korupsiya
from .forms import KorupsiyaForm
from .models import Korupsiya

def create_korupsiya_article(request):
    korupsiya = Korupsiya.objects.all()  # Barcha korupsiya obyektlarini olish
    if request.method == 'POST':
        form = KorupsiyaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Kerakli URL manzilga yo'naltirish
    else:
        form = KorupsiyaForm()
    
    context = {
        'korupsiya': korupsiya,
        'form': form,
    }
    return render(request, 'users/create_korupsiya_article.html', context)


################################################################################################
################################################################################################
# delete koruptions
def delete_korupsiya_article(request, pk):
    article = get_object_or_404(Korupsiya, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('home')  # O'chirishdan keyin kerakli URLga yo'naltirish
    return render(request, 'users/delete_korupsiya_article.html', {'article': article})


################################################################################################

def trigger(request):
    return render(request,'erasmus/trigger/triger.html')

def pageET1(request):
    return render(request,'erasmus/trigger/page-tr1.html')

def pageET2(request):
    return render(request,'erasmus/trigger/page-tr2.html')

def pageET3(request):
    return render(request,'erasmus/trigger/page-tr3.html')

def pageET4(request):
    return render(request,'erasmus/trigger/page-tr4.html')
    
    
################################################################################################
################################################################################################
def debse(request):
    return render(request,'erasmus/debse/debse.html')

def pageED1(request):
    return render(request,'erasmus/debse/page-d1.html')

def pageED2(request):
    return render(request,'erasmus/debse/page-d2.html')

def pageED3(request):
    return render(request,'erasmus/debse/page-d3.html')

def pageED4(request):
    return render(request,'erasmus/debse/page-d4.html')




################################################################################################
################################################################################################




def update_article_news(request, pk):
    article = get_object_or_404(ArticleNews, pk=pk)
    if request.method == 'POST':
        form = ArticleNewsForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')  # yoki kerakli URLga yo'naltirish
    else:
        form = ArticleNewsForm(instance=article)
    return render(request, 'users/update_article_news.html', {'form': form})

def update_article_elon(request, pk):
    article = get_object_or_404(ArticleElon, pk=pk)
    if request.method == 'POST':
        form = ArticleElonForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')  # yoki kerakli URLga yo'naltirish
    else:
        form = ArticleElonForm(instance=article)  # Bu yerda ArticleElonForm ishlatiladi
    return render(request, 'users/update_article_elon.html', {'form': form})

######################################################################################



def index(request):
    ekranImg = ekranImages.objects.all()
    Article_news = ArticleNews.objects.all()
    Article_elon = ArticleElon.objects.all()

    context = {
        'ekranImg':ekranImg,
        'Article_news':Article_news,
        'Article_elon':Article_elon,
    }
    return render(request,'index.html',context)


def ax(request):
    return render(request,'news/axborot-xizmati.html')
    
    

def news(request):
    Article_news = ArticleNews.objects.all()
    paginator = Paginator(Article_news, 16)  # pageda 16 ta maqola korinib turadi
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request,'news/news.html', {'page_obj':page_obj} )


def news_detail(request,pk):
    Article_news = ArticleNews.objects.get(pk=pk)
    context = {
        'article':Article_news,
    }
    return render(request,'news/news-in.html',context)



def elon(request):
    Article_elon = ArticleElon.objects.all()
    paginator = Paginator(Article_elon, 16)  # pageda 16 ta maqola korinib turadi
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
    }
    return render(request,'news/elon.html',context)


def elon_detail(request,pk):
    Article_elon = ArticleElon.objects.get(pk=pk)
    context = {
        'Article_elon':Article_elon,
    }
    return render(request,'news/elon-in.html',context)



################################################################################################
# Instut hamma pagelari

def institut(request):
    return render(request,'institut/__institut.html')

def kengash(request):
    return render(request,'institut/__kengash.html')

def meyoriyHujjat(request):
    return render(request,'institut/__meyoriy-hujjat.html')

def institutPage_1(request):
    return render(request,'institut/instut-page1.html')

def institutPage_2(request):
    return render(request,'institut/instut-page2.html')

def institutPage_3(request):
    return render(request,'institut/instut-page3.html')

def institutPage_4(request):
    return render(request,'institut/instut-page4.html')

def institutPage_5(request):
    return render(request,'institut/instut-page5.html')

def institutPage_6(request):
    return render(request,'institut/instut-page6.html')

def institutPage_7(request):
    return render(request,'institut/instut-page7.html')

################################################################################################

def OTMkengash(request):
    return render(request,'institut/__kengash-in.html')

def kengash1920(request):
    return render(request,'institut/kengash_19-20.html')

def kengash2021(request):
    return render(request,'institut/kengash_20-21.html')

def kengash2122(request):
    return render(request,'institut/kengash_21-22.html')

def kengash2223(request):
    return render(request,'institut/kengash_22-23.html')

def kengash2324(request):
    return render(request,'institut/kengash_23-24.html')

################################################################################################

def vasiylik(request):
    return render(request,"institut/__vasiylik.html")

def vp1(request):
    return render(request,"institut/vasiylik-page-1.html")

def vp2(request):
    return render(request,"institut/vasiylik-page-2.html")


################################################################################################

def yoshOlimlar(request):
    return render(request,"institut/__yosh-olimlar.html")

def xotinQizlar(request):
    return render(request,"institut/__xotin-qizlar.html")

def ilmiyKengash(request):
    return render(request,"institut/__ilmiy-kengash.html")

################################################################################################

def mhPage1(request):
    return render(request,'institut/mh-page1.html')

def mhPage2(request):
    return render(request,'institut/mh-page2.html')

def mhPage3(request):
    return render(request,'institut/mh-page3.html')

def mhPage4(request):
    return render(request,'institut/mh-page4.html')

def mhPage5(request):
    return render(request,'institut/mh-page5.html')

def mhPage6(request):
    return render(request,'institut/mh-page6.html')

def mhPage7(request):
    return render(request,'institut/mh-page7.html')

def mhPage8(request):
    return render(request,'institut/mh-page8.html')

################################################################################################

def rektorat(request):
    return render(request, 'rektorat/rektorat.html')


def rektor(request):
    return render(request, 'rektorat/rektorat/rektor.html')

def prYoshlar(request):
    return render(request, 'rektorat/rektorat/pr-yoshlar.html')

def prOquv(request):
    return render(request, 'rektorat/rektorat/pr-oquv.html')

def prIlmiy(request):
    return render(request, 'rektorat/rektorat/pr-ilmiy.html')

def prMoliya(request):
    return render(request, 'rektorat/rektorat/pr-moliya.html')

def prXalqaro(request):
    return render(request, 'rektorat/rektorat/pr-xalqaro.html')


################################################################################################

def bolimlar(request):
    return render(request, 'rektorat/bolimlar/bolimlar.html')

def pageB1(request):
    return render(request, 'rektorat/bolimlar/page-b1.html')

def pageB2(request):
    return render(request, 'rektorat/bolimlar/page-b2.html')

def pageB3(request):
    return render(request, 'rektorat/bolimlar/page-b3.html')

def pageB4(request):
    return render(request, 'rektorat/bolimlar/page-b4.html')

def pageB5(request):
    return render(request, 'rektorat/bolimlar/page-b5.html')

def pageB6(request):
    return render(request, 'rektorat/bolimlar/page-b6.html')

def pageB7(request):
    return render(request, 'rektorat/bolimlar/page-b7.html')

def pageB8(request):
    return render(request, 'rektorat/bolimlar/page-b8.html')

def pageB9(request):
    return render(request, 'rektorat/bolimlar/page-b9.html')

def pageB10(request):
    return render(request, 'rektorat/bolimlar/page-b10.html')

def pageB11(request):
    return render(request, 'rektorat/bolimlar/page-b11.html')

def pageB12(request):
    return render(request, 'rektorat/bolimlar/page-b12.html')

def pageB13(request):
    return render(request, 'rektorat/bolimlar/page-b13.html')

def pageB14(request):
    return render(request, 'rektorat/bolimlar/page-b14.html')



################################################################################################
################################################################################################

def markazlar(request):
    return render(request, 'rektorat/markazlar/markaz.html')

def pageM1(request):
    return render(request, 'rektorat/markazlar/page-m1.html')


def pageM2(request):
    return render(request, 'rektorat/markazlar/page-m2.html')


def pageM3(request):
    return render(request, 'rektorat/markazlar/page-m3.html')


def pageM4(request):
    return render(request, 'rektorat/markazlar/page-m4.html')


def pageM5(request):
    return render(request, 'rektorat/markazlar/page-m5.html')

def pageM6(request):
    return render(request, 'rektorat/markazlar/page-m6.html')




################################################################################################
################################################################################################

def fakultet(request):
    return render(request, 'rektorat/fakultet/fakultet.html')   

def pageF1(request):
    return render(request, 'rektorat/fakultet/page-f1.html')   

def pageF2(request):
    return render(request, 'rektorat/fakultet/page-f2.html')   

def pageF3(request):
    return render(request, 'rektorat/fakultet/page-f3.html')   

def pageF4(request):
    return render(request, 'rektorat/fakultet/page-f4.html')   

def pageF5(request):
    return render(request, 'rektorat/fakultet/page-f5.html')   

def pageF6(request):
    return render(request, 'rektorat/fakultet/page-f6.html')   


################################################################################################
################################################################################################

def kafedra(request):
    return render(request, 'rektorat/kafedra/kafedra.html')   

def pageK1(request):
    return render(request,'rektorat/kafedra/page-k1.html')

def pageK2(request):
    return render(request,'rektorat/kafedra/page-k2.html')

def pageK3(request):
    return render(request,'rektorat/kafedra/page-k3.html')

def pageK4(request):
    return render(request,'rektorat/kafedra/page-k4.html')

def pageK5(request):
    return render(request,'rektorat/kafedra/page-k5.html')

def pageK6(request):
    return render(request,'rektorat/kafedra/page-k6.html')

def pageK7(request):
    return render(request,'rektorat/kafedra/page-k7.html')

def pageK8(request):
    return render(request,'rektorat/kafedra/page-k8.html')

def pageK9(request):
    return render(request,'rektorat/kafedra/page-k9.html')

def pageK10(request):
    return render(request,'rektorat/kafedra/page-k10.html')

def pageK11(request):
    return render(request,'rektorat/kafedra/page-k11.html')

def pageK12(request):
    return render(request,'rektorat/kafedra/page-k12.html')

def pageK13(request):
    return render(request,'rektorat/kafedra/page-k13.html')

def pageK14(request):
    return render(request,'rektorat/kafedra/page-k14.html')

def pageK15(request):
    return render(request,'rektorat/kafedra/page-k15.html')

def pageK16(request):
    return render(request,'rektorat/kafedra/page-k16.html')

def pageK17(request):
    return render(request,'rektorat/kafedra/page-k17.html')

def pageK18(request):
    return render(request,'rektorat/kafedra/page-k18.html')

def pageK19(request):
    return render(request,'rektorat/kafedra/page-k19.html')

def pageK20(request):
    return render(request,'rektorat/kafedra/page-k20.html')

def pageK21(request):
    return render(request,'rektorat/kafedra/page-k21.html')

def pageK22(request):
    return render(request,'rektorat/kafedra/page-k22.html')

def pageK23(request):
    return render(request,'rektorat/kafedra/page-k23.html')

def pageK24(request):
    return render(request,'rektorat/kafedra/page-k24.html')

def pageK25(request):
    return render(request,'rektorat/kafedra/page-k25.html')

def pageK26(request):
    return render(request,'rektorat/kafedra/page-k26.html')

def pageK27(request):
    return render(request,'rektorat/kafedra/page-k27.html')

def pageK28(request):
    return render(request,'rektorat/kafedra/page-k28.html')


################################################################################################
################################################################################################


def ilmiyFaoliyat(request):
    return render(request,'faoliyat/ilmiy-faoliyat/ilmiy.html')

def pageIF1(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if1.html')
 
def pageIF2(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if2.html')
 
def pageIF3(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if3.html')
 
def pageIF4(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if4.html')
 
def pageIF5(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if5.html')
 
def pageIF6(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if6.html')
 
def pageIF7(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if7.html')
 
def pageIF8(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if8.html')
 
def pageIF9(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if9.html')
 

 
def pageIF11(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if11.html')
 
def pageIF12(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if12.html')
 
def pageIF13(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if13.html')
 
def pageIF14(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if14.html')
 
def pageIF15(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if15.html')
 
def pageIF16(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if16.html')
    
def pageIF17(request):
    return render(request,'faoliyat/ilmiy-faoliyat/page-if17.html')
 
    
################################################################################################
################################################################################################


def oquvFaoliyat(request):
    return render(request,'faoliyat/oquv-faoliyat/oquv.html')

def pageOF1(request):
    return render(request,'faoliyat/oquv-faoliyat/page-of1.html')

def pageOF2(request):
    return render(request,'faoliyat/oquv-faoliyat/page-of2.html')

def pageOF3(request):
    return render(request,'faoliyat/oquv-faoliyat/page-of3.html')

def pageOF4(request):
    return render(request,'faoliyat/oquv-faoliyat/page-of4.html')

def pageOF5(request):
    return render(request,'faoliyat/oquv-faoliyat/page-of5.html')


################################################################################################
################################################################################################


def xalqaroFaoliyat(request):
    return render(request,'faoliyat/xalqaro-faoliyat/xalqaro.html')

def pageXF1(request):
    return render(request,'faoliyat/xalqaro-faoliyat/page-xf1.html')

def pageXF2(request):
    return render(request,'faoliyat/xalqaro-faoliyat/page-xf2.html')

def pageXF3(request):
    return render(request,'faoliyat/xalqaro-faoliyat/page-xf3.html')

def pageXF4(request):
    return render(request,'faoliyat/xalqaro-faoliyat/page-xf4.html')

def pageXF5(request):
    return render(request,'faoliyat/xalqaro-faoliyat/page-xf5.html')

def pageXF6(request):
    return render(request,'faoliyat/xalqaro-faoliyat/page-xf6.html')


################################################################################################
################################################################################################


def moliyaviyFaoliyat(request):
    return render(request,'faoliyat/moliyaviy-faoliyat/moliyaviy.html')

def pageMF1(request):
    return render(request,'faoliyat/moliyaviy-faoliyat/page-mf1.html')

def pageMF2(request):
    return render(request,'faoliyat/moliyaviy-faoliyat/page-mf2.html')

def pageMF3(request):
    return render(request,'faoliyat/moliyaviy-faoliyat/page-mf3.html')

def pageMF4(request):
    return render(request,'faoliyat/moliyaviy-faoliyat/page-mf4.html')

def pageMF5(request):
    return render(request,'faoliyat/moliyaviy-faoliyat/page-mf5.html')

def pageMF6(request):
    return render(request,'faoliyat/moliyaviy-faoliyat/page-mf6.html')

def pageMF7(request):
    return render(request,'faoliyat/moliyaviy-faoliyat/page-mf7.html')


################################################################################################
################################################################################################


def korupsiyaFaoliyat(request):
    articles = Korupsiya.objects.all()  # O'zgaruvchi nomini 'articles' deb o'zgartirdik
    return render(request, 'faoliyat/korupsiya/korupsiya.html', {'korupsiya': articles})  # kalit nomi 'korupsiya'

def korupsiya_detail(request, pk):
    article = get_object_or_404(Korupsiya, pk=pk)
    return render(request, 'korupsiya/korupsiya_copy.html', {'item': article})

def pageKF1(request):
    return render(request,'faoliyat/korupsiya/page-kf1.html')

def pageKF2(request):
    return render(request,'faoliyat/korupsiya/page-kf2.html')

################################################################################################
################################################################################################



def callCenter(request):
    return render(request,'qabul/call-center.html')

def bakalavr(request):
    return render(request,'qabul/bakalavr/bakalavr.html')

def pageBak1(request):
    return render(request,'qabul/bakalavr/page-b1.html')

def pageBak2(request):
    return render(request,'qabul/bakalavr/page-b2.html')

def pageBak3(request):
    return render(request,'qabul/bakalavr/page-b3.html')

def pageBak4(request):
    return render(request,'qabul/bakalavr/page-b4.html')

def pageBak5(request):
    return render(request,'qabul/bakalavr/page-b5.html')

def pageBak6(request):
    return render(request,'qabul/bakalavr/page-b6.html')

def pageBak7(request):
    return render(request,'qabul/bakalavr/page-b7.html')

def pageBak8(request):
    return render(request,'qabul/bakalavr/page-b8.html')

################################################################################################
################################################################################################

def magistr(request):
    return render(request,'qabul/magistr/magistr.html')

def pageQM1(request):
    return render(request,'qabul/magistr/page-m1.html')

def pageQM2(request):
    return render(request,'qabul/magistr/page-m2.html')

def pageQM3(request):
    return render(request,'qabul/magistr/page-m3.html')

def pageQM4(request):
    return render(request,'qabul/magistr/page-m4.html')

def pageQM5(request):
    return render(request,'qabul/magistr/page-m5.html')

def pageQM6(request):
    return render(request,'qabul/magistr/page-m6.html')

def pageQM7(request):
    return render(request,'qabul/magistr/page-m7.html')

def pageQM8(request):
    return render(request,'qabul/magistr/page-m8.html')

def pageQM9(request):
    return render(request,'qabul/magistr/page-m9.html')

################################################################################################
################################################################################################

def sirtqi(request):
    return render(request,'qabul/sirtqi/sirtqi.html')

def pageSirtqi1(request):
    return render(request,'qabul/sirtqi/page-sirtqi1.html')

def pageSirtqi2(request):
    return render(request,'qabul/sirtqi/page-sirtqi2.html')

def pageSirtqi3(request):
    return render(request,'qabul/sirtqi/page-sirtqi3.html')

def pageSirtqi4(request):
    return render(request,'qabul/sirtqi/page-sirtqi4.html')

def pageSirtqi5(request):
    return render(request,'qabul/sirtqi/page-sirtqi5.html')

def pageSirtqi6(request):
    return render(request,'qabul/sirtqi/page-sirtqi6.html')

def pageSirtqi7(request):
    return render(request,'qabul/sirtqi/page-sirtqi7.html')

def pageSirtqi8(request):
    return render(request,'qabul/sirtqi/page-sirtqi8.html')



################################################################################################
def xorijiyTalabalar(request):
    return render(request,'qabul/xorijiy-talabalar.html')
################################################################################################



def doktarantura(request):
    return render(request,'qabul/dokt/dokt.html')
        
def pageDOK1(request):
    return render(request,'qabul/dokt/page-dok1.html')
        
def pageDOK2(request):
    return render(request,'qabul/dokt/page-dok2.html')
        
def pageDOK3(request):
    return render(request,'qabul/dokt/page-dok3.html')
        
def pageDOK4(request):
    return render(request,'qabul/dokt/page-dok4.html')
        
def pageDOK5(request):
    return render(request,'qabul/dokt/page-dok5.html')
        
        
################################################################################################
################################################################################################

def qoshmaTalim(request):
    return render(request,'qabul/qoshmaTalim/qtalim.html')

def pageQT1(request):
    return render(request,'qabul/qoshmaTalim/page-qt1.html')

def pageQT2(request):
    return render(request,'qabul/qoshmaTalim/page-qt2.html')

def pageQT3(request):
    return render(request,'qabul/qoshmaTalim/page-qt3.html')

def pageQT4(request):
    return render(request,'qabul/qoshmaTalim/page-qt4.html')

def pageQT5(request):
    return render(request,'qabul/qoshmaTalim/page-qt5.html')

def pageQT6(request):
    return render(request,'qabul/qoshmaTalim/page-qt6.html')

def pageQT7(request):
    return render(request,'qabul/qoshmaTalim/page-qt7.html')

def pageQT8(request):
    return render(request,'qabul/qoshmaTalim/page-qt8.html')

def pageQT9(request):
    return render(request,'qabul/qoshmaTalim/page-qt9.html')

def pageQT10(request):
    return render(request,'qabul/qoshmaTalim/page-qt10.html')

        
################################################################################################
def texnikum(request):
    return render(request,'qabul/texnikum.html')
################################################################################################


def ikkiMutaxasislik(request):
    return render(request,'qabul/im/im.html')

def pageIM1(request):
    return render(request,'qabul/im/page-im1.html')

def pageIM2(request):
    return render(request,'qabul/im/page-im2.html')

def pageIM3(request):
    return render(request,'qabul/im/page-im3.html')

def pageIM4(request):
    return render(request,'qabul/im/page-im4.html')

def pageIM5(request):
    return render(request,'qabul/im/page-im5.html')

def pageIM6(request):
    return render(request,'qabul/im/page-im6.html')

def pageIM7(request):
    return render(request,'qabul/im/page-im7.html')

def pageIM8(request):
    return render(request,'qabul/im/page-im8.html')

def pageIM9(request):
    return render(request,'qabul/im/page-im9.html')

def pageIM10(request):
    return render(request,'qabul/im/page-im10.html')


################################################################################################
################################################################################################

def tB(request):
    return render(request,'talabalar/bakalavr/bakalavr.html')

def tBp1(request):
    return render(request,'talabalar/bakalavr/page-b1.html')

def tBp2(request):
    return render(request,'talabalar/bakalavr/page-b2.html')

def tBp3(request):
    return render(request,'talabalar/bakalavr/page-b3.html')

def tBp4(request):
    return render(request,'talabalar/bakalavr/page-b4.html')

def tBp5(request):
    return render(request,'talabalar/bakalavr/page-b5.html')

def tBp6(request):
    return render(request,'talabalar/bakalavr/page-b6.html')

def tBp7(request):
    return render(request,'talabalar/bakalavr/page-b7.html')

def tBp8(request):
    return render(request,'talabalar/bakalavr/page-b8.html')

def tBp9(request):
    return render(request,'talabalar/bakalavr/page-b9.html')

def tBp10(request):
    return render(request,'talabalar/bakalavr/page-b10.html')
    

def tBp11(request):
    return render(request,'talabalar/bakalavr/page-b11.html')

def tBp12(request):
    return render(request,'talabalar/bakalavr/page-b12.html')

def tBp13(request):
    return render(request,'talabalar/bakalavr/page-b13.html')



################################################################################################
################################################################################################


def tM(request):
    return render(request,'talabalar/magistr/_tm.html')

def tMp1(request):
    return render(request,'talabalar/magistr/page-m1.html')

def tMp2(request):
    return render(request,'talabalar/magistr/page-m2.html')

def tMp3(request):
    return render(request,'talabalar/magistr/page-m3.html')

def tMp4(request):
    return render(request,'talabalar/magistr/page-m4.html')

def tMp5(request):
    return render(request,'talabalar/magistr/page-m5.html')

def tMp6(request):
    return render(request,'talabalar/magistr/page-m6.html')

def tMp7(request):
    return render(request,'talabalar/magistr/page-m7.html')

def tMp8(request):
    return render(request,'talabalar/magistr/page-m8.html')

def tMp9(request):
    return render(request,'talabalar/magistr/page-m9.html')


def tMp10(request):
    return render(request,'talabalar/magistr/page-m10.html')

def tMp11(request):
    return render(request,'talabalar/magistr/page-m11.html')

def tMp12(request):
    return render(request,'talabalar/magistr/page-m12.html')


################################################################################################
def sirtqiT(request):
    return render(request,'talabalar/sirtqiT.html')
################################################################################################

def xt(request):
    return render(request,'talabalar/xt/xt.html')

def xtp1(request):
    return render(request,'talabalar/xt/page-xt1.html')

def xtp2(request):
    return render(request,'talabalar/xt/page-xt2.html')

def xtp3(request):
    return render(request,'talabalar/xt/page-xt3.html')

def xtp4(request):
    return render(request,'talabalar/xt/page-xt4.html')

def xtp5(request):
    return render(request,'talabalar/xt/page-xt5.html')

def xtp6(request):
    return render(request,'talabalar/xt/page-xt6.html')

################################################################################################
################################################################################################

def qt(request):
    return render(request,'talabalar/qt/qt.html')


def qtp1(request):
    return render(request,'talabalar/qt/page-xt1.html')

def qtp2(request):
    return render(request,'talabalar/qt/page-xt2.html')

def qtp3(request):
    return render(request,'talabalar/qt/page-xt3.html')

def qtp4(request):
    return render(request,'talabalar/qt/page-xt4.html')

def qtp5(request):
    return render(request,'talabalar/qt/page-xt5.html')

def qtp6(request):
    return render(request,'talabalar/qt/page-qt6.html')


def aloqa(request):
    return render(request,'aloqa/aloqa.html')

def bayroq(request):
    return render(request,'aloqa/bayroq.html')

def gerb(request):
    return render(request,'aloqa/gerb.html')

################################################################################################
################################################################################################
