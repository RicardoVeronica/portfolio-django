# Django based Portfolio Project

Simple portfolio project made with Django using simple GET API endpoints for retrieval. Complete project is in Django rest framework browsable api...

### Technologies Used

This project uses my personal stack to work:

* Django - Python Web framework
  * Django models
  * Django admin
  * Context processors
  * django-ckeditor
* Django Rest Framework - Python API framework for create rest API's
  * Class Based Views
  * Serializers
  * custom permissions
* Divio Cloud - Web platform to deploy projects easily
* Docker - Container based virtual environment for Django projects
* Git and Github - Version control

[This project live](https://portfolio-django.us.aldryn.io/)

### Run locally

```sh
$ docker-compose up
# And go to 0.0.0.0:8000
`````````

### For API

For listing all projects or to post a project in Browsable API, go to:

[Endpoint Get list projects](https://portfolio-django.us.aldryn.io/api/)

For details, updates or deletion of a project, go to: (Protected with custom permission)

[Endpoint Get detail project](https://portfolio-django.us.aldryn.io/api/project/1/)
