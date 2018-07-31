<VirtualHost *:80>
    ServerName educationskey.dev
    DocumentRoot /var/www/html/www/educationskey/htdocs
    <Directory "/var/www/html/www/educationskey/htdocs/">
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        Require local
    </Directory>
    ErrorLog "var/www/html/educationskey/logs/error.log"
    CustomLog "var/www/html/educationskey/logs/access.log" common
</VirtualHost>


<VirtualHost *:80>
    ServerName educationskey.dev
    DocumentRoot /var/www/html/educationskey.dev/htdocs
    <Directory "/var/www/html/educationskey.dev/htdocs/">
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        Require local
    </Directory>
    ErrorLog "var/www/html/educationskey.dev/logs/error.log"
    CustomLog "var/www/html/educationskey.dev/logs/access.log" common
</VirtualHost>





<VirtualHost *:80>
    ServerAdmin admin@educationskey.dev
    ServerName educationskey.dev
    ServerAlias www.educationskey.dev
    DocumentRoot /var/www/html/educationskey.dev
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>