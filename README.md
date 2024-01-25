# Overnight

This command line application will fetch Github milestones and issues, and creates one or more
Pull Requests for each.

You can then review and comment on those Pull Requests, and it will refine the branches.

## Usage

Prerequisites:

* You must have `OPENAI_ACCESS_TOKEN` and `GITHUB_TOKEN` set in your environment.

```console
$ python overnight.py --repository Overbryd/overnight
```

