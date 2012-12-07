# BATMAN

A Python deployment toolbelt

![batman](http://1.bp.blogspot.com/-z0lXpuKOQXQ/UFZE-PjgIPI/AAAAAAAADrM/HrzTbznSYFI/s1600/famous-cartoon-character-batman.jpg)

## Usage

Create a `.batman.yml` file in your repository.  You can set the name of the virtualenv to run, the temp directory used to store hashes, the list of files to check for updates, and the commands to run when those files change.   You can also provide a list of symlinks that should be created, if they aren't already.

Batman should be called by an automated deployment script, but you can call it manually like this:

`batman /full/path/to/project`

## Assumptions

You need pip, virtualenv, virtualenvwrapper, and python already installed on your deployment target.

## .batman.yml

 * **virtualenv** specify the virtualenv to install packages into for this repository
 * **hash_dir** the temp directory to store hashes in. This is how batman can tell if your files have changed.
 * **add2virutalenv** Add these paths to the virtualenv
 * **update_on_change** Mapping from file to watch to command to run if the file changes
 * **ensure_symlinks** Mapping from symlink name to target to create symlinks.  You can use paths relative to the project root for src if you want.
 * **delete_pattern** command-line glob that will search the directory structure and delete all files matching this pattern.  Be careful with this one!

## Example .batman.yml (this one is used for our rg2 app)

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

## License

This project uses the MIT license. See LICENSE file for more details
