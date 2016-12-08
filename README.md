# kairx-deploy
The purpose of this repository to is keep track of how our web applications were deployed for
experimentation during Optimizely set up.

## Deployment
Utilizing a reverse proxy (NGINX) to expose our two sites on differing
ports on an OIT VM (colab-sbx-64). Control will be port 80 and intervention will
be port 6004.

#### Deploy Production
```
#adding this image so that we have a vim to play with inside the container
docker build -t nginx/vim .

docker run -d -p 80:80 \
-v $(pwd)/control:/usr/share/nginx/html2 \
-v $(pwd)/control/nginx_conf_control:/etc/nginx \
--name kairx_control \
--restart=always \
nginx/vim

docker run -d -p 6004:80 \
-v $(pwd)/intervention:/usr/share/nginx/html2 \
-v $(pwd)/intervention/nginx_conf_intervention:/etc/nginx \
--name kairx_intervention \
--restart=always \
nginx/vim
```

#### Mirrored Deploy
```
#adding this image so that we have a vim to play with inside the container
docker build -t nginx/vim .

docker run -d -p 8013:80 \
-v $(pwd)/control:/usr/share/nginx/html2 \
-v $(pwd)/control/nginx_conf_control:/etc/nginx \
--name kairx_control_mirror \
--restart=always \
nginx/vim

docker run -d -p 8014:80 \
-v $(pwd)/intervention:/usr/share/nginx/html2 \
-v $(pwd)/intervention/nginx_conf_intervention:/etc/nginx \
--name kairx_intervention_mirror \
--restart=always \
nginx/vim
```
