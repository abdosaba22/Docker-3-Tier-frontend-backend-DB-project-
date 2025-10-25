FROM httpd:2.4

COPY index.html /usr/local/apache2/htdocs/index.html

COPY proxy_modules.conf /usr/local/apache2/conf/extra/proxy_modules.conf

COPY vhost.conf /usr/local/apache2/conf/extra/vhost.conf

RUN echo "Include conf/extra/vhost.conf" >> /usr/local/apache2/conf/httpd.conf

RUN echo "Include conf/extra/proxy_modules.conf" >> /usr/local/apache2/conf/httpd.conf
 
EXPOSE 80
