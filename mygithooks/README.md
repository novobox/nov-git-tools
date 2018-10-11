INSTALLATION
------------

* cp post-checkout (PROJECT)/.git/hooks/
* Edit (PROJECT)/.git/hooks/post-checkout 
* Replace path_to_changelog=/absolute-path/to/your/CHANGELOG.txt


USE WITH GIT FLOW
-----------------

* git flow release start <tag>
* /absolute-path/to/your/CHANGELOG.txt modified (copy git logs since last version) -> edit it


NOTICE
------

* First tag is empty
* Don't work with "hotfixes" (git flow hotfix start)
* Never call a branch "..release.."
