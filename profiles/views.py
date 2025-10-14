from django.shortcuts import render


def profile(request):
    """Display the user's profile."""

    template = 'profiles/profile.html'
    content = {}

    return render(request, template, context)
