FROM nginxinc/nginx-unprivileged:stable-alpine@sha256:15c994d10d6d78658721c3bcafff14cb281fba2a4bdf9d5ba92c416a472516e3
COPY default.conf.template /etc/nginx/templates/default.conf.template
COPY index.html app.js /usr/share/nginx/html/
ENV API_UPSTREAM=http://api:8080
USER 101
EXPOSE 8080
