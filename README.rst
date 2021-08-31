=====
Translation
=====

translation is a Django app works with i18next when translation is being stored in the database, it retrieves required translations from database,
and store missing keys sent from from frontend .


Quick start
-----------

1. Add "translation" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'translation',
    ]

2. Include the translation URLconf in your project urls.py like this::

    path('translation/', include('translation.urls')),

3. Run ``python manage.py migrate`` to create the translation models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a translations (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/translation/ to participate in the poll.