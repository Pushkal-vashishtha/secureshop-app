FROM nginxinc/nginx-unprivileged:stable-alpine@sha256:ed04ec1ff34502c339ee5c3ae3f855442398edc1d05591e2b98981dcbbd20b1e
COPY default.conf.template /etc/nginx/templates/default.conf.template
COPY index.html app.js /usr/share/nginx/html/
ENV API_UPSTREAM=http://api:8080
USER 101
EXPOSE 8080
