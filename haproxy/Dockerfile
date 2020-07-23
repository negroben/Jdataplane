FROM haproxy:2.2
COPY ./conf/haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
COPY ./conf/dataplaneapi /usr/local/bin
COPY ./conf/dataplane.service /etc/systemd/
COPY ./conf/dataplaneapiex /usr/local/sbin