[![Build Status](https://travis-ci.org/courtem/django-template-model.svg?branch=master)](https://travis-ci.org/courtem/django-template-model)
[![Maintainability](https://api.codeclimate.com/v1/badges/2e15c7ac17e66d1c8e16/maintainability)](https://codeclimate.com/github/courtem/django-template-model/maintainability)
[![codecov](https://codecov.io/gh/courtem/django-template-model/branch/master/graph/badge.svg)](https://codecov.io/gh/courtem/django-template-model)
![Python Version](https://img.shields.io/badge/python-%3E%3D%203.6-blue.svg)
![Django Version](https://img.shields.io/badge/django-%3E%3D%202.1-blue.svg)
![Rest Version](https://img.shields.io/badge/django--rest--framework-%3E%3D%203.10.0-blue)

# django-template-model

## Description

This application will allow you to store `odt`, `docx` or `html` templates in
your database. You will be able to manipulate them through a view set, enriched
with an additional route to download the template.

## Setup

Edit your settings file as follows:

```
INSTALLED_APPS = [
    ...
    template_model,
]
```

Then your urls file:

```
urlpatterns = [
    ...
    path('...', include('template_model.urls')),
]
```

## Routes

* `.../document-template/` (name: `template-list`, methods: `['get', 'post']`)
* `.../document-template/{pk}/` (name: `template-detail`,
  methods: `['get', 'update', 'patch', 'delete']`)
* `.../document-template/{pk}/content/` (name: `template-content`,
  methods: `['get']`)
