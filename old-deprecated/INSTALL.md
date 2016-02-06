# Installation Instructions (osx)

    $ brew update
    $ brew install python
    $ brew install caskroom/cask/brew-cask
    $ brew cask install gnucash
    $ brew install mysql 

# Bootstrap Database Instructions (osx/*nix)

The `mysql` installation assumes a root user with a password set.

    $ mysql.server start
    $ ./bootstrap.sh

# Import Data Instructions (osx/*nix)

A ssh config entry for `Hostname dev-app.denhac.org` `Host 10.0.101.248` is assumed.

    $ scp dev-app.denhac.org:/srv/dev-database.sql data/.
    $ ./data/import.sh


# Bootstrap Application (osx/*nix)

	$ pip install --upgrade pip
    $ pip install Flask
	$ pip install python-ldap
