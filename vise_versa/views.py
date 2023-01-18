from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    words_num = len(user_text.split())
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text, 'words_number': words_num,
                                            'reversedtext': reversed_text})
