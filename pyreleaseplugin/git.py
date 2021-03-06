# -*- coding: utf-8 -*-
from subprocess import Popen


def is_tree_clean():
    """
    Check if git working tree is clean.

    Returns:
        False if there are uncommited changes, True otherwise
    """
    return False if Popen(["git", "diff-files", "--quiet"]).wait() else True


def commit_changes(projectName, version):
    """
    Commit current release changes.

    Args:
        version (str): The version specifier to include in the commit message
    """
    commit_message = "Update version file and changlog for release {}-{}".format(projectName, version)
    code = Popen(["git", "commit", "-a", "-m", commit_message]).wait()
    if code:
        raise RuntimeError("Error committing changes")


def tag(projectName, version):
    """
    Add a tag to the release.

    Args:
        version (str): The version specifier to include in the commit message
    """
    tag = "{}-{}".format(projectName, version)
    code = Popen(["git", "tag", tag]).wait()
    if code:
        raise RuntimeError("Error tagging release")


def push_code(branch):
    """
    Push code changes to git branch `branch`.
    """
    code = Popen(["git", "push", "origin", branch]).wait()
    if code:
        raise RuntimeError("Error pushing changes to git")


def push_tags():
    """
    Push tags to git.
    """
    code = Popen(["git", "push", "--tags"]).wait()
    if code:
        raise RuntimeError("Error pushing tags to git")


def push(release_branch):
    """
    Push commits and tags to Github.
    """
    push_code(release_branch)
    push_tags()
