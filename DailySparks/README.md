DailySparks
============

DailySparks is a tiny Python utility that returns short, actionable micro-challenges
you can complete in a few minutes. It's designed to create small, repeatable
moments of progress and mindfulness in a busy day.

Usage
------

Import and call:

    from DailySparks import get_spark, add_favorite, list_favorites

    print(get_spark())

Save favorites and list them:

    add_favorite("Drink a full glass of water right now.")
    print(list_favorites())

Persistence
-----------

Favorites are saved to `DailySparks/data/favorites.json` next to the package.
