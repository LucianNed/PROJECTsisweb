# PROJECTsisweb
web application to manage a small game database

run:
$python manage.py runserver

API:
/api/games/             GET
/api/games/[id]         GET
/api/platforms/         GET
/api/platforms/[id]     GET
/api/accesories/        GET
/api/accesories/[id]    GET
/api/regions/           GET
/api/regions/[id]       GET
/api/favorites/         GET,PUT
/api/favorites/[id]     GET,POST,DEL
/api/gamescores/        GET,PUT
/api/gamescores/[id]    GET,POST,DEL
/api/releases/          GET
/api/releases/[id]      GET

response: json, xml

added features:
-users can save a favorite game ()
-users can give game ratings(also update and delete them)
-added api

first version features:
-users can see games for platforms
-users can see platforms and all their games
-users can view the release dates of the games on a platform in a certain region
-users can view accesories available for selected platform

