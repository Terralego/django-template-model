# Versions

1.0.6           (2020-09-09)
----------------------------

* Support django 3.1


1.0.5           (2020-06-09)
----------------------------

* Simplify rendering

1.0.4           (2020-06-08)
----------------------------

* Handle text or binary based templates (Compatibility with django-template-engines)


1.0.3           (2020-06-05)
----------------------------

* Delete views / urls and useless restframework dependencies
* Now with loader config, Template are discoverable like any other template

1.0.2           (2020-06-05)
----------------------------

* Add python 3.8 and django 3.0 support
* Add loader to handle Django Template Engine support


1.0.1           (2019-09-24)
----------------------------

Update:

* mimetype and magic are no longer used


1.0.0
----------------------------

From now on, `Template` model contains:

* a name (`name`),
* a mime type (`mime_type`),
* a file (`template_file`),
* the date of its creation (`added`),
* the date of its last update (`updated`).

0.1.1
----------------------------

This package is compatible with `Django>=2.1.0,<3.0.0` et `djangorestframework>=3.8.0,<3.11.0`.

0.1.0
----------------------------

From now on, `Template` model contains:

* a name,
* a format,
* a content,
* the date of its creation,
* the date of its last update.

0.0.1
----------------------------

* `Template` model
* Admin site
* View set with an additional route to download a template
