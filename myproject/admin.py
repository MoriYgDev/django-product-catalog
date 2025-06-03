from django.contrib.admin import AdminSite
from django.utils.translation import activate

class EnglishAdminSite(AdminSite):
    def each_context(self, request):
        # Activate English language for this request/context
        activate('en')
        # Optionally, you can set request.LANGUAGE_CODE here as well if middleware isn't doing it
        # request.LANGUAGE_CODE = 'en' 
        return super().each_context(request)

# Instantiate your custom admin site
admin_site = EnglishAdminSite(name='myadmin')