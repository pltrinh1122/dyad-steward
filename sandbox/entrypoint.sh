#!/bin/sh
# /src = the fetched PR code, bind-mounted READ-ONLY (host copy stays pristine, code can't tamper it).
# /work = ephemeral tmpfs (writable). Copy src->work so code that writes (e.g. falsify.py seen-state)
# works, while nothing escapes the container and our fetched copy is untouched.
set -eu
if [ -d /src ]; then
  cp -a /src/. /work/ 2>/dev/null || true
fi
exec "$@"
