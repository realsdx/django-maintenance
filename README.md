# Maintenance mode django apps

*Under development*
<br>
=====
Maintenance Mode    
=====

A app to show maintenance mode error page(503) to normal users.

Quick start
-----------

1. Add "maintenance" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'maintenance',
    ]
2.  Add 'maintenance.middleware.MaintenanceMiddleware' to last of the MIDDDLEWARE list.

3. Include the maintenance URLconf in your project urls.py like this::

    path('maintenance/', include('maintenance.urls')),

4. Run `python manage.py migrate` to create the maintenance models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to set the boolean value of maintenance mode state (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/ to check if it's working as expected.