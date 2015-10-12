# from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from xxxxxxxx
#
# # Create your views here.
#
# def login(request):
#     if request.methon == 'POST':
#         # attempting to log in
#         username = request.POST['citizenname']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password= password)
#
#         if user is not None and user.is_active:
#             logoin(request, user)
#             return redirect('movie_detail')
#         else:
#             return render(request,
#                   'citizens/login.html',
#                   {'failed': True,
#                   "username": username})
#
#     return render(request,
#                   'citizens/login.html',
#                   {})
#
#
#
# @login_required
# etx.....
