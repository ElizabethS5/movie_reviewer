# At least three (3) class-based views
# All views are DRY with all helpers factored out to appropriate modules
# At least three database queryset methods used: all(), get(), filter()
# At least one view has additional arguments passed via url path
# All network requests have sufficient exception handling for 4xx and 5xx
# responses

from django.shortcuts import render  # , HttpResponseRedirect, reverse
# from django.contrib.auth import login
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.views import View


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {})
