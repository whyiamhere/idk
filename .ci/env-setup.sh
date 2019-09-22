#!/usr/bin/env bash

# Show all commands and exit upon failure
set -eux

# Install the latest clang snapshot
curl https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
echo "deb http://apt.llvm.org/disco/ llvm-toolchain-disco main" >> /etc/apt/sources.list
apt update
apt install clang-10 lld-10 -y
export LD=ld.lld-10
export CC=clang-10
export CXX=clang++-10

pushd /root
rm -rf .ccache
git clone --depth=1 https://$GITID:$GITPWD@github.com/wloot/tc-dump.git -b ccache .ccache
popd
git clone --depth=1 https://$GITID:$GITPWD@github.com/wloot/tc-dump.git -b build_llvm build/llvm

ccache -s

# Enable compression so that we can have more objects in
ccache --set-config=compression=true

# Clear out the stats so we actually know the cache stats
ccache -z

# Update ccache symlinks
/usr/sbin/update-ccache-symlinks

# Prepend ccache into the PATH
export PATH="/usr/lib/ccache:$PATH"
