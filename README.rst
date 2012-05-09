Introduction
============

``django-cms-lite`` is a package designed to dynamically expose Django
templates.

Requirements
============

Django 1.4 (it may work with older versions, but I haven't tested this)

Installation
============

Add ``cms_lite`` to your ``INSTALLED_APPS``.

Add cms_lite to your URLConf, using something like this::

  urlpatterns += patterns("",
      url(r"^", include("cms_lite.urls")),
  )


Usage
=====

Somewhere discoverable by your TEMPLATE_DIRS setting, include a
directory named cms_lite. All files therein will be exposed as per the
above URLConf setting.
