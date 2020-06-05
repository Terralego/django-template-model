[![Build Status](https://travis-ci.org/Terralego/django-template-model.svg?branch=master)](https://travis-ci.org/Terralego/django-template-model)
[![PyPI version](https://badge.fury.io/py/django-template-model.svg)](https://badge.fury.io/py/django-template-model)
[![Maintainability](https://api.codeclimate.com/v1/badges/2e15c7ac17e66d1c8e16/maintainability)](https://codeclimate.com/github/courtem/django-template-model/maintainability)
[![codecov](https://codecov.io/gh/Terralego/django-template-model/branch/master/graph/badge.svg)](https://codecov.io/gh/courtem/django-template-model)
![Python Version](https://img.shields.io/badge/python-%3E%3D%203.6-blue.svg)
![Django Version](https://img.shields.io/badge/django-%3E%3D%202.2-blue.svg)

# django-template-model

## Description

This application will allow you to store templates in
your database, and discovering with any Template Engine

## Setup

Edit your settings file as follows:

```
INSTALLED_APPS = [
    ...
    template_model,
]
```

```
TEMPLATES = [
  {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [ # your template dirs here
      ],
      'APP_DIRS': False,  # Disable auto discovering
      'OPTIONS': {
          'context_processors': [
              'django.contrib.auth.context_processors.auth',
              'django.template.context_processors.debug',
              'django.template.context_processors.i18n',
              'django.template.context_processors.media',
              'django.template.context_processors.static',
              'django.template.context_processors.tz',
              'django.contrib.messages.context_processors.messages',
              'django.template.context_processors.request',
          ],
          'loaders': [
              'django.template.loaders.filesystem.Loader',
              'django.template.loaders.app_directories.Loader',
              # add loader here if you want to use it with this backend
              'template_model.loader.Loader',
          ],
      },
  },
```

