from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, "blog/index.html", context={"site": "Stepik.org"})

def about(request):
    return render(request, "blog/about.html", context={"site": "Stepik"})

def user_name(request):
    profile_data = ['Павел', 45, '+79234567891', 'pavel@pavel.com']
    work_time = 5
    user_list = [{'name': 'Дмитрий', 'experience': 9},
                                {'name': 'Павел', 'experience': 5},
                                {'name': 'Алексей', 'experience': 3},
                                {'name': 'Иван', 'experience': 0},
                                {'name': 'Денис', 'experience': 2},
                                {'name': 'Игорь', 'experience': 7},
                                {'name': 'Руслан', 'experience': 1},
                                {'name': 'Евгений', 'experience': 4},
                                {'name': 'Андрей', 'experience': 2},
                                {'name': 'Николай', 'experience': 8}]
    sort_user_list = list(enumerate([i for i in user_list if i['experience'] <= 2], start=1))
    time = datetime.now()
    return render(request, 'blog/user_name.html', context={'work_time': work_time,
                                                           'profile_data': profile_data, 'site': 'Stepik',
                                                           'time': time, 'sort_user_list': sort_user_list})


