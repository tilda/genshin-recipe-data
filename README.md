# `genshin-recipe-data`
A repository to keep a current copy of Genshin Impact's cooking recipe data. Updated on a best effort basis.

# Why?
I'm making tools for myself as someone trying to be a completionist in a gacha game, despite how stupid it sounds.

This was originally in [enkanomiya](https://github.com/tilda/enkanomiya) but since I am making another project using this data, it makes more sense to share a repository between the 2 projects.

For the record, all of this was typed out manually for the most part.

# How to use it?
Simply use the data in `static/recipes.json`. It's a big JSON object basically looking like this:
```js
{
    "food-name": {
        "name": "Food Name",
        "rarity": 1,
        "location": "Where you can find it"
    }
    // and it goes on... and on
}
```

# License
Unlicense, public domain, whatever you want to call it. You are free to use this data however you see fit, because I didn't make the game anyway.