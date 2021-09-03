from django.shortcuts import redirect


def unaunthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/blog')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func


def aunthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return view_func(request, *args, **kwargs)
		else:
			return redirect('/aunthenticated')
	return wrapper_func
