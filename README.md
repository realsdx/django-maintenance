# Maintenance mode for Django apps
**Under development**


## Maintenance Mode

A app to show maintenance mode error page(503) to normal users.

Setup
-----------

1.  Run `python setup.py sdist bdist_wheel` .<br>
    This will generate a source archive and a python wheel package.

2.  Now Run `pip install <path_to_the_package>`.<br>
    *Use a virtual environment*


Quick start
-----------

1. Add "maintenance" to your INSTALLED_APPS setting like this::
    ```
    INSTALLED_APPS = [
        ...
        'maintenance',
    ]
    ```

2.  Add 'maintenance.middleware.MaintenanceMiddleware' to last of the MIDDDLEWARE list.
    ```
    MIDDLEWARE = [
    ...
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maintenance.middleware.MaintenanceMiddleware',
    ]
    ```

3. Include the maintenance URLconf in your project urls.py like this::

    ```
    path('maintenance/', include('maintenance.urls')),
    ```

4. Run `python manage.py migrate` to create the maintenance models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to set the boolean value of maintenance mode state (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/ to check if it's working as expected.