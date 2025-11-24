FROM alpine:3.18

# Install lighttpd en curl voor health checks
RUN apk add --no-cache lighttpd curl

# Copy configuratie bestanden
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf
COPY index.html /var/www/localhost/htdocs/index.html

# Fix permissions - belangrijk!
RUN mkdir -p /var/log/lighttpd && \
    chown -R lighttpd:lighttpd /var/log/lighttpd /var/www/localhost && \
    chmod -R 755 /var/www/localhost/htdocs

# Expose poort
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

# Start lighttpd
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]