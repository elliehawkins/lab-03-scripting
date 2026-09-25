#!/bin/bash
set -euo pipefail
curl https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz
# tar
# tr can squeeze repeated newlines
cat myfile.tsv | tr -s '\n' > cleaned.tsv