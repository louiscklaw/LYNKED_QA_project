#!/usr/bin/env bash

set -ex

pushd _ref/docker-appium

  docker-compose pull

  docker-compose build

  docker-compose up

popd
