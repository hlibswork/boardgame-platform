﻿#BoardGame Platform 🎲

A project for managing board games and events in Django.  
Implemented a system of players and hosts, event creation, event registration, search, filtering, authorization and basic administration.

## Functionality:
- User with the role `Player` or `Host`.
- Create/edit/delete games and events
- Participation in events (registration/cancellation)
- Filtering and searching by genre/game name
- Pagination with support for filters
- Personal authorization (login/logout)
- Visits counter on the main page
- Display of registered events
- Custom `Player` model based on `AbstractUser`
- Tests for models, forms, views, admin

## Check it Out:
[https://boardgame-platform-j85g.onrender.com/](https://boardgame-platform-j85g.onrender.com/)

## Technologies:
- Python 3.9
- Django 4.2
- Bootstrap
- SQLite (built-in database for convenience)
- crispy-bootstrap4

To see the filled platform:

python manage.py loaddata boardgames_fixture.json

admin user
Hlib
12345678g
 
