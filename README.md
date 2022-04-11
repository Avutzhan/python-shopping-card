# python-shopping-card

Bugs:
* from docker container to localhost
* from docker container to localhost:8000 and other ports

On MacOs just use  docker.for.mac.localhost to get localhost

but in linux you have bad options.
* extra_hosts:
  - "host.docker.internal:172.17.0.1"
  * if you use it you can access just to localhost other ports closed
  * you must configure your service to localhost:80 to access directly
  * or publish to internet to get access directly without problems
* network_mode: host
  * here is problems to connect other containers by container name
  * you must rewrite connections by absolute path