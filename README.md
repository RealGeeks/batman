# BATMAN

A Python deployment toolbelt

# Usage

Create a `.batman.yml` file in your repository.  You can set the name of the virtualenv to run, the temp directory used to store hashes, the list of files to check for updates, and the commands to run when those files change.  

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
```
