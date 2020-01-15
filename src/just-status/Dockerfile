FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/
COPY nginx.conf /etc/nginx

# VOLUME /usr/share/nginx/html
# VOLUME /etc/nginx