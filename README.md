# stacked-diff-test
Repository to test out the flows of stacked diffs with open source tools.

The goals are tied to being able to chunk one large piece of code into separate reviewable units and end up in a format that supports deployment. This inevitably means that some of these tools work better in ideal situations (trunk-based development) and some work better in non-ideal situations. It's fine to decide one approach is better overall, but we should keep in mind our limitations.

Limitations: 
 - The platform is GitHub.
 - Trunk-based development is not really possible to change to, because of the way existing tooling works.
 - Another code review tool MIGHT be possible, especially if it's free or can work in the context of self-hosted OSS that your team has to agree to use.

