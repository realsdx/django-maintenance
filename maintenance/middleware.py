from maintenance import models
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse, reverse_lazy

class MaintenanceMiddleware(MiddlewareMixin):
    def should_redirect(self,request):
        if request.user.is_staff:
            return True
        if request.path.startswith("/admin"):
            return True
        else:
            return False

    def process_request(self,request):
        try:
            mode = models.MainteneceMode.objects.all().first()
            state = mode.status #state of mmode
        except Exception:
            return None
            
        if state:
            if self.should_redirect(request):
                return None
            else:
                maintenance_path = reverse('page_503')
                if not (request.path == maintenance_path):
                    return HttpResponseRedirect(maintenance_path,{})
                else:
                    return None
        else:
            return None