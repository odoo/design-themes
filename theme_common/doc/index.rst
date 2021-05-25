You need to install the *Less CSS* compiler to run this module

* on Linux, use your distribution's package manager to install nodejs and npm.
   * In debian wheezy and Ubuntu 13.10 and before you need to install nodejs manually:

       .. code-block:: console

           $ wget -qO- https://deb.nodesource.com/setup | bash -
           $ apt-get install -y nodejs

   * In later debian (>jessie) and ubuntu (>14.04) you may need to add a symlink as npm packages call ``node`` but debian calls the binary ``nodejs``

       .. code-block:: console

           $ apt-get install -y npm
           $ sudo ln -s /usr/bin/nodejs /usr/bin/node

   * Once npm is installed, use it to install less and less-plugin-clean-css:

       .. code-block:: console

           $ sudo npm install -g less less-plugin-clean-css

* on OS X, install nodejs via your preferred package manager (`homebrew <http://brew.sh/>`_, `macports <https://www.macports.org/>`_) then install less and less-plugin-clean-css:

   .. code-block:: console

       $ sudo npm install -g less less-plugin-clean-css

* on Windows, `install nodejs <http://nodejs.org/download/>`_, reboot (to update the `PATH`) and install less and less-plugin-clean-css:

   .. code-block:: ps1

       C:\> npm install -g less less-plugin-clean-css
