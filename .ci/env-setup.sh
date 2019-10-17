#!/usr/bin/env bash

pushd /root
rm -rf .ccache
git clone --depth=1 https://$GITID:$GITPWD@github.com/wloot/tc-dump.git -b ccache .ccache
popd
ccache -s

# Clear out the stats so we actually know the cache stats
ccache -z

# Prepend ccache into the PATH
export PATH="/usr/lib/ccache:$PATH"
