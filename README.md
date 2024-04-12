# stacked-diff-test
Repository to test out the flows of stacked diffs with open source tools.

Tools tested:
 - git-branchless
 - sapling
 - jj
 - Stacked Git
 - Maiao

This analysis will have a few goals and a few non-goals.

The goals are tied to being able to chunk one large piece of code into separate reviewable units and end up in a format that supports deployment. This inevitably means that some of these tools work better in ideal situations (trunk-based development) and some work better in non-ideal situations. It's fine to decide one approach is better overall, but we should keep in mind our limitations.

The non-goals are evaluating anything else other than stacked-diffness for reviews, e.g. "trunk based development is good".

TODO: List common workflows w.r.t. pushing-pulling in between commits and how it interacts with amending locally etc.

