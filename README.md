# BATMAN

A Python deployment toolbelt [![Build Status](https://travis-ci.org/RealGeeks/batman.png)](https://travis-ci.org/RealGeeks/batman)

![batman](http://1.bp.blogspot.com/-z0lXpuKOQXQ/UFZE-PjgIPI/AAAAAAAADrM/HrzTbznSYFI/s1600/famous-cartoon-character-batman.jpg)

## Usage

Create a `.batman.yml` file in your repository.  You can set the name of the virtualenv to run, the temp directory used to store hashes, the list of files to check for updates, and the commands to run when those files change.   You can also provide a list of symlinks that should be created, if they aren't already.

Batman should be called by an automated deployment script, but you can call it manually like this:

`batman /full/path/to/project`

## Installation
Batman is in pip, so you should be able to:

```
pip install batman
```

and it will be installed.  I usually install Batman in the system site-packages, since a big advantage of using Batman is that it manages your virtual environments for you.

## Motivations

I had a lot of code that always ended up in my deployment scripts that all did the same things:

1. If a file changes, do X
2. If a virtualenv doesn't exist, create it
3. Add paths to a virtualenv
4. Add symlinks if they don't already exist
5. Delete files if they exist

Now my fabric scripts just call batman, and I can eliminate the code from my deployment scripts.

## Assumptions

Batman is an *opinionated* tool and makes several assumptions about your deployment target platform.

1. You need pip, virtualenv, virtualenvwrapper, bash, and python already installed on your deployment target.  
2. virtualenvwrapper should be installed and working in the environment where you execute batman
3. Since it uses the `select()` and  `fcntl()` system calls, Batman probably only works on linux systems.
4. `virtualenvwrapper.sh` should be in your PATH on your deploy target machine


## .batman.yml

 * **virtualenv** specify the virtualenv to install packages into for this repository
 * **hash_dir** the temp directory to store hashes in. This is how batman can tell if your files have changed.
 * **add2virutalenv** Add these paths to the virtualenv (this should be a *list*)
 * **update_on_change** Mapping from file to watch to command to run if the file changes
 * **ensure_symlinks** Mapping from symlink name to target to create symlinks.  You can use paths relative to the project root for src if you want.
 * **delete_pattern** command-line glob that will search the directory structure and delete all files matching this pattern.  Be careful with this one!

## Paths

All paths in the .batman.yml file are relative to the directory containing the .batman.yml file.  You can also use `~`, which will expand to 
the home directory of the user running the `batman` command.

You can also use absolute paths.

## Example .batman.yml (this one is used for the RealGeeks internal rg2 app)

```yaml
virtualenv: rg2
hash_dir: ~/tmp/hashes/
delete_pattern: "*.pyc"

update_on_change:
  requirements.txt: "PIP_DOWNLOAD_CACHE=\"$HOME/tmp/pip_cache\" pip install -r requirements.txt"
  static/js/: "./manage.py synccompress --settings=settings"
  styler/source/template/: "./manage.py run_management_command_on_all_sites restyle --settings=settings.settings_mcp"

ensure_symlinks:
  ~/conf/nginx.conf: ~/rg2/server_config/nginx.conf
  ~/rg2/static/media: ~/.virtualenvs/rg2/lib/python2.7/site-packages/django/contrib/admin/media:
```

## Other notes

The `update_on_change` key can take any glob that bash can expand.  For example:

```yaml
update_on_change:
    "*/migrations/*": "./manage.py migrate"
```

The update_on_change commands will only be rerun if one the following conditions are met:

  1. The command changes in the `.batman.yml` file
  2. The command was just added to the `.batman.yml` file
  3. The contents of the file (or any of the files matching the glob) in the key are changed

Whether or not a file is changed is based on the hash of the file, *not* the modified time.

## Changelog

_0.6.0_ Change internal serialization format to yaml isntead of python literal syntax.  This will make all of your `update_on_change` stuff run, so I'm doing a minor version bump.
_0.5 and below_ : I didn't keep track of my changes

## License

This project uses the MIT license. See LICENSE file for more details
