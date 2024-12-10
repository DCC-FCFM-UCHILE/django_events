from braces.views import MessageMixin
from django.views.generic import View


class CoreMessageMixin(MessageMixin):
    def msg_success(self, msg, desc=None):
        self.messages.success(f"<span class='fw-bold'>{desc}:</span> {msg}" if desc else f"{msg}")

    def msg_info(self, msg, desc=None):
        self.messages.info(f"<span class='fw-bold'>{desc}:</span> {msg}" if desc else f"{msg}")

    def msg_warning(self, msg, desc=None):
        self.messages.warning(f"<span class='fw-bold'>{desc}:</span> {msg}" if desc else f"{msg}")

    def msg_error(self, msg, desc=None):
        self.messages.error(f"<span class='fw-bold'>{desc}:</span> {msg}" if desc else f"{msg}")

    def msg_guardado(self, msg=None):
        return self.msg_success(msg, desc="Guardado") if msg else self.msg_success("Guardado")

    def msg_eliminado(self, msg=None):
        return self.msg_success(msg, desc="Eliminado") if msg else self.msg_succes("Eliminado")

    def msg_requeridos(self):
        return self.msg_warning("Completa todos los datos requeridos")


class CoreModuleViewMixin(CoreMessageMixin, View):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
