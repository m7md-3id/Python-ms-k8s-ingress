# Python-ms-k8s-ingress
A simple flask web server with 3 end points as micro service deployed in k8s and accesses with nginx ingress

The three endpoints the app will serve is (/, /requests, /quieries).

Each endpoint deployed as a stand alone service and traffic is controled by nginx ingress deployed in k8s.

Redis server is used to cache and store the hits.

