git show v1.3:specification/datasets/cost_and_usage/columns/allocatedtags.md \
  | perl -pe 's/\[([^\]]+)\]\([^)]+\)/$1/g' \
  > /tmp/allocatedtags_v13.md && \

git show working_draft:specification/datasets/cost_and_usage/columns/allocatedtags.md \
  | perl -pe 's/\[([^\]]+)\]\([^)]+\)/$1/g' \
  > /tmp/allocatedtags_working.md && \

git diff --no-index \
  --color \
  --word-diff=plain \
  --word-diff-regex='[^[:space:]]+' \
  /tmp/allocatedtags_v13.md /tmp/allocatedtags_working.md
