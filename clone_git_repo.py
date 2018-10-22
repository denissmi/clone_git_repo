"""
The script clones git remote repo to the local path or pulls the last changes if the repo exists.

Example of the usage:
python clone_git_repo.py --git-url https://github.com/denissmi/clone_git_repo --branch master
--local_path C:\clone_git_repo
"""
import argparse
import git
import pathlib


def local_repo(local_path: pathlib.Path, git_url: str = None):
    """
    Clones remote git repo if this one does not exists and git url assigned, then returns the local repo.

    :param local_path: local path to the repo
    :param git_url: git repo URL address
    :return: git.Repo object
    """
    if local_path.exists():
        return git.Repo(local_path)
    elif git_url:
        return git.Repo.clone_from(git_url, local_path)

    return None


def parse_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--git-url', dest='git_url', required=True, help='Gir repo URL address')
    parser.add_argument('--branch', dest='branch', default='master', help='Repo branch')
    parser.add_argument('--local-path', dest='local_path', type=pathlib.Path, default=pathlib.Path(),
                        help='Path to local repo')

    return parser.parse_args()


def main():
    """The main function."""
    args = parse_arguments()
    repo = local_repo(args.local_path, git_url=args.git_url)
    if not repo:
        # There is no local repo
        return None

    if args.branch not in repo.heads:
        # There is no required branch
        return None

    repo.heads[args.branch].checkout()
    repo.head.reset(index=True, working_tree=True)

    origin = repo.remote()
    origin.pull()

    return None


if __name__ == '__main__':
    main()
