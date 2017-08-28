# Flask-template-project

This is an app template that helps me
speed up the head work when building flask apps.

It is ideal for small projects and/or hackathons.

## Included goodies
This template project comes preloaded with:

* **bootstrap 3.3.7**
* **jQuery 2.2.4**
* **peewee**, *a python3 ORM*
* **`tools`** submodule, which includes:
	* simple SHA-224 hashing function
	* simple string sanitizing function (via `bleach` package.)
* **a simple admin interface** (via `flask-admin` package)
*   * The admin interface is located under `/admin/`
*   * Default credentials for login are u:`admin` p:`1234` (**change this**)

## Supported deployment options
Out of the box, this template supports following deployment options:

1. test server - popular `app.run()`
2. running with **gunicorn**
3. deploying to **Heroku**
4. building & deploying a **docker** image

---

*I do not advise you to use this template in its original state for more serious projects.*
