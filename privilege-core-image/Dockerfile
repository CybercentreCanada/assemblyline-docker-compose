ARG version=latest
ARG registry
FROM ${registry}cccs/assemblyline-core:$version

USER root
RUN ln -s /var/lib/assemblyline/.local /root/.local
