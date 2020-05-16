d ##
upstream odoo {
server odoo1.com:2019;
}

server {
listen 443 ssl default_server;
listen [::]:443 ssl default_server;
server_name odoo1.com www.odoo1.com;
root /usr/share/nginx/html;
index index.html index.htm;

# log files
access_log /var/log/nginx/odoo.access.log;
error_log /var/log/nginx/odoo.error.log;

# ssl filess
ssl on;
ssl_ciphers ALL:!ADH:!MD5:!EXPORT:!SSLv2:RC4+RSA:+HIGH:+MEDIUM;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_prefer_server_ciphers on;
ssl_certificate /etc/nginx/ssl/odoo.crt;
ssl_certificate_key /etc/nginx/ssl/odoo.key;

# proxy buffers
proxy_buffers 16 64k;
proxy_buffer_size 128k;

location / {
        proxy_pass  http://odoo;
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
        proxy_redirect off;

        proxy_set_header    Host            $host;
        proxy_set_header    X-Real-IP       $remote_addr;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Forwarded-Proto https;
    }

    location ~* /web/static/ {
        proxy_cache_valid 200 60m;
        proxy_buffering on;
        expires 864000;
        proxy_pass http://odoo;
    }
}

#########################################################
server {
server_name odoo2.com www.odoo2.com;
root /usr/share/nginx/html;
index index.html index.htm;

# log files
access_log /var/log/nginx/odoo.access.log;
error_log /var/log/nginx/odoo.error.log;


# proxy buffers
proxy_buffers 16 64k;
proxy_buffer_size 128k;

location / {
        proxy_pass  http://odoo;
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
        proxy_redirect off;

        proxy_set_header    Host            $host;
        proxy_set_header    X-Real-IP       $remote_addr;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Forwarded-Proto https;
    }

    location ~* /web/static/ {
        proxy_cache_valid 200 60m;
        proxy_buffering on;
        expires 864000;
        proxy_pass http://odoo;
    }
}
