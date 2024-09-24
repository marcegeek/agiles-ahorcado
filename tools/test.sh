#!/bin/sh
cd "$(dirname $0)/.."
coverage run -m pytest &&
coverage run --append -m behave

coverage report
