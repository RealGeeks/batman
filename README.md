# BATMAN

A Python deployment toolbelt

![batman](http://1.bp.blogspot.com/-z0lXpuKOQXQ/UFZE-PjgIPI/AAAAAAAADrM/HrzTbznSYFI/s1600/famous-cartoon-character-batman.jpg)

# Usage

Create a `.batman.yml` file in your repository.  You can set the name of the virtualenv to run, the temp directory used to store hashes, the list of files to check for updates, and the commands to run when those files change.   You can also provide a list of symlinks that should be created, if they aren't already.

Batman should be called by an automated deployment script, but you can call it manually like this:

`batman /full/path/to/project`

## Example .batman.yml (this one is used for our rg2 app)

```yaml
virtualenv: rg2
hash_dir: ~/tmp/hashes/

update_on_change:
  requirements.txt: "PIP_DOWNLOAD_CACHE=\"$HOME/tmp/pip_cache\" pip install -r requirements.txt"
  static/js/: "./manage.py synccompress --settings=settings"
  styler/source/template/: "./manage.py run_management_command_on_all_sites restyle --settings=settings.settings_mcp"

ensure_symlinks:
  ~/rg2/server_config/nginx.conf: ~/conf/nginx.conf
  ~/.virtualenvs/rg2/lib/python2.7/site-packages/django/contrib/admin/media: ~/rg2/static/media
```
