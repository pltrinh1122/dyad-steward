# PR-review sandbox image — runs untrusted PR code (python + gh + pyyaml) in a contained box.
# Pinned, reproducible, non-root. No credentials are ever baked in or mounted (see bin/pr-sandbox).
FROM python:3.12-slim

ARG GH_VERSION=2.63.2

RUN set -eux; \
    pip install --no-cache-dir pyyaml==6.0.2; \
    apt-get update; \
    apt-get install -y --no-install-recommends ca-certificates curl; \
    curl -fsSL "https://github.com/cli/cli/releases/download/v${GH_VERSION}/gh_${GH_VERSION}_linux_amd64.tar.gz" -o /tmp/gh.tgz; \
    tar -xzf /tmp/gh.tgz -C /tmp; \
    mv "/tmp/gh_${GH_VERSION}_linux_amd64/bin/gh" /usr/local/bin/gh; \
    apt-get purge -y curl; apt-get autoremove -y; \
    rm -rf /tmp/gh* /var/lib/apt/lists/*; \
    useradd -m -u 10001 sandbox

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 0755 /usr/local/bin/entrypoint.sh

USER sandbox
ENV HOME=/work
WORKDIR /work
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["sh", "-c", "echo '[pr-sandbox] no command given; PR code is at /work'; ls -la /work"]
