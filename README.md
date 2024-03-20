# DCC Utils para Proyectos Django

## Descripción

Este proyecto provee utilidades para las Apps basadas en Django del DCC:

- [sso](docs/SSO.md): provee autenticación utilizando cuenta Mi Uchile mediante el uso de Upasaporte del Centro Ucampus.
- [events](docs/EVENTS.md): provee mensajería a través de mqtt y django signals para notificar cambios en entidades de negocio.
- [users](docs/USERS.md): extiende el usuario estándar de django para incluir información adicional de las personas desde el portal.

Debido a que este es un proyecto que está en constante mejora se recomienda incluir este proyecto como un submodulo en su repositorio, asegurándose que siempre apunte a la última versión de la rama **main** y crear un link simbólico de la App SSO a su proyecto Django. Puede ver un ejemplo de esto en [Django Boilerplate](https://github.com/DCC-FCFM-UCHILE/django-boilerplate).

```ps
~ git submodule add https://github.com/DCC-FCFM-UCHILE/django_utils
~ git submodule update --init
```

**NO UTILIZAR ESTE PROYECTO COMO BASE PARA CONSTRUIR SU APP.** 

Puede utilizar el [Django Boilerplate](https://github.com/DCC-FCFM-UCHILE/django-boilerplate) como referencia o base para construir un nuevo proyecto.
