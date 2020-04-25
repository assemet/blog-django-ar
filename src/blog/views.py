from django.shortcuts import render

# Create your views here.
posts =[
            {
            'title': 'التدوينه الاولي',
            'content': 'نص التدوينه الاولي كنص تجريبي',
            'post_date': '15-3-2019',
            'author': 'Ahmad Abouissa'
            },

            {
            'title': 'التدوينه الثانيه',
            'content': 'نص التدوينه الاولي كنص تجريبي',
            'post_date': '15-3-2019',
            'author': 'Ahmad Abouissa'
            },
            {
            'title': 'التدوينه الثالثه',
            'content': 'نص التدوينه الاولي كنص تجريبي',
            'post_date': '15-3-2019',
            'author': 'Ahmad Abouissa'
            },
            {
            'title': 'التدوينه الرابعه',
            'content': 'نص التدوينه الاولي كنص تجريبي',
            'post_date': '15-3-2019',
            'author': 'Ahmad Abouissa'
            },
]
def home(request):
    context={
    'title': 'الصفحه الرئيسيه',
    'posts': posts
        
    }
    return render(request, 'blog/index.html',context)
