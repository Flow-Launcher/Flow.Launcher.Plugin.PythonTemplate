# Python Template for Wox Plugin

Just a Python Template Advice for Wox plugin, not a plugin.

You can follow the template advice or not. But it could be better if you do.

## :file_folder: File Structure

``` 
.
│  README.md
│  LICENSE
│  plugin.json
│  .gitignore
│  .env  # user config file
│  main.py
│  test.py
|  commands.py  # commands for developer
│  requirements.txt
|  requirements-dev.txt  # only for developer
|  babel.cfg  # `babel` config file
│
├─assets
│      example.png
│      favicon.ico
│
└─plugin  # main scripts
        __init__.py
        extensions.py
        settings.py
        templates.py
        ui.py
        utils.py
        └──translations  # localization
                ├─en_US
                └─zh_CN
```

## :sparkles: Features

### :desktop_computer: Commandas

Using `click` to integrate the command function.

We can use the command to update `plugin.json` from the package itself.

Just like follow.

``` 
python commands.py gen-plugin-info
```

### :globe_with_meridians: Localizations

Using `gettext` to integrate localization function.

We can init a language like follow.

``` 
python commands.py init lang
```

Then we can fill `.po` file in **translations** folder.

If something changed, you can take this to update the information.

``` 
python commands.py update
```

After all of this, we need to compile the `.po` to `.mo` file.

``` 
python commands.py compile
```

## :runner: ToDos

* [x] auto commands
* [x] local language
* [ ] inputs parser, for mulity inputs
* [ ] setting ui for wox
